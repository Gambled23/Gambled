import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str, is_external: bool = False
) -> rx.Component:
    return rx.link(
            rx.hstack(
                rx.icon(icon),
                rx.text(text, size="4"),
                width="100%",
                padding_x="0.5rem",
                padding_y="0.75rem",
                align="center",
                style={
                    "_hover": {
                        "bg": rx.color("accent", 4),
                        "color": rx.color("accent", 11),
                    },
                    "border-radius": "0.5em",
                },
            ),
            href=href,
            is_external=is_external,
            underline="none",
            weight="medium",
            width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "slash", "/"),
        sidebar_item("Bio", "book-text", "/bio"),
        sidebar_item("Portfolio", "folder-kanban", "/portfolio"),
        sidebar_item("Links", "link", "/links"),
        sidebar_item("Resumé", "file-user", "/Resume.pdf", True),
        spacing="1",
        width="100%",
    )

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="100%",
                        height="auto",
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="100vh",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )