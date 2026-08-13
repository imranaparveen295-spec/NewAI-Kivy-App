import urllib.parse
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView


class NewAIApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=12, spacing=10)

        title = Label(
            text="🤖 New AI\nSahil has created me",
            size_hint_y=None,
            height=80,
            font_size="22sp",
        )

        self.prompt = TextInput(
            hint_text="Photo kya banani hai? Example: Taj Mahal at sunset",
            multiline=True,
            size_hint_y=None,
            height=110,
        )

        self.status = Label(
            text="Prompt likho aur CREATE IMAGE dabao.",
            size_hint_y=None,
            height=55,
            font_size="16sp",
        )

        button = Button(
            text="CREATE IMAGE",
            size_hint_y=None,
            height=65,
        )
        button.bind(on_press=self.create_image)

        self.image = AsyncImage(
            source="",
            allow_stretch=True,
            keep_ratio=True,
        )

        root.add_widget(title)
        root.add_widget(self.prompt)
        root.add_widget(button)
        root.add_widget(self.status)
        root.add_widget(self.image)

        return root

    def create_image(self, instance):
        q = self.prompt.text.strip().lower()

        if q == "bye":
            self.stop()
            return

        if "photo" not in q and "bana" not in q:
            self.status.text = "Sahi prompt likho — 'photo' ya 'bana' use karo."
            return

        p = q.replace("photo", "").replace("bana", "").strip()

        if not p:
            p = "taj mahal"

        encoded_prompt = urllib.parse.quote(p, safe="")
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        self.status.text = "Image generate ho rahi hai..."
        self.image.source = url
        self.image.reload()
        self.status.text = f"Prompt: {p}"


if __name__ == "__main__":
    NewAIApp().run()
