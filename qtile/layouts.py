from libqtile import layout
from libqtile.config import Match
from colors import colors


layout_conf = {
    "border_normal": colors["black"],
    "border_focus": colors["blue"],
    "border_width": 5,
    "margin": 15
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    # *layout_conf_floating,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='pavucontrol'),
    Match(wm_class='nitrogen'),
    Match(wm_class='lxappearance'),
    Match(wm_class='android-studio'),
], **layout_conf)