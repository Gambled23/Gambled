import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.components.project_card import project_card
from Gambled.variables import projects

def subtitle(
    text: str,
) -> rx.Component:
    return rx.heading(
        text, 
        as_="h3", 
        size="8",
        color=rx.color("mint", 12),
        align="left",
        padding_top="1em",
    ),

@rx.page(title="Portfolio")
def portfolio():
        return rx.flex(
        # rx.color_mode.button(position="top-right"),
        sidebar(),
        rx.vstack(
            rx.flex(
                rx.heading("Portfolio",
                        as_="h1",
                        size="9",
                        align="center",
                ),
            width="100%",
            direction="column",
            spacing="3",
            ),
            subtitle("Web developer"),
            rx.grid(
                project_card(project=projects["asanawave"]),
                project_card(project=projects["nisha"]),
                project_card(project=projects["dixios"]),
                project_card(project=projects["OnlineWeddingInvitation"]),
                project_card(project=projects["Gambled23"]),
                columns=rx.breakpoints(sm="1", md="3",),
                spacing="4",
                padding_x="1em",
                width="100%",
            ),

            subtitle("Personal projects"),
            rx.grid(
                project_card(project=projects["TheParkingZone"]),
                project_card(project=projects["nix-dotfiles"]),
                columns=rx.breakpoints(sm="1", md="3",),
                spacing="4",
                padding_x="1em",
                width="100%",
            ),

            rx.heading(
                "Discord bots",
                as_="h4", 
                size="6",
                color=rx.color("mint", 12),
                align="left",
            ),
            rx.grid(
                project_card(project=projects["eliasbot"]),
                project_card(project=projects["caphpibot"]),
                columns=rx.breakpoints(sm="1", md="3",),
                spacing="4",
                padding_x="1em",
                width="100%",
            ),
        width="100%",
        ),
    ),