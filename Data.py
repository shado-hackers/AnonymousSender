from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag. \n\nBy @shado_hackers ♥"

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @shado_hackers

Follow meh : [Click Here](https://mobile.twitter.com/Shado_hackers)

Support : [OMG INFO](https://t.me/OMG_info)

LEECH group : [don't touch](https://t.me/nexleech)

Developer : @shado_hackers
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("❗Remove Caption ❕", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 📂", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About The Bot 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ deploy bot ♥", url="https://deployheroku.vercel.app/")],
        [InlineKeyboardButton("❄️Support Group ☀️", url="https://t.me/OMG_info")],
    ]
