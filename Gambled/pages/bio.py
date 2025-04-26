import reflex as rx
from Gambled.components.sidebar import sidebar
from Gambled.variables import age

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
                    f"I'm César González, a {age} years old student at Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI UDG), born in México, living in Guadalajara, Jalisco.",
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
