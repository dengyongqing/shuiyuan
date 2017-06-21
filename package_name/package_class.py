import os


class SampleClass():
    def __init__(self, name='sample name'):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self

    def get_login(self):
        return os.getlogin()
