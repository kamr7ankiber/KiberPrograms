import requests


def detect_technology(domain):

    result = "🖥 TECHNOLOGY DETECTION\n\n"

    try:
        response = requests.get(
            f"https://{domain}",
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        headers = response.headers
        html = response.text.lower()


        # Server
        server = headers.get(
            "Server",
            "Unknown"
        )

        result += f"Server:\n{server}\n\n"


        # CDN
        if "cloudflare" in str(headers).lower():
            cdn = "Cloudflare"
        else:
            cdn = "Unknown"

        result += f"CDN:\n{cdn}\n\n"


        # CMS
        if "wp-content" in html or "wordpress" in html:
            cms = "WordPress"

        elif "joomla" in html:
            cms = "Joomla"

        elif "drupal" in html:
            cms = "Drupal"

        else:
            cms = "Unknown"


        result += f"CMS:\n{cms}\n\n"


        # Framework izləri
        if "bootstrap" in html:
            framework = "Bootstrap"

        else:
            framework = "Unknown"


        result += f"Framework:\n{framework}\n"


        return result


    except Exception as e:
        return f"Technology xətası: {e}"
