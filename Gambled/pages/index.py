import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.components.project_card import project_card
from Gambled.variables import *

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
                project_card(
                    avatar="/asanawave/logo.svg",
                    title="Asanawave",
                    description_short="Webapp django app for a yoga teacher",
                    description_long="Currently I’m working with a three people team to develop and deploy a webapp for a private client, using Django as backend and HTMX to replace Javascript in the frontend.\nWe provide a space for a private teachers to upload lessons and manage all of their learning materials, while keeping close communication with their students.\nMy main responsibilities as a developer are integrating newly developed components to the system, write tests for existing components, and as a server administrator to provide a seamless integration on cloud.",
                    link="https://asanawave.com/",
                ),
                project_card(
                    avatar="/logos/nix.png",
                    title="Nix dotfiles",
                    description_short="My nix configuration for all my devices",
                    description_long="All of my devices run NixOS, so I decided to create a repository with all of my dotfiles and configuration files.\nI use this repository to keep track of all the changes I make to my system, and to share my configuration with others.\nFeel free to snoop around.",
                    repo="https://github.com/Gambled23/nix-dotfiles",
                ),
                project_card(
                    avatar="/logos/ia.svg",
                    title="Dixios",
                    description_short="AI and LLM Consultant at Dixios",
                    description_long="I'm currently working as a consultant for Dixios, a company that gives training to office employees on how to use AI tools to improve their productivity.\nMy main responsibilities are to create training materials, and to give training sessions to employees.\nI also help the company to integrate AI tools into their workflow, and to create custom solutions for their clients.",
                    link="https://dixios.com/",
                ),
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
