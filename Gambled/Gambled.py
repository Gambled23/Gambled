"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    age: int = 21
    ...

style = {
    "background": "#0E1511",
    "height": "100vh",
    "width": "100vw",
    "margin": "0px",
}


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
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                # height="100%",
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


def project_card(
          avatar: str,
          title: str,
          description_short: str,
          description_long: str,
          link: str = None,
          repo: str = None,

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
            size="3",
            as_child=True,
            ),
        ),
    ),
    rx.dialog.content(
        rx.dialog.title(title),
        rx.dialog.description(description_long, 
                              white_space="pre-wrap",
                              font_size="1.1em",
                              text_align="justify",
                            ),
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
                        f"I'm César González, a {State.age} years old student of the Degree in computer science at CUCEI (UdeG). I'm starting my last semester at college and graduating on 2025's summer.",
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
                    description_long="Currently I’m working with a three people team to develop and deploy a webapp for a private client, using Django as backend and HTMX to replace Javascript in the frontend.\nWe provide a space for a private teachers to upload lessons and manage all of their learning materials, while keeping close communication with their students.\nMy main responsibilities as a developer are integrating newly developed components to the system, write tests for existing components, and managing nginx server for provide a seamless integration on cloud.",
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

@rx.page(title="Bio")
def bio():
    return rx.flex(
        # rx.color_mode.button(position="top-right"),
        sidebar(),
        rx.vstack(
            rx.heading("Bio", 
                        as_="h1", 
                        size="9",
                    ),
            rx.container(
                rx.text(
                    f"I'm César González, a {State.age} years old student at Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI UDG), born in México, living in Guadalajara, Jalisco.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "Since I was a child I was curious about computers, and my passion just grew when I got my first computer and started to explore its insides and outsides.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "I started programming by accident. When I was 13 years old using tasker, without knowing that I was learning the basics of problem solving, just trying to automate my life.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "Shortly after that, I learned that you could do the same thing I was doing with tasker in my phone, writing code in a computer, so I started to watch online courses about coding and started to learn java.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "I became really frustrated, so I dropped learning to code for a while and started to focus more on another things I liked, like editing videos.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "It was until 2021 when I decided to study computer science that I gave coding another chance, and with the right focus I got hold of the basics of C and C++, which helped me to learn by myself things that really interested me, like web development, bash scripting and I even developed a discord bot.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "When I started taking classes like network administration, and server configuration, I discovered another passion of mine, I was very surprised to see behind the scenes, and how a webpage is not just some HTML that you can magically access via internet.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "I continued my fullstack adventure by doing some services for the ITRANS department of CUCEI in 2024, where I learned a lot about web development in a professional environment, but more importantly, I learned how to work in a team and the AGILE methodology, because until that moment I was used to code alone.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "During this time I developed a couple of personal projects, and became Lead Developer of Asanawave, a web platform for a private client, a yoga teacher, who wanted to upload their video classes behind a paywall and manage their business.",
                    padding_bottom="1em",
                    text_align="justify",
                    font_size="1.2em",
                ),
                rx.text(
                    "If youre interested in kwnowing more about my projects, feel free to ",
                    rx.link(
                        "check out my portfolio.",
                    ),
                    text_align="justify",
                    font_size="1.3em",
                ),

            ),
            align="center",
            width="100%",
            padding_top="4em",
            padding_right="2em",
        ),
    )

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

@rx.page(title="Links")
def links():
        return rx.flex(
        # rx.color_mode.button(position="top-right"),
        sidebar(),
        rx.vstack(
            rx.heading("Bio", 
                        as_="h1", 
                        size="9",
                    ),
            rx.container(
                rx.heading(
                    "Contact",
                    text_align="left",
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link(
                            "Email",
                            href="mailto:ipog71@gmail.com",
                            is_external=True,
                        )
                    ),
                    rx.list.item(
                        rx.link(
                            "Telegram",
                            href="https://t.me/Gambled23",
                            is_external=True,
                        )
                    ),
                    padding_bottom="2em",
                ),

                rx.heading(
                    "Social",
                    text_align="left",
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link(
                            "Mastodon",
                            href="https://mastodon.social/@Gambled23",
                            is_external=True,
                        )
                    ),
                    rx.list.item(
                        rx.link(
                            "Discord",
                            href="https://discord.com/users/320649011000246272",
                            is_external=True,
                        )
                    ),
                    padding_bottom="2em",
                ),

                rx.heading(
                    "Media logging",
                    text_align="left",
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link(
                            "Books",
                            href="https://www.goodreads.com/user/show/113163810-c-sar-daniel-gonz-lez",
                            is_external=True,
                        )
                    ),
                    rx.list.item(
                        rx.link(
                            "Movies",
                            href="https://www.imdb.com/user/ur102644810/ratings?ref_=nv_usr_rt_4",
                            is_external=True,
                        )
                    ),
                    rx.list.item(
                        rx.link(
                            "Anime",
                            href="https://anilist.co/user/Gambled23/",
                            is_external=True,
                        )
                    ),
                    padding_bottom="2em",
                ),
                width="100%",
            ),
            align="center",
            width="100%",
            padding_top="4em",
            padding_right="2em",
        ),
    )

app = rx.App(
    theme=rx.theme(accent_color="grass"),
    style=style,
)
app.add_page(index)
