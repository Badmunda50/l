from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import io
from Badlogo.plugins.buttons import get_main_menu
from Badlogo.plugins.callbacks import handle_callback_query, send_edited_image
from Badlogo import app

users_data = {}


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Logo Maker Bot!\nPlease send me an image.")


@app.on_message(filters.photo)
async def handle_photo(client, message):
    photo = await message.download()
    with open(photo, "rb") as file:
        photo_bytes = file.read()

    users_data[message.chat.id] = {
        'photo': photo_bytes,
        'position': (10, 10),
        'font_size': 40,
        'color': 'black',
        'stroke_enabled': False,
        'stroke_width': 2,
        'stroke_color': 'black',
        'font_path': "Southam Demo.ttf",
        'bg_color': (255, 255, 255, 0),
        'bg_opacity': 1.0,
        'emboss_enabled': False,
        'third_text': {
            'text': '',
            'enabled': False,
            'color': 'black',
            'size': 40
        }
    }
    await message.reply_text("I got the image! Now send me the text you want to add to the image.")


@app.on_message(filters.text & ~filters.command("start"))
async def handle_text(client, message):
    chat_id = message.chat.id
    if chat_id in users_data and 'photo' in users_data[chat_id]:
        users_data[chat_id]['text'] = message.text
        await message.reply_text("Choose an option:", reply_markup=get_main_menu())
        await send_edited_image(client, chat_id)

