from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock as clk

import os


class Program(App):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.format_list = ["png", "gif", "jpeg", "jpg"]

        self.img_path = "img/"
        self.img_list = list()
        self.img_order = 0

        self.counter = 0

        self.uploading_text = Label(text="Uploading...")

    def upload_img(self, file_path):
        file_list = os.listdir(file_path)
        self.bar.max = len(file_list)
        self.bar.value = 0

        for file in file_list:
            if file.split(".")[-1] in self.format_list:
                self.img_list.append(file)

            self.counter += 1
            self.bar.value = self.counter

        self.uploading_text.text("Images Uploaded!")
        clk.schedule_before(self.start, 1.5)

    def build(self):
        pass

    def start(self):
        pass

    def forward(self):
        pass

    def backward(self):
        pass



