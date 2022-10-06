import os, subprocess
from libqtile import hook
from settings.groups import groups
from settings.mouse import mouse

from settings.screens import screens
from settings.keys import keys, mod
from settings.layouts import layouts, layout_conf, floating_layout


@hook.subscribe.startup_complete
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])