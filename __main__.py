from textual.app import App
from textual.widgets import Log

TEXT = """
[0K I must not fear.[0;m
[0K[0K[36;1m Fear is the mind-killer.[0;m[0;m
[0K Fear is the little-death that brings total obliteration.[0;m
[0K[0K[36;1m I will face my fear.[0;m[0;m
[0K I will permit it to pass over me and through me.[0;m
[0K And when it has gone past, I will turn the inner eye to see its path.[0;m
[0K Where the fear has gone there will be nothing.[0;m
[0K Only I will remain.[0;m
"""


class MyApp(App):
    def compose(self):
        yield Log()

    async def on_ready(self):
        log = self.query_one(Log)
        log.write_line(TEXT)


if __name__ == "__main__":
    app = MyApp(css_path="app.tcss")
    app.run()
