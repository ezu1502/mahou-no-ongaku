from mahou.window import MahouWindow

class App:
    def __init__(self) -> None:
        self.window = MahouWindow(app = self)

    def run(self):
        self.window.launch()