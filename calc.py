from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.result = ""

        layout = BoxLayout(orientation='vertical')
        self.display = Button(text="0", font_size=32, halign='right', size_hint=(1, 0.4), background_color=[0, 0, 1, 1])
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.25, 1))
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current = instance.text

        if current == '=':
            try:
                self.result = str(eval(self.expression))
            except Exception as e:
                self.result = "Error"
            self.expression = ""
        else:
            if current in '0123456789':
                self.expression += current
            elif current in '+-*/.':
                if self.expression and self.expression[-1] not in '+-*/.':
                    self.expression += current

        self.display.text = self.result if self.result else self.expression


if __name__ == '__main__':
    CalculatorApp().run()
