#! /usr/bin/env python

import itfoundrykit as kit
kit.confirm_version('2.1.1')

# - - -

family = kit.Family(
    client    = 'Google Fonts',
    trademark = 'Hind',
    script    = 'Bangla',
)

family.set_masters(
    modules = [
        # 'kerning',
        'mark_positioning',
        'mark_to_mark_positioning',
    ],
)

family.set_styles()

# - - -

builder = kit.Builder(family)

builder.fontrevision = '0.100'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

builder.build()
