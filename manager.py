from pandas import read_csv
from configparser import ConfigParser
from remote import Remote
from datetime import datetime


class Manager:

    def __init__(self):
        conf = ConfigParser(strict=False)
        conf.read('config.ini')
        self.label_user = conf.get('user', 'label_user')
        host = conf.get('remote', 'host')
        username = conf.get('remote', 'username')
        password = conf.get('remote', 'password')
        self.remote = Remote(host, username, password)

        self.local_path = conf.get('data', 'local_path')
        self.remote_path = conf.get('data', 'remote_path')
        self.buffer_path = conf.get('data', 'buffer_path')

        self.bool_cols: list[str] = eval(conf.get('column', 'bool_cols'))

        self.data = read_csv(self.local_path, sep="\t", index_col=0, encoding="utf-8")
        self.data["time"] = self.data["time"].astype("datetime64[ns]")

        self.index = 0

    def __getattr__(self, item):
        # 在pandas模块中，如果列是bool类型，那么返回的是numpy.bool_类型，但在checkBox设置值时，需要返回python的bool类型，否则会报错
        # "DeprecationWarning: In future, it will be an error for 'np.bool_' scalars to be interpreted as an index"
        if item in self.bool_cols:
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

    @property
    def time(self) -> datetime:
        return self.item['time']

    @property
    def user(self) -> str:
        return self.item['user']

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
               space: bool = False, alien: bool = False,
               traditional: bool = False, clarity: int = 5):
        self.data.at[self.image_path, 'text_label_new'] = text
        self.data.at[self.image_path, 'uncertain'] = uncertain
        self.data.at[self.image_path, 'invalid'] = invalid
        self.data.at[self.image_path, 'punctuation'] = punctuation
        self.data.at[self.image_path, 'symbol'] = symbol
        self.data.at[self.image_path, 'space'] = space
        self.data.at[self.image_path, 'alien'] = alien
        self.data.at[self.image_path, 'traditional'] = traditional
        self.data.at[self.image_path, 'clarity'] = clarity
        self.data.at[self.image_path, 'change'] = True
        self.data.at[self.image_path, 'user'] = self.label_user
        self.data.at[self.image_path, 'time'] = datetime.now()

    def restore(self):
        self.data.at[self.image_path, 'text_label_new'] = self.text_label_origin
        self.data.at[self.image_path, 'change'] = False
        self.data.at[self.image_path, 'uncertain'] = False
        self.data.at[self.image_path, 'invalid'] = False
        self.data.at[self.image_path, 'punctuation'] = False
        self.data.at[self.image_path, 'symbol'] = False
        self.data.at[self.image_path, 'space'] = False
        self.data.at[self.image_path, 'alien'] = False
        self.data.at[self.image_path, 'traditional'] = False
        self.data.at[self.image_path, 'clarity'] = 5
        self.data.at[self.image_path, 'user'] = "baidu"
        self.data.at[self.image_path, 'time'] = datetime.now()

    def save(self):
        self.data.to_csv(self.local_path, sep="\t", encoding="utf-8")

    def remote_load(self):
        self.remote.load_data(self.remote_path, self.buffer_path)
        buffer = read_csv(self.buffer_path, sep="\t", index_col=0, encoding="utf-8")
        buffer["time"] = buffer["time"].astype("datetime64[ns]")
        self.data = self.data.combine(buffer, lambda x, y: x if x[-1] > y[-1] else y)

    def remote_save(self):
        self.remote.load_data(self.remote_path, self.buffer_path)
        buffer = read_csv(self.buffer_path, sep="\t", index_col=0, encoding="utf-8")
        buffer["time"] = buffer["time"].astype("datetime64[ns]")
        buffer.combine(self.data, lambda x, y: x if x[-1] > y[-1] else y).to_csv(self.buffer_path, sep="\t",
                                                                                 encoding="utf-8")
        self.remote.save_data(self.buffer_path, self.remote_path)
