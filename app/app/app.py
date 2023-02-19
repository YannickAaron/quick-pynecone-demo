# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

from datetime import datetime

import pynecone as pc


class Message(pc.Model, table=True):
    username: str
    message: str
    timestamp: str


class State(pc.State):
    count: int = 0

    username: str = ""
    message: str = ""
    timestamp: str = ""

    messages: list[Message] = []

    def pressed(self):
        self.count += 1

    def add_message(self):
        if self.username != "" or self.message != "":
            self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            with pc.session() as session:
                session.add(Message(username=self.username, message=self.message, timestamp=self.timestamp))
                session.commit()
        self.get_messages()

    def get_messages(self):
        with pc.session() as session:
            self.messages = session.query(Message).all()


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
            pc.button(
                "Get messages",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                on_click=State.get_messages,
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            pc.vstack(
                pc.input(
                    # Setting the initial value of the input.
                    placeholder="Username",
                    on_blur=State.set_username,
                    border="0.1em solid",
                    padding="0.5em",
                    border_radius="0.5em",
                ),
                pc.input(
                    placeholder="Message",
                    on_blur=State.set_message,
                    border="0.1em solid",
                    padding="0.5em",
                    border_radius="0.5em",
                ),
                pc.button(
                    "Add message",
                    border="0.1em solid",
                    padding="0.5em",
                    border_radius="0.5em",
                    on_click=State.add_message,
                    _hover={
                        "color": "rgb(107,99,246)",
                    },
                ),
            ),
            pc.foreach(
                State.messages,
                lambda message: pc.vstack(
                    pc.text(message.username, font_size="1.5em"),
                    pc.text(message.message, font_size="1.5em"),
                    pc.text(message.timestamp, font_size="1.5em"),
                ),
            ),
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
