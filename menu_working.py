from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Recon",
                    callback_data="recon_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💉 SQL/XSS",
                    callback_data="vuln_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛡 Security",
                    callback_data="security_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 CMS",
                    callback_data="cms_menu"
                )
            ]
        ]
    )

    return keyboard



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
                    text="⬅️ Geri",
                    callback_data="back_main"
                )
            ]
        ]
    )


def vuln_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💉 SQLi Audit",
                    callback_data="tool_sqli"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚔️ XSS Analyzer",
                    callback_data="tool_xss"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔐 Authentication",
                    callback_data="tool_auth"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📂 Sensitive Files",
                    callback_data="tool_files"
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


def security_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛡 Misconfiguration",
                    callback_data="tool_security"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 SSL Check",
                    callback_data="tool_ssl"
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


def cms_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 WordPress Check",
                    callback_data="tool_wp"
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
