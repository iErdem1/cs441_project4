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
        super().__init__(**kwargs)
        self.format_list = ["png", "gif", "jpeg", "jpg"]

        self.img_path = "img/"
        self.img_list = list()
        self.img_index = 0

        self.counter = 0

        self.uploading_text = Label(text="Uploading...")

        self.bar = ProgressBar()
        self.body = BoxLayout(orientation="vertical")

        self.info = Label(text="[color=#05f]A. Ihsan Erdem[/color] Image Viewer",
                          markup=True,
                          size_hint_y=.1)

        self.button_bar = BoxLayout(size_hint_y=.15)
        self.next_button = Button(text='Next',
                                  size_hint_x=2,
                                  on_release=self.forward)
        self.prev_button = Button(text='Previous',
                                  size_hint_x=.2,
                                  on_release=self.backward)

    def on_start(self):
        title = Label(text='Game Development Project 4')

    def upload_img(self, file_path):
        file_list = os.listdir(file_path)
        self.bar.max = len(file_list)
        self.bar.value = 0

        for file in file_list:
            if file.split(".")[-1] in self.format_list:
                self.img_list.append(file)

            self.counter += 1
            self.bar.value = self.counter

        #self.uploading_text.text("Images Uploaded!")
        clk.schedule_once(self.start, 1.5)

    def build(self):
        self.body.add_widget(self.uploading_text)
        self.body.add_widget(self.bar)

        clk.schedule_once(lambda event=None: self.upload_img(self.img_path), 1)
        return self.body

    def start(self, event=None):
        self.body.clear_widgets()

        self.img = Image(source=self.img_path + self.img_list[0],
                         allow_stretch=True,
                         keep_ratio=True)

        self.button_bar.add_widget(self.prev_button)
        self.button_bar.add_widget(Widget())
        self.button_bar.add_widget(self.next_button)

        self.body.add_widget(self.info)
        self.body.add_widget(self.img)
        self.body.add_widget(self.button_bar)

    def forward(self, event=None):
        self.img_index += 1

        if self.img_index < len(self.img_list):
            try:
                self.img.source = self.img_path + self.img_list[self.img_index]
                self.info.text = self.img_list[self.img_index]

            except Exception as e:
                self.info.text = "Upload Fail: {}".format(self.img_list[self.img_index])

        else:
            try:
                self.img_index = 0
                self.img.source = self.img_path + self.img_list[self.img_index]
                self.info.text = self.img_list[self.img_index]

            except Exception as e:
                print(e)
                self.info.text = "Upload Fail: {}".format(self.img_list[self.img_index])

    def backward(self, event=None):
        self.img_index -= 1

        if self.img_index >= 0:
            try:
                self.img.source = self.img_path + self.img_list[self.img_index]
                self.info.text = self.img_list[self.img_index]
            except Exception as e:
                print(e)
                self.info.text = "Upload Fail: {}".format(self.img_list[self.img_index])
        else:
            try:
                self.img_index = len(self.img_list) - 1
                self.img.source = self.img_path + self.img_list[self.img_index]
                self.info.text = self.img_list[self.img_index]
            except Exception as e:
                print(e)
                self.info.text = "Upload Fail: {}".format(self.img_list[self.img_index])


Program().run()





