import reflex as rx

def hstack(texto, icon) -> rx.Component:
    return rx.hstack(
        rx.icon(icon,size= 15, color = "white"),
        rx.text(texto, font_size="15px",font_weight="bold",color = "white"),
        align="center"
    )