from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Badlogo.plugins.callbacks import *

def get_main_menu():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Opacity", callback_data='opacity')],
            [InlineKeyboardButton("Font Options", callback_data='font_options')],
            [InlineKeyboardButton("Color Options", callback_data='color_options')],
            [InlineKeyboardButton("Stroke Options", callback_data='stroke_options')],
            [InlineKeyboardButton("Shadow Options", callback_data='shadow_options')],
            [InlineKeyboardButton("Inner Shadow Options", callback_data='inner_shadow_options')],
            [InlineKeyboardButton("Background Options", callback_data='background_options')],
            [InlineKeyboardButton("Emboss Options", callback_data='emboss_options')],
            [
                InlineKeyboardButton("⬆️", callback_data='move_up'),
                InlineKeyboardButton("⬅️", callback_data='move_left'),
                InlineKeyboardButton("➡️", callback_data='move_right'),
                InlineKeyboardButton("⬇️", callback_data='move_down')
            ],
            [
                InlineKeyboardButton("⬆️ Fast Up", callback_data='fast_up'),
                InlineKeyboardButton("⬅️ Fast Left", callback_data='fast_left'),
                InlineKeyboardButton("➡️ Fast Right", callback_data='fast_right'),
                InlineKeyboardButton("⬇️ Fast Down", callback_data='fast_down')
            ],
            [
                InlineKeyboardButton("Increase Size 2×", callback_data='increase_font_2x'), 
                InlineKeyboardButton("Decrease Size 2×", callback_data='decrease_font_2x')
            ],
            [
                InlineKeyboardButton("Increase Size 4×", callback_data='increase_font_4x'), 
                InlineKeyboardButton("Decrease Size 4×", callback_data='decrease_font_4x')
            ],
            [InlineKeyboardButton("3rd Text Options", callback_data='third_text_options')]
        ]
    )

# Add functions to generate other specific menus if needed.
