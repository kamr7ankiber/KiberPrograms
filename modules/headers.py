import requests


def get_headers(url):
    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        result = (
            f"URL: {url}\n\n"
            f"Server: {headers.get('Server', 'Yoxdur')}\n"
            f"Content-Type: {headers.get('Content-Type', 'Yoxdur')}\n"
            f"X-Frame-Options: {headers.get('X-Frame-Options', 'Yoxdur')}\n"
            f"Content-Security-Policy: {headers.get('Content-Security-Policy', 'Yoxdur')}"
        )

        return result

    except Exception:
        return "Sayta qoşulmaq mümkün olmadı."
