import requests


def cookie_check(domain):

    result = "🍪 COOKIE SECURITY ANALYZER\n\n"
    result += f"Target: {domain}\n\n"

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        cookies = response.headers.get(
            "Set-Cookie"
        )


        if not cookies:

            result += (
                "Set-Cookie: Tapılmadı\n\n"
            )

            result += (
                "Qeyd:\n"
                "Ana səhifə cookie göndərmir."
            )

            return result



        result += "Set-Cookie:\n"
        result += cookies + "\n\n"


        cookie_lower = cookies.lower()


        result += "Təhlükəsizlik yoxlaması:\n\n"


        if "secure" in cookie_lower:

            result += "Secure: Enabled ✅\n"

        else:

            result += "Secure: Missing ⚠️\n"



        if "httponly" in cookie_lower:

            result += "HttpOnly: Enabled ✅\n"

        else:

            result += "HttpOnly: Missing ⚠️\n"



        if "samesite" in cookie_lower:

            result += "SameSite: Enabled ✅\n"

        else:

            result += "SameSite: Missing ⚠️\n"


        return result



    except Exception as e:

        return f"Cookie xətası: {e}"
