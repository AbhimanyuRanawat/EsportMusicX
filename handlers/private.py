
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
ššš„š„šØ š šš¦š„š¶ šš®ššš§ š šš„š¢š¬š”šš§āāļø \nšš®š©šš«ššš¬š­ š„ šš šš®š¬š¢š š« šš„šš²šš« š ššØš­ ššØš« \nššš„šš š«šš¦ ā¤ļø šš®š§ šš§ š§ šš«š¢šÆšš­š š šš©š¬ ššš«šÆšš« \nā­šššÆšš„šØš©šš šš² [Ł­š°ššššššš¢š ššššš ššššš ššŁ­](https://t.me/Itz_Venom_xD)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā°š¢šš»š²šæš¤“ā±", url="https://t.me/Itz_Venom_xD")
                  ],[
                    InlineKeyboardButton(
                        "ā°š¦šš½š½š¼šæššā±", url="https://t.me/AlishaSupport"
                    ),
                    InlineKeyboardButton(
                        "ā°ššæš¼šš½š©ā±", url="https://t.me/Shayri_Music_Lovers"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ā°šš”šš­ šš«šØš®š©š„ā±", url="https://t.me/LoL_Offical_TuM_BiN"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Qį“į“į“É“ š į“ŹÉŖź±Źį“š„ šš§š„š¢š§š\nš @Itz_VeNom_xD š„**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¦šš½š½š¼šæšā¤ļø", url="https://t.me/AlishaSupport")
                ]
            ]
        )
   )
