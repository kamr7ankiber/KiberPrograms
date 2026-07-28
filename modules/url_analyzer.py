import requests
from urllib.parse import urlparse


def analyze_url(url):

    result = "🔗 URL ANALYZER\n\n"
    result += f"URL:\n{url}\n\n"

    try:

        parsed = urlparse(url)

        domain = parsed.netloc

        if not domain:
            domain = parsed.path


        result += f"Domain:\n{domain}\n\n"


        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        result += (
            f"Status:\n"
            f"{response.status_code}\n\n"
        )


        result += (
            "Final URL:\n"
            f"{response.url}\n\n"
        )


        server = response.headers.get(
            "Server",
            "Unknown"
        )


        result += (
            "Server:\n"
            f"{server}\n\n"
        )


        if parsed.scheme == "https":

            result += (
                "HTTPS:\n"
                "Enabled ✅"
            )

        else:

            result += (
                "HTTPS:\n"
                "Disabled ⚠️"
            )


        return result


    except Exception as e:

        return f"URL Analyzer xətası: {e}"
