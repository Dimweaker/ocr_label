import numpy as np
import os
import pandas as pd

DATA_PATH = 'data.csv'
BOOL_COLS = ['uncertain', 'invalid', 'punctuation', 'symbol', 'space', 'change']


class Manager:

    def __init__(self):
        self.data = pd.read_csv(DATA_PATH, sep="\t", index_col=0, encoding="utf-8")
        self.index = 0

    def __getattr__(self, item):
        # 在pandas模块中，如果列是bool类型，那么返回的是numpy.bool_类型，但在checkBox设置值时，需要返回python的bool类型，否则会报错
        # "DeprecationWarning: In future, it will be an error for 'np.bool_' scalars to be interpreted as an index"
        if item in BOOL_COLS:
            return bool(self.item[item])
        return self.__getattribute__(item)

    @property
    def item(self):
        return self.data.iloc[self.index]

    @property
    def text_label(self) -> str:
        return self.item['text_label_new']

    @property
    def text_label_origin(self) -> str:
        return self.item['text_label_origin']

    @property
    def prediction_text_label(self) -> str:
        return self.item['prediction']

    @property
    def prediction_score(self) -> float:
        return self.item['score']

    @property
    def image_path(self) -> str:
        return self.item["image_path"]

    @property
    def clarity(self) -> int:
        return self.item['clarity']

    def is_changed(self, image: str | int) -> bool:
        if isinstance(image, int):
            return self.data.iloc[image].change
        if image.isdigit():
            image = f"train/mg_crop_{image}.jpg"
        return self.data.loc[image, 'change']

    def next_unchanged(self):
        i = self.index
        while self.is_changed(i):
            i += 1
            if i >= len(self.data):
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
            self.index = image - 1
            return self.image_path
        if image.isdigit():
            image = f"train/mg_crop_{image}.jpg"
        try:
            self.index = self.data.index.get_loc(image)
        except ValueError:
            print(f"Image {image} not found")
            return None
        return image

    def change(self, text: str,
               uncertain: bool = False, invalid: bool = False,
               punctuation: bool = False, symbol: bool = False,
               space: bool = False, clarity: int = 5):
        self.data.at[self.image_path, 'text_label_new'] = text
        self.data.at[self.image_path, 'uncertain'] = uncertain
        self.data.at[self.image_path, 'invalid'] = invalid
        self.data.at[self.image_path, 'punctuation'] = punctuation
        self.data.at[self.image_path, 'symbol'] = symbol
        self.data.at[self.image_path, 'space'] = space
        self.data.at[self.image_path, 'clarity'] = clarity
        self.data.at[self.image_path, 'change'] = True

    def restore(self):
        self.data.at[self.image_path, 'text_label_new'] = self.text_label_origin
        self.data.at[self.image_path, 'change'] = False
        self.data.at[self.image_path, 'uncertain'] = False
        self.data.at[self.image_path, 'invalid'] = False
        self.data.at[self.image_path, 'punctuation'] = False
        self.data.at[self.image_path, 'symbol'] = False
        self.data.at[self.image_path, 'space'] = False
        self.data.at[self.image_path, 'clarity'] = 5

    def save(self):
        self.data.to_csv(DATA_PATH, sep="\t", encoding="utf-8")
