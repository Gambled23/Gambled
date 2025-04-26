import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.components.project_card import project_card
from Gambled.variables import age, projects

@rx.page(title="Home")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        # rx.color_mode.button(position="top-right"),
        sidebar(),
        rx.vstack(
            rx.heading("Home", 
                        as_="h1", 
                        size="9",
                    ),
            rx.grid(
                rx.container(
                    rx.image(
                        src="/profile-picture.jpeg",
                        width="80%",
                        border_radius="5%",
                        margin_x="auto",
                        padding="0.5em",
                    ),
                    rx.flex(
                        rx.link(
                            rx.image(
                                src="/logos/github.png",
                                margin_x="auto",
                                height="100%",
                            ),
                            href="https://github.com/gambled23",
                            is_external=True,
                            height="80px",
                        ),
                        rx.link(
                            rx.image(
                                src="/logos/linkedin.webp",
                                height="100%",
                                margin_x="auto",
                            ),
                            href="https://www.linkedin.com/in/c%C3%A9sar-daniel-gonz%C3%A1lez-gir%C3%B3n-989793260/",
                            is_external=True,
                            height="80px",
                        ),
                        rx.link(
                            rx.image(
                                src="/logos/gmail.png",
                                height="100%",
                                margin_x="auto",
                            ),
                            href="mailto:ipog71@gmail.com",
                            is_external=True,
                            height="80px",
                        ),
                        justify_content="space-around",
                        margin_x="auto",
                    ),
                    size="2",
                    height="auto",
                ),
                rx.container(
                    rx.text(
                        f"I'm César González, a {age} years old student of the Degree in computer science at CUCEI (UdeG). I'm starting my last semester at college and graduating on 2025's summer.",
                        padding="1em",
                        text_align="justify",
                        font_size="1.3em",
                    ),
                    rx.text(
                        "I have experience in fullstack web development and server administration; I'm a big fan of selfhosting and DIY tech, so I try to build my own projects from design to deployment.",
                        padding="1em",
                        text_align="justify",
                        font_size="1.3em",
                    ),
                    size="2",
                ),
                columns=rx.breakpoints(sm="1", lg="2"),
                align="center",
                width="100%",
                padding="2em",
            ),
            rx.heading("Currently working on", 
                as_="h1", 
                size="9",
                align="center",
                padding_top="2em",
                color=rx.color("brown", 12),
            ),
            rx.grid(
                project_card(project=projects["asanawave"]),
                project_card(project=projects["nix-dotfiles"]),
                project_card(project=projects["dixios"]),
                columns=rx.breakpoints(sm="1", md="3",),
                spacing="4",
                padding="2em",
            ),
        align="center",
        width="100%",
        padding_top="4em",
        padding_right="2em",
        ),
    )
