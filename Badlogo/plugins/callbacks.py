from pyrogram import Client
from Badlogo import app
from Badlogo.plugins.buttons import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import io

# Add Opacity Buttons
@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id

    if chat_id in users_data:
        if data.startswith('color_'):
            users_data[chat_id]['color'] = data.split('_')[1]
            await callback_query.answer(f"Text color set to {users_data[chat_id]['color']}!", show_alert=True)

        elif data == 'opacity_options':
            await callback_query.message.reply_text(
                "Adjust Opacity:",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("-", callback_data='decrease_opacity')],
                        [InlineKeyboardButton("+", callback_data='increase_opacity')]
                    ]
                )
            )
            await callback_query.answer()

        elif data == 'increase_opacity':
            if users_data[chat_id]['bg_opacity'] < 1.0:
                users_data[chat_id]['bg_opacity'] += 0.1
                await callback_query.answer(f"Opacity increased to {users_data[chat_id]['bg_opacity'] * 100}%", show_alert=True)
            else:
                await callback_query.answer("Opacity is already at maximum!", show_alert=True)

        elif data == 'decrease_opacity':
            if users_data[chat_id]['bg_opacity'] > 0.1:
                users_data[chat_id]['bg_opacity'] -= 0.1
                await callback_query.answer(f"Opacity decreased to {users_data[chat_id]['bg_opacity'] * 100}%", show_alert=True)
            else:
                await callback_query.answer("Opacity is already at minimum!", show_alert=True)

        elif data == 'font_options':
            await callback_query.message.reply_text(
                "Select Font:",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Font 1", callback_data='font_1')],
                        [InlineKeyboardButton("Font 2", callback_data='font_2')],
                        [InlineKeyboardButton("Font 3", callback_data='font_3')],
                        [InlineKeyboardButton("Font 4", callback_data='font_4')],
                        [InlineKeyboardButton("Font 5", callback_data='font_5')],
                        [InlineKeyboardButton("Font 6", callback_data='font_6')],
                        [InlineKeyboardButton("Font 7", callback_data='font_7')],
                        [InlineKeyboardButton("Font 8", callback_data='font_8')],
                        [InlineKeyboardButton("Font 9", callback_data='font_9')],
                        [InlineKeyboardButton("Font 10", callback_data='font_10')]
                    ]
                )
            )
            await callback_query.answer()

        elif data.startswith('font_'):
            font_number = int(data.split('_')[1])
            font_paths = [
                "path/to/font1.ttf",
                "path/to/font2.ttf",
                "path/to/font3.ttf",
                "path/to/font4.ttf",
                "path/to/font5.ttf",
                "path/to/font6.ttf",
                "path/to/font7.ttf",
                "path/to/font8.ttf",
                "path/to/font9.ttf",
                "path/to/font10.ttf"
            ]
            users_data[chat_id]['font_path'] = font_paths[font_number - 1]
            await callback_query.answer(f"Font set to Font {font_number}!", show_alert=True)

        # Add other callback handlers as per the original code


async def send_edited_image(client, chat_id):
    user_data = users_data[chat_id]
    photo_data = user_data['photo']
    text = user_data.get('text', '')
    position = user_data.get('position', (10, 10))
    color = user_data.get('color', 'black')
    font_path = user_data.get('font_path', "Southam Demo.ttf")
    stroke_color = user_data.get('stroke_color', 'black')
    stroke_width = user_data.get('stroke_width', 2)
    stroke_enabled = user_data.get('stroke_enabled', False)
    font_size = user_data.get('font_size', 40)
    shadow_enabled = user_data.get('shadow_enabled', False)
    inner_shadow_enabled = user_data.get('inner_shadow_enabled', False)
    shadow_color = user_data.get('shadow_color', 'gray')
    shadow_offset = user_data.get('shadow_offset', (5, 5))
    shadow_size = user_data.get('shadow_size', 3)

    image = Image.open(io.BytesIO(photo_data))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Apply shadow
    if shadow_enabled:
        shadow_position = (position[0] + shadow_offset[0], position[1] + shadow_offset[1])
        for x in range(-shadow_size, shadow_size + 1):
            for y in range(-shadow_size, shadow_size + 1):
                draw.text((shadow_position[0] + x, shadow_position[1] + y), text, fill=shadow_color, font=font)

    # Apply inner shadow
    if inner_shadow_enabled:
        for x in range(-shadow_size, shadow_size + 1):
            for y in range(-shadow_size, shadow_size + 1):
                draw.text((position[0] - x, position[1] - y), text, fill=shadow_color, font=font)

    # Apply text with stroke or normal text
    if stroke_enabled:
        draw.text(position, text, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke_color)
    else:
        draw.text(position, text, fill=color, font=font)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    await client.send_photo(chat_id, img_byte_arr, caption="Here is your edited logo!")
