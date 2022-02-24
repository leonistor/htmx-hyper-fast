# pyright: reportWildcardImportFromLibrary=false
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from domonic import *


app = FastAPI()
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/contact/1/edit", response_class=HTMLResponse)
def edit_contact():
    return str(
        fieldset(
            div(
                label("First Name"),
                input(_type="text", value="Joe"),
                _class="grid",
            ),
            div(
                label("Last Name"),
                input(_type="text", value="Blow"),
                _class="grid",
            ),
            div(
                label("Email"),
                input(_type="email", value="joe@blow.me"),
                _class="grid",
            ),
            div(
                button(
                    "Submit",
                    **{
                        "_hx-put": "http://localhost:8000/contact/1",
                    },
                ),
                button(
                    "Cancel",
                    _class="secondary",
                    **{"_hx-get": "http://localhost:8000/contact/1"},
                ),
                _class="grid",
            ),
            **{
                "_hx-target": "this",
                "_hx-swap": "outerHTML",
            },
        ),
    )


@app.put("/contact/1", response_class=HTMLResponse)
def show_updated_contact():
    return str(
        fieldset(
            div(
                label("First Name"),
                p(strong("Joe")),
                _class="grid",
            ),
            div(
                label("Last Name"),
                p(strong("Blow")),
                _class="grid",
            ),
            div(
                label("Email"),
                p(strong("joe@blow.me")),
                _class="grid",
            ),
            button(
                "Click to edit",
                **{"_hx-get": "http://localhost:8000/contact/1/edit"},
            ),
            _class="test",
            **{
                "_hx-target": "this",
                "_hx-swap": "outerHTML",
            },
        ),
    )


@app.get("/contact/1", response_class=HTMLResponse)
def show_contact():
    return str(
        fieldset(
            div(
                label("First Name"),
                p(strong("Joe")),
                _class="grid",
            ),
            div(
                label("Last Name"),
                p(strong("Blow")),
                _class="grid",
            ),
            div(
                label("Email"),
                p(strong("joe@blow.me")),
                _class="grid",
            ),
            button(
                "Click to edit",
                **{"_hx-get": "http://localhost:8000/contact/1/edit"},
            ),
            _class="test",
            **{
                "_hx-target": "this",
                "_hx-swap": "outerHTML",
            },
        ),
    )
