import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.variables import *

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
