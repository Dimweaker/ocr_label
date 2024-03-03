import os

ORIGIN_PATH = 'train_label.txt'
NEW_PATH = 'train_label_new.txt'
CHANGE_PATH = 'train_label_change.txt'


class Manager:
    @staticmethod
    def load(data_path: str):
        with open(data_path, 'r', encoding="utf-8") as f:
            data = map(lambda x: x.strip().split('\t'), f.readlines())
            return {
                image_path: text_label for image_path, text_label in data
            }

    def save(self):
        with open(NEW_PATH, 'w', encoding="utf-8") as f:
            for image_path, text_label in self.new.items():
                f.write(f'{image_path}\t{text_label}\n')

        with open(CHANGE_PATH, 'w', encoding="utf-8") as f:
            for image_path in self.changes:
                f.write(f'{image_path}\n')

    def __init__(self):
        self.origin = self.load(ORIGIN_PATH)

        if os.path.exists(NEW_PATH):
            self.new = self.load(NEW_PATH)
        else:
            self.new = self.origin
            self.save()

        if os.path.exists(CHANGE_PATH):
            with open(CHANGE_PATH, 'r', encoding="utf-8") as f:
                self.changes = set(x.strip() for x in f.readlines())
        else:
            self.changes = set()

        with open('result.txt', 'r', encoding="utf-8") as f:
            prediction = map(lambda x: x.strip().split('\t'), f.readlines())
            self.prediction = {image_path: (text_label, score) for image_path, text_label, score in prediction}

        self.image_paths = list(self.new.keys())
        self.index = 0

    def is_changed(self, image: str | int) -> bool:
        if isinstance(image, int):
            image = self.image_paths[image]
        if image.isdigit():
            image = f"train/mg_crop_{image}.jpg"
        return image in self.changes

    def next_unchanged(self):
        i = self.index
        while self.is_changed(i):
            i += 1
            if i >= len(self.image_paths):
                return None
        self.index = i
        return self.image_path

    def last_unchanged(self):
        i = self.index
        while self.is_changed(i):
            i -= 1
            if i < 0:
                return None
        self.index = i
        return self.image_path

    def jump(self, image: str | int):
        if isinstance(image, int):
            image = self.image_paths[image]
        if ':' in image:
            image = int(image.split(':')[-1])
            image = self.image_paths[image]
        if image.isdigit():
            image = f"train/mg_crop_{image}.jpg"
        try:
            self.index = self.image_paths.index(image)
        except ValueError:
            print(f"Image {image} not found")
            return None
        return image

    def change(self, text: str):
        self.new[self.image_path] = text
        self.changes.add(self.image_path)
        self.save()

    def restore(self):
        self.new = self.origin
        self.changes.remove(self.image_path)
        self.save()

    @property
    def image_path(self) -> str:
        return self.image_paths[self.index]

    @property
    def text_label(self) -> str:
        return self.new[self.image_paths[self.index]]

    @property
    def text_label_origin(self) -> str:
        return self.origin[self.image_paths[self.index]]

    @property
    def prediction_text_label(self) -> str:
        return self.prediction[self.image_paths[self.index]][0]

    @property
    def prediction_score(self) -> float:
        return float(self.prediction[self.image_paths[self.index]][1])
