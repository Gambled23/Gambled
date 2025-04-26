import reflex as rx

class ImageState(rx.State):
    images = [
        "/logos/github.png",
        "/logos/gmail.png",
        "/logos/nix.png",
    ]
    current_index: int = 0

    @rx.event
    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images)

def project_card(
          avatar: str,
          title: str,
          description_short: str,
          description_long: str,
          link: str = None,
          repo: str = None,
          size: str = "3",

) -> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(
        rx.card(
            rx.link(
            rx.flex(
                rx.avatar(src=avatar),
                rx.box(
                    rx.heading(title),
                    rx.text(description_short,),
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
        rx.dialog.title(title),
        rx.dialog.description(
            description_long, 
            white_space="pre-wrap",
            font_size="1.1em",
            text_align="justify",
        ),
        rx.image(
            src=ImageState.images[ImageState.current_index]
        ),
        rx.moment(interval=3000, on_change=ImageState.next_image, display="none"),
        rx.hstack(
            rx.cond(
                link,
                rx.link(
                    rx.button(
                        rx.icon("square-arrow-out-up-right"),
                        "Link",
                    ),
                    href=link,
                    is_external=True,
                    color_scheme="green",
                    variant="solid",
                ),
            ),
            rx.cond(
                repo,
                rx.link(
                    rx.button(
                        rx.icon("github"),
                        "Repository",
                    ),
                    color="white",
                    color_scheme="blue",
                    variant="solid",
                    href=repo,
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
