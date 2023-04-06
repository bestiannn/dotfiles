from libqtile import layout
from libqtile.config import Match
from .catppuccin import colors

# Select your color scheme of catppuccin
colors = colors["mocha"]

layout_conf = {
    "border_normal": colors["base"],
    "border_focus": colors["lavender"],
    "border_width": 4,
    "margin": 10
}

layout_conf_bsp = {
    "border_normal": colors["base"],
    "border_focus": colors["lavender"],
    "border_on_single": True,
    "border_width": 3,
    "margin": 5,
    "grow_amount": 5,
    "fair": False,
    "ratio": 1.3
}

layout_conf_max = {
    "border_normal": colors["base"],
    "border_focus": colors["lavender"],
    "border_width": 0,
    "margin": 10,
}

layouts = [
    layout.Bsp(**layout_conf_bsp),
    layout.Max(**layout_conf_max)
    #layout.MonadTall(**layout_conf),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='pavucontrol'),
    Match(wm_class='nitrogen'),
    Match(wm_class='lxappearance'),
    Match(wm_class='android-studio'),
    Match(wm_class='python2.7'),
    Match(wm_class='launcher-4'),
    Match(wm_class='stacer'),
    Match(wm_class='VirtualBox Manager'),
    Match(wm_class='VirtualBox Machine')
], **layout_conf)
