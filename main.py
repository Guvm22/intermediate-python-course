import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.widget import Widget


DICE_ART = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅",
}


class DiceRollerApp(App):
    def build(self):
        self.title = "Pixel Dice Roller"
        Window.clearcolor = (0.12, 0.12, 0.18, 1)

        root = BoxLayout(orientation="vertical", padding=30, spacing=20)

        title = Label(
            text="🎲 Pixel Dice Roller",
            font_size="32sp",
            bold=True,
            color=(0.4, 0.8, 1, 1),
            size_hint=(1, 0.12),
        )
        root.add_widget(title)

        self.dice_label = Label(
            text="⚀",
            font_size="120sp",
            size_hint=(1, 0.45),
            color=(1, 1, 1, 1),
        )
        root.add_widget(self.dice_label)

        self.result_label = Label(
            text="Presiona para lanzar",
            font_size="22sp",
            color=(0.7, 0.7, 0.7, 1),
            size_hint=(1, 0.1),
        )
        root.add_widget(self.result_label)

        sides_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1), spacing=10)
        sides_label = Label(
            text="Caras del dado:",
            font_size="18sp",
            color=(0.8, 0.8, 0.8, 1),
            size_hint=(0.5, 1),
        )
        self.sides_spinner = Spinner(
            text="6",
            values=["4", "6", "8", "10", "12", "20", "100"],
            font_size="18sp",
            size_hint=(0.5, 1),
            background_color=(0.2, 0.5, 0.9, 1),
        )
        sides_layout.add_widget(sides_label)
        sides_layout.add_widget(self.sides_spinner)
        root.add_widget(sides_layout)

        roll_btn = Button(
            text="¡Lanzar!",
            font_size="26sp",
            bold=True,
            size_hint=(1, 0.13),
            background_color=(0.2, 0.6, 1, 1),
            background_normal="",
        )
        roll_btn.bind(on_press=self.roll_dice)
        root.add_widget(roll_btn)

        self.history_label = Label(
            text="Historial: —",
            font_size="14sp",
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, 0.1),
        )
        root.add_widget(self.history_label)

        self.history = []
        return root

    def roll_dice(self, instance):
        sides = int(self.sides_spinner.text)
        result = random.randint(1, sides)

        if sides == 6:
            self.dice_label.text = DICE_ART[result]
        else:
            self.dice_label.text = str(result)

        self.result_label.text = f"Resultado: {result}  (d{sides})"
        self.result_label.color = (0.3, 1, 0.5, 1)

        self.history.append(result)
        if len(self.history) > 6:
            self.history.pop(0)
        self.history_label.text = "Historial: " + "  ".join(str(n) for n in self.history)


if __name__ == "__main__":
    DiceRollerApp().run()
