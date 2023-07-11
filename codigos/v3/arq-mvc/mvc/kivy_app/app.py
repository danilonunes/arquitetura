import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.widget import Widget

class ProdutoWidget(Widget):
    pass

class ProdutoApp(App):
    def build(self):
        return ProdutoWidget()

if __name__ == '__main__':
    ProdutoApp().run()
