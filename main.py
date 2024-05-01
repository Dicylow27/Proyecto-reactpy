
from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


@component
def Photo(alt_text, image_id):
    return html.img(
        {
            "src": f"https://picsum.photos/id/{image_id}/500/300",
            "style": {"width": "30%"},
            "alt": alt_text,
        }
    )


@component
def Gallery():
    return html.section(
        html.h1("Famous Musicians"),
        Photo("Landscape", image_id=830),
        Photo("City", image_id=274),
        Photo("Puppy", image_id=237),
    )


@component
def Item(name, done):
        if done:
            return html.li(name, " ✔")
        else:
            return html.li(name)


@component
def TodoList():
    return html.section(
        html.h1("My Todo List"),
        html.ul(
            Item("Encuentra un problema interesante para resolver", done=True),
            Item("Crea una aplicación para resolverlo", done=False),
            Item("¡Comparte esa aplicación con el mundo!", done=True),
        ),
    )




@component
def PagePrin():
    return html.div(
        html.h1("MIchael Araujo!"),
        Gallery(),
        TodoList()
)
    
    
app = FastAPI()
configure(app, PagePrin)