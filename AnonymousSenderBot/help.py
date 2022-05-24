import random
from pyrogram import Client, filters


STICKERS = ["CAACAgUAAx0CQOmOBQACD0dijJcEET4nLf5e5Nw5hCUBcKwAASQAAgMCAAJx5PFWae33aIYNtbweBA", "CAACAgUAAx0CQOmOBQACD0ZijJb37in18z0QPAxbLCGJ5srtBQACawIAAhCt2FZVN0_rNZ_zPh4E"]


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	STICKER = random.choice(STICKERS)
	await msg.reply_sticker(STICKER)
