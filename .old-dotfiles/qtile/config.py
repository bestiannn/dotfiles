from typing import List  # noqa: F401

from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy

from keys import keys
from screens import screens
from layouts import layouts, layout_conf, floating_layout

mod = "mod4"

groups = [Group(i) for i in ["B", "A", "w", "W", "2", "s"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen(toggle=True)),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

widget_defaults = dict(
    font='Mononoki Nerd Font',
    fontsize=17,
    padding=3,
)
extension_defaults = widget_defaults.copy()

mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating())
]