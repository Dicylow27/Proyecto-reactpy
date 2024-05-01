from my_chosen_backend import Application

from reactpy import component, html
from reactpy.backend.my_chosen_backend import configure


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = Application()
configure(app, HelloWorld)