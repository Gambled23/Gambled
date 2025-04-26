import reflex as rx
from typing import Optional, Dict, Any

def project_card(
        project: Optional[Dict[str, Any]] = None,
        size: str = "3",

) -> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(
        rx.card(
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
    ),
    rx.dialog.content(
        rx.dialog.title(project["title"]),
        rx.dialog.description(
            project["description_long"], 
            white_space="pre-wrap",
            font_size="1.1em",
            text_align="justify",
        ),
        rx.cond(
            project["body_image"],
            rx.image(
                src=project["body_image"],
                width="100%",
                height="auto",
                border_radius="20px",
                padding="0.5em",
                margin_x="auto",
            ),
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
