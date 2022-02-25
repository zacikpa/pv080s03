import ipywidgets as widgets
from ipywidgets import interact, Layout

# define controllers for each byte
first = widgets.IntSlider(description="1st", min=0, max=255, readout_format="")
first_text = widgets.BoundedIntText(
    description="1st", min=0, max=255, layout=Layout(width="100%")
)
widgets.jslink((first, "value"), (first_text, "value"))

second = widgets.IntSlider(description="2nd", min=0, max=255)
second_text = widgets.BoundedIntText(
    description="2nd", min=0, max=255, layout=Layout(width="100%")
)
l = widgets.jslink((second, "value"), (second_text, "value"))

third = widgets.IntSlider(description="3rd", min=0, max=255)
third_text = widgets.BoundedIntText(
    description="3rd", min=0, max=255, layout=Layout(width="100%")
)
l = widgets.jslink((third, "value"), (third_text, "value"))

fourth = widgets.IntSlider(description="4th", min=0, max=255)
fourth_text = widgets.BoundedIntText(
    description="4th", min=0, max=255, layout=Layout(width="100%")
)
l = widgets.jslink((fourth, "value"), (fourth_text, "value"))

byte_ui = widgets.GridBox(
    [
        first_text,
        second_text,
        third_text,
        fourth_text,
        first,
        second,
        third,
        fourth,
    ],
    layout=widgets.Layout(grid_template_columns="repeat(4, 23%)"),
)
