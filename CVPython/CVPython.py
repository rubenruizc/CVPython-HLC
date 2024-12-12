import reflex as rx
from CVPython.views.header.header import header 


class State (rx.State):
    pass

def index () -> rx.Component:
    return rx.vstack(
        header(),
        
    )

app = rx.App()
app.add_page(index)
app._compile()