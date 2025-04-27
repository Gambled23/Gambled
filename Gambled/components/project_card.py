import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
from typing import Optional, Dict, Any
import random

class IterState(rx.State):
    color: list[str] = [
        "red",
        "green",
        "blue",
    ]

def colored_box(color: str):
    return rx.button(color, background_color=color)

def project_card(
        project: Optional[Dict[str, Any]] = None,
        size: str = "3",
) -> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(
        rx.card(
            rx.hover_card.root(
            rx.hover_card.trigger(
                rx.link(
                    rx.flex(
                        rx.avatar(src=project["avatar"]),
                        rx.box(
                            rx.heading(project["title"],),
                            rx.text(project["description_short"],),
                        ),
                        height="100%",
                        align="center",
                        spacing="4",
                    ),
                    height="100%",
                    size=size,
                    as_child=True,
                ),
            ),
            hover_card(project),
        ),
    ),
    ),
    rx.dialog.content(
        rx.dialog.title(project["title"]),
        rx.dialog.description(
            project["description_long"], 
            white_space="pre-wrap",
            font_size="1.1em",
            text_align="justify",
            padding_bottom="0.5em",
        ),
        rx.cond(
            project["body_image"],
            rx.image(
                src=project["body_image"],
                width="100%",
                height="auto",
                border_radius="20px",
                padding_bottom="0.5em",
                margin_x="auto",
            ),
        ), 
        rx.hstack(
            rx.foreach(project["technologies"], status_chip),
            wrap="wrap",
            spacing="2",
            padding_bottom="2em",
        ),
        rx.hstack(
            rx.cond(
                project["link"],
                rx.link(
                    rx.button(
                        rx.icon("square-arrow-out-up-right"),
                        "Link",
                    ),
                    href=project["link"],
                    is_external=True,
                    color_scheme="green",
                    variant="solid",
                ),
            ),
            rx.cond(
                project["repo"],
                rx.link(
                    rx.button(
                        rx.icon("github"),
                        "Repository",
                    ),
                    color="white",
                    color_scheme="blue",
                    variant="solid",
                    href=project["repo"],
                    is_external=True,
                ),
            ),
            rx.dialog.close(
                rx.button(
                    "Close",
                    color_scheme="gray",
                    variant="soft",
                ),    
            ),
            width="100%",
            height="100%",
            spacing="4",
            justify="end",
            align="center",
        ),
    ),
)


status_chip_props = {
    "radius": "full",
    "variant": "outline",
    "size": "3",
}


color_schemes = ["indigo", "cyan", "orange", "crimson", "tomato", "red", "grass", "gray"]
def status_chip(
    name: str,
) -> rx.Component:
    return rx.badge(
        name,
        color_scheme=random.choice(color_schemes),
        **status_chip_props,
    )

def hover_card(
        project: Optional[Dict[str, Any]] = None,
    ) -> rx.Component:
    return rx.hover_card.content(
            rx.flex(
                rx.cond(
                    project["thumbnail"],                
                    rx.image(
                        src=project["thumbnail"],
                        width="100%",
                        height="auto",
                        border_radius="10px",
                    ),
                ), 

                rx.hstack(
                    rx.foreach(project["technologies"], status_chip),
                    spacing="2",
                    justify="center",
                    wrap="wrap",
                ),
            ),
        ),