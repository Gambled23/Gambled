import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.variables import *

@rx.page(title="Portfolio")
def portfolio():
        return rx.flex(
        # rx.color_mode.button(position="top-right"),
        sidebar(),
        rx.vstack(
            rx.heading("Portfolio", 
                        as_="h1", 
                        size="9",
                    ),
            align="center",
            width="100%",
            padding_top="4em",
            padding_right="2em",
        ),
    ),