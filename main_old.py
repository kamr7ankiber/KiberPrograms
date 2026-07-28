import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import TOKEN
from modules.ip_info import get_ip_info
from modules.dns_check import check_dns
from modules.headers import get_headers
from modules.url_check import check_url
from modules.ssl_check import check_ssl
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from modules.recon import recon_domain
from modules.report import generate_report
from modules.cve_lookup import cve_lookup
from modules.virustotal import vt_lookup
from modules.nmap_scan import nmap_scan
from modules.xss_audit import xss_audit
from modules.url_analyzer import analyze_url
from modules.file_check import file_check
from modules.cors_check import cors_check
from modules.cookie_check import cookie_check
from modules.wordpress_check import wordpress_check
from modules.wp_cve import wp_cve_lookup
from modules.sqli_audit import sqli_audit
from modules.sqli_form import sqli_form_audit
from modules.sqliaudit import sqliaudit
from modules.auth_check import auth_check
from modules.sensitive_files import sensitive_file_check
from modules.security_config import security_config_check
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

class SSLState(StatesGroup):
    waiting_domain = State()

def old_main_menu():
   def recon_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Full Recon",
                    callback_data="tool_recon"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 Subdomain Discovery",
                    callback_data="tool_subdomain"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Geri",
                    callback_data="back_main"
                )
            ]
        ]
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔍 IP Analiz",
                    callback_data="ip"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 DNS Yoxlama",
                    callback_data="dns"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 SSL Yoxlama",
                    callback_data="ssl"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌍 URL Analiz",
                    callback_data="url"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛡 Header Analiz",
                    callback_data="headers"
                )
            ]
        ]
    )

    return keyboard



@dp.message(Command("start"))
async def start(message: Message):

    kb = main_menu()

    print("MENU TEST:", kb)

    await message.answer(
        "🛡 SECURITY TOOLKIT",
        reply_markup=kb
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Mövcud komandalar:\n\n"
        "/start - botu başladır\n"
        "/help - kömək menyusu\n"
        "/ip 8.8.8.8 - IP məlumatı\n"
        "/dns example.com - DNS yoxlaması\n"
        "/headers https://example.com - HTTP başlıqları"
        "/ssl example.com - SSL sertifikat analizi\n"
        "/recon example.com - Tam recon analiz\n"


    )


@dp.message(Command("ip"))
async def ip_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/ip 8.8.8.8"
        )
        return

    ip = args[1]

    result = get_ip_info(ip)

    await message.answer(result)


@dp.message(Command("dns"))
async def dns_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/dns example.com"
        )
        return

    domain = args[1]

    result = check_dns(domain)

    await message.answer(result)


@dp.message(Command("headers"))
async def headers_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/headers https://example.com"
        )
        return

    url = args[1]

    result = get_headers(url)

    await message.answer(result)
@dp.message(Command("url"))
async def url_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/url https://example.com"
        )
        return

    url = args[1]

    result = check_url(url)

    await message.answer(result)

@dp.message(Command("ssl"))
async def ssl_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/ssl example.com"
        )
        return

    domain = args[1]

    result = check_ssl(domain)

    await message.answer(result)

@dp.callback_query()
async def menu_callback(callback):

    data = callback.data

    if data == "tool_sqli":

        waiting_tool[callback.from_user.id] = "sqli"

        await callback.message.answer(
            "💉 SQLi Audit\n\nURL göndərin:"
        )

    elif data == "tool_xss":

        waiting_tool[callback.from_user.id] = "xss"

        await callback.message.answer(
            "⚔️ XSS Audit\n\nURL göndərin:"
        )

    elif data == "tool_auth":

        waiting_tool[callback.from_user.id] = "auth"

        await callback.message.answer(
            "🔐 Authentication Audit\n\nURL göndərin:"
        )

    elif data == "tool_files":

        waiting_tool[callback.from_user.id] = "files"

        await callback.message.answer(
            "📂 Sensitive Files\n\nDomain göndərin:"
        )

    elif data == "tool_security":

        waiting_tool[callback.from_user.id] = "security"

        await callback.message.answer(
            "🛡 Security Check\n\nURL göndərin:"
        )

    elif data == "tool_wp":

        waiting_tool[callback.from_user.id] = "wp"

        await callback.message.answer(
            "📋 WordPress Check\n\nDomain göndərin:"
        )

    elif data == "back_main":

        await callback.message.edit_text(
            "🛡 SECURITY TOOLKIT",
            reply_markup=main_menu()
        )



    await callback.answer()



@dp.message(SSLState.waiting_domain)
async def process_ssl(message: Message, state: FSMContext):

    domain = message.text

    result = check_ssl(domain)

    await message.answer(result)

    await state.clear()

@dp.message(Command("recon"))
async def recon_command(message: Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/recon example.com"
        )
        return

    domain = args[1]

    result = recon_domain(domain)

    await message.answer(result)

@dp.message(Command("report"))
async def report_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/report example.com"
        )
        return

    domain = args[1]

    result = generate_report(domain)

    await message.answer(result)

@dp.message(Command("cve"))
async def cve_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/cve wordpress"
        )
        return


    keyword = " ".join(args[1:])

    result = cve_lookup(keyword)

    await message.answer(result)


@dp.message(Command("vt"))
async def vt_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/vt example.com"
        )
        return


    domain = args[1]

    result = vt_lookup(domain)

    await message.answer(result)



@dp.message(Command("nmap"))
async def nmap_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/nmap example.com"
        )
        return

    target = args[1]

    result = nmap_scan(target)

    await message.answer(result)



@dp.message(Command("xsscheck"))
async def xss_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/xsscheck example.com"
        )
        return


    domain = args[1]

    result = xss_audit(domain)

    await message.answer(result)



@dp.message(Command("urlcheck"))
async def urlcheck_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/urlcheck https://example.com"
        )
        return


    url = args[1]

    result = analyze_url(url)

    await message.answer(result)



@dp.message(Command("files"))
async def files_command(message: Message):

    args = message.text.split()

    if len(args) < 2:

        await message.answer(
            "İstifadə:\n/files example.com"
        )

        return


    domain = args[1]

    result = file_check(domain)

    await message.answer(result)



@dp.message(Command("cors"))
async def cors_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/cors example.com"
        )
        return


    domain = args[1]

    result = cors_check(domain)

    await message.answer(result)



@dp.message(Command("cookies"))
async def cookies_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/cookies example.com"
        )
        return


    domain = args[1]

    result = cookie_check(domain)

    await message.answer(result)



@dp.message(Command("wpcheck"))
async def wpcheck_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/wpcheck example.com"
        )
        return


    domain = args[1]

    result = wordpress_check(domain)

    await message.answer(result)


@dp.message(Command("wpcve"))
async def wpcve_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/wpcve elementor"
        )
        return


    component = args[1]

    result = wp_cve_lookup(component)

    await message.answer(result)




@dp.message(Command("sqli"))
async def sqli_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/sqli https://site.com/page?id=1"
        )
        return


    url = args[1]

    result = sqli_audit(url)

    await message.answer(result)




@dp.message(Command("sqliform"))
async def sqliform_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/sqliform https://site.com"
        )
        return


    url = args[1]

    result = sqli_form_audit(url)

    await message.answer(result)


@dp.message(Command("sqliaudit"))
async def sqliaudit_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/sqliaudit https://site.com"
        )
        return


    url = args[1]

    result = sqliaudit(url)

    await message.answer(result)



@dp.message(Command("auth"))
async def auth_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/auth https://site.com"
        )
        return


    url = args[1]

    result = auth_check(url)

    await message.answer(result)



@dp.message(Command("sensitive"))
async def sensitive_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/sensitive example.com"
        )
        return


    domain = args[1]

    result = sensitive_file_check(domain)

    await message.answer(result)



@dp.message(Command("security"))
async def security_command(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer(
            "İstifadə:\n/security https://site.com"
        )
        return


    url = args[1]

    result = security_config_check(url)

    await message.answer(result)





@dp.message()
async def tool_runner(message: Message):

    user_id = message.from_user.id

    if user_id not in waiting_tool:
        return

    tool = waiting_tool[user_id]
    url = message.text.strip()

    if tool == "sqli":

        await message.answer("💉 SQLi Audit başladı...")

        result = sqliaudit(url)

        await message.answer(
            str(result)
        )


    elif tool == "xss":

        await message.answer("⚔️ XSS Audit başladı...")

        result = xss_audit(url)

        await message.answer(
            str(result)
        )


    elif tool == "auth":

        await message.answer("🔐 Authentication Audit başladı...")

        result = auth_check(url)

        await message.answer(
            str(result)
        )


    del waiting_tool[user_id]

   

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
