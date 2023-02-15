# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    count: int = 0

    def pressed(self):
        self.count += 1


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Hello Pycone!", font_size="2em"),
            pc.box("The button below has been clicked ", State.count, " times."),
            pc.button(
                "Click me!",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                on_click=State.pressed,
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
