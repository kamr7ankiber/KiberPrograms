import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

from config import TOKEN

from menu import (
    main_menu,
    recon_menu,
    vuln_menu,
    security_menu,
    cms_menu
)

from modules.sqliaudit import sqliaudit
from modules.xss_audit import xss_audit
from modules.auth_check import auth_check
from modules.sensitive_files import sensitive_file_check
from modules.security_config import security_config_check
from modules.wordpress_check import wordpress_check


bot = Bot(token=TOKEN)
dp = Dispatcher()


waiting_tool = {}


@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "🛡 SECURITY TOOLKIT\n\nTool seç:",
        reply_markup=main_menu()
    )


@dp.callback_query()
async def menu_callback(callback):

    data = callback.data
    user = callback.from_user.id


    if data == "recon_menu":

        await callback.message.edit_text(
            "🔎 Recon Tools",
            reply_markup=recon_menu()
        )


    elif data == "vuln_menu":

        await callback.message.edit_text(
            "💉 Vulnerability Audit",
            reply_markup=vuln_menu()
        )


    elif data == "security_menu":

        await callback.message.edit_text(
            "🛡 Security Checks",
            reply_markup=security_menu()
        )


    elif data == "cms_menu":

        await callback.message.edit_text(
            "📋 CMS Tools",
            reply_markup=cms_menu()
        )


    elif data == "tool_sqli":

        waiting_tool[user] = "sqli"

        await callback.message.answer(
            "💉 SQLi Audit\n\nURL göndərin:"
        )


    elif data == "tool_xss":

        waiting_tool[user] = "xss"

        await callback.message.answer(
            "⚔️ XSS Audit\n\nURL göndərin:"
        )


    elif data == "tool_auth":

        waiting_tool[user] = "auth"

        await callback.message.answer(
            "🔐 Auth Check\n\nURL göndərin:"
        )


    elif data == "tool_files":

        waiting_tool[user] = "files"

        await callback.message.answer(
            "📂 Sensitive Files\n\nDomain göndərin:"
        )


    elif data == "tool_security":

        waiting_tool[user] = "security"

        await callback.message.answer(
            "🛡 Security Config\n\nURL göndərin:"
        )


    elif data == "tool_wp":

        waiting_tool[user] = "wp"

        await callback.message.answer(
            "📋 WordPress Check\n\nDomain göndərin:"
        )


    elif data == "back_main":

        await callback.message.edit_text(
            "🛡 SECURITY TOOLKIT",
            reply_markup=main_menu()
        )


    await callback.answer()



@dp.message()
async def tool_runner(message: Message):

    user = message.from_user.id

    if user not in waiting_tool:
        return


    tool = waiting_tool[user]

    target = message.text.strip()


    try:

        if tool == "sqli":

            result = sqliaudit(target)


        elif tool == "xss":

            result = xss_audit(target)


        elif tool == "auth":

            result = auth_check(target)


        elif tool == "files":

            result = sensitive_file_check(target)


        elif tool == "security":

            result = security_config_check(target)


        elif tool == "wp":

            result = wordpress_check(target)


        else:

            result = "Tool tapılmadı"


        await message.answer(
            str(result)
        )


    except Exception as e:

        await message.answer(
            f"Xəta: {e}"
        )


    del waiting_tool[user]



async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
