from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from .catppuccin import colors

# Select your color scheme of catppuccin
colors = colors["mocha"]

screens = [
    Screen(bottom=bar.Bar(
        [
            # Left side
            widget.GroupBox(background=colors["lavender"],
                            other_screen_border=colors["lavender"],
                            other_current_screen_border=colors["lavender"],
                            this_screen_border=colors["lavender"],
                            this_current_screen_border=colors["lavender"],
                            active=colors["overlay1"],
                            inactive=colors["text"],
                            block_highlight_text_color=colors["mantle"],
                            fontsize=15,
                            padding_x=15,
                            use_mouse_wheel=False,
                            font='Roboto Mono',
                            disable_drag=True
                            ),
            widget.TextBox(text="",
                           fontsize=35,
                           foreground=colors["lavender"],
                           background=colors["surface0"],
                           padding=0,
                           ),
            widget.Spacer(length=20),
            widget.WindowName(foreground=colors["text"],
                              fontsize=18,
                              font="Cascadia Code",
                              ),
            widget.Spacer(length=20),

            # Right side
            widget.TextBox(text="",
                           fontsize=35,
                           foreground=colors["surface1"],
                           background=colors["base"],
                           padding=0
                           ),
            widget.Systray(padding=15,
                           icon_size=25,
                           background=colors["surface1"],
                           ),
            widget.Spacer(length=25, background=colors["surface1"]),

            widget.TextBox(text="",
                           fontsize=35,
                           foreground=colors["surface0"],
                           background=colors["surface1"],
                           padding=0
                           ),
            widget.Battery(background=colors["surface0"],
                           foreground=colors["text"],
                           font="Cascadia Code",
                           fontsize=20,
                           format="  {percent:2.0%} ",
                           show_short_text=False,
                           low_percentage=0.2,
                           low_foreground = colors["red"],
                           ),
            widget.PulseVolume(background=colors["surface0"],
                               foreground=colors["text"],
                               font="Cascadia Code",
                               fontsize=20,
                               fmt="󰕾 {} ",
                               mouse_callbacks={
                                   'Button3': lazy.spawn('pavucontrol -t 4')}
                               ),

            widget.TextBox(text="",
                           fontsize=35,
                           foreground=colors["mantle"],
                           background=colors["surface0"],
                           padding=0
                           ),
            widget.Clock(background=colors["mantle"],
                         foreground=colors["text"],
                         format=" %d/%m/%Y  %H:%M ",
                         font="Cascadia Code",
                         fontsize=20,
                         padding=10
                         ),
        ], size=35, background=colors["base"]),
    )
]
