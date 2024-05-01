
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
        return html.li(name, " ✔" if done else "")


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
def ListaDeDato(items):
    list_item_elements = [html.li(text) for text in items]
    return html.ul(list_item_elements)


@component
def TodoListq():
    tasks = [
        "Make breakfast (important)",
        "Feed the dog (important)",
        "Do laundry",
        "Go on a run (important)",
        "Clean the house",
        "Go to the grocery store",
        "Do some coding",
        "Read a book (important)",
    ]
    return html.section(
        html.h1("My Todo List"),
        ListaDeDato(tasks),
    )

@component
def ListaDatos():
    personas = [
        "Michael Araujo",
        "Sammy Sanchez",
        "Isabel",
        "Sileidy",
        "Yasel",
        "Candy",
        "Jesus",
        "Espiritu Santo",
    ]
    return html.section(
        html.h1("Lista de Personas"),
        ListaDeDato(personas),
    )

@component
def PagePrin():
    return html.div(
        html.h1("MIchael Araujo!"),
        Gallery(),
        TodoList(),
        TodoListq(),
        ListaDatos()
)
    
    
app = FastAPI()
configure(app, PagePrin)