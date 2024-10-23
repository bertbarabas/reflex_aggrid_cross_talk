import reflex as rx
from reflex_ag_grid import ag_grid


class State(rx.State):
    """The app state."""

    current_grid = "Grid1"
    message = ""

    def change_current_grid(self, new_grid: str):
        self.message = ""
        self.current_grid = new_grid

    def grid1_cell_clicked(self):
        self.message = "This should only print if a cell on Grid 1 was clicked!"

    def grid2_cell_clicked(self):
        self.message = "This should only print if a cell on Grid 2 was clicked!"


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Testcase for AgGrid Crosstalk", size="9"),
            rx.select(
                ["Grid1", "Grid2"],
                value=State.current_grid,
                on_change=State.change_current_grid,
            ),
            rx.match(
                State.current_grid,
                (
                    "Grid1",
                    rx.vstack(
                        rx.heading("Grid 1"),
                        ag_grid(
                            id="AgGrid1",
                            column_defs=[
                                ag_grid.column_def(field="Column 1"),
                                ag_grid.column_def(field="Column 2"),
                            ],
                            row_data=[
                                {"Column 1": "A1:1", "Column 2": "1:2"},
                                {"Column 1": "A2:1", "Column 2": "2:2"},
                                {"Column 1": "A3:1", "Column 2": "3:2"},
                            ],
                            on_cell_clicked=State.grid1_cell_clicked(),
                        ),
                    ),
                ),
                (
                    "Grid2",
                    rx.vstack(
                        rx.heading("Grid 2"),
                        ag_grid(
                            id="AgGrid2",
                            column_defs=[
                                ag_grid.column_def(field="Column 1"),
                                ag_grid.column_def(field="Column 2"),
                            ],
                            row_data=[
                                {"Column 1": "B1:1", "Column 2": "1:2"},
                                {"Column 1": "B2:1", "Column 2": "2:2"},
                                {"Column 1": "B3:1", "Column 2": "3:2"},
                            ],
                            # on_cell_clicked=State.grid2_cell_clicked(),
                        ),
                    ),
                ),
                rx.heading("This shouldn't happen"),
            ),
            rx.heading(f"message = {State.message}"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
