"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Gambled.components.sidebar import sidebar
from .pages import *


class State(rx.State):
    """The app state."""
    ...


# style = {
#     "background": "#0E1511",
#     "height": "100vh",
#     "width": "100vw",
#     "margin": "0px",
# }

app = rx.App(
    theme=rx.theme(accent_color="grass"),
    # style=style,
)
