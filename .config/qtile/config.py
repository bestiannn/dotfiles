import os
import subprocess
from libqtile import hook, qtile

from settings.groups import groups
from settings.mouse import mouse
from settings.screens import screens
from settings.keys import keys, mod
from settings.layouts import layouts, layout_conf, floating_layout


@hook.subscribe.startup_complete
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
    # Force the first group to be on the first screen and the second group to be on the second screen
    qtile.groups_map["1"].cmd_toscreen(0, toggle=False)
    try:
        qtile.groups_map["6"].cmd_toscreen(1, toggle=False)
    except:
        pass
