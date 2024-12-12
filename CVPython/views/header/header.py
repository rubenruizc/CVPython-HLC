import reflex as rx

def header() -> rx.Component:
    imagen = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie4oBT8e-x76ieAfVp-qKQ1e8T0C6uLjrUC94OWDCyYXswugGlx1Rxxh3kX8drtS_ekPbrGaZR0C1gyBMlD-3KkD2kuLyhk2JXIVTjndjABBlln-g8FOfXB_N7EakBzsUDXc9AvzUW2xo/s1902/yo+furbo.jpeg"
    return rx.vstack(
        rx.hstack(
            rx.image(src=imagen, width="150px", height="150px", border_radius="50%",margin = "20px"),
            
            rx.vstack(
                rx.text("Ruben Ruiz Castaño", font_size="50px",font_weight="bold",color = "white"),
                rx.hstack(
                rx.text("Nacionalidad: Española", font_size="15px",font_weight="bold",color = "white"),
                rx.text(" Fecha de nacimiento: 15/04/2005", font_size="15px",font_weight="bold",color = "white"),
                rx.text("Género: Masculino ", font_size="15px",font_weight="bold",color = "white"),
                align="center"
                )
        ),
            
            align="center"
        ),
        
        
        align="center",
        bg = "#2E5077",
        width="100%",
        padding_x = "16px",
        padding_y = "16px",
    )