import requests
from urllib.parse import urlparse


def check_url(url):
    try:
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        parsed = urlparse(url)

        result = (
            f"URL: {url}\n"
            f"Domen: {parsed.netloc}\n"
            f"Status kodu: {response.status_code}\n"
            f"Final URL: {response.url}\n"
            f"Server: {response.headers.get('Server', 'Yoxdur')}"
        )

        return result

    except Exception as e:
        return f"URL yoxlanmadı: {e}"
