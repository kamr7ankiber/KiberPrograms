import requests


def check_security_headers(domain):

    result = "🛡 SECURITY HEADERS\n\n"

    try:
        response = requests.get(
            f"https://{domain}",
            timeout=5
        )

        headers = response.headers


        # HSTS
        if "Strict-Transport-Security" in headers:
            result += "HSTS: Enabled\n"
        else:
            result += "HSTS: Missing\n"


        # CSP
        if "Content-Security-Policy" in headers:
            result += "CSP: Enabled\n"
        else:
            result += "CSP: Missing\n"


        # X-Frame
        if "X-Frame-Options" in headers:
            result += "X-Frame: Enabled\n"
        else:
            result += "X-Frame: Missing\n"


        # X-Content-Type
        if "X-Content-Type-Options" in headers:
            result += "X-Content-Type: Enabled\n"
        else:
            result += "X-Content-Type: Missing\n"


        return result


    except Exception as e:
        return f"Security Headers xətası: {e}"
