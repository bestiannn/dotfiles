from libqtile import layout
from libqtile.config import Match
from colors import colors


layout_conf = {
    "border_normal": colors["black"],
    "border_focus": colors["purple"],
    "border_width": 5,
    "margin": 15
}

layout_conf_bsp = {
    "border_normal": colors["black"],
    "border_focus": colors["purple"],
    "border_width": 5,
    "margin": 10,
    "grow_amount": 5,
    "fair": False,
    "ratio": 1.3
}

layouts = [
    layout.Bsp(**layout_conf_bsp),
    layout.MonadTall(**layout_conf)
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    *layout.Floating.default_float_rules,
    # *layout_conf_floating,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='pavucontrol'),
    Match(wm_class='nitrogen'),
    Match(wm_class='lxappearance'),
    Match(wm_class='android-studio'),
    Match(wm_class='python2.7'),
    Match(wm_class='launcher-4'),
], **layout_conf)
