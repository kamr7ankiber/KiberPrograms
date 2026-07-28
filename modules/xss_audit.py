import requests
from bs4 import BeautifulSoup


def xss_audit(domain):

    result = "🛡 XSS AUDIT\n\n"
    result += f"Target: {domain}\n\n"

    try:

        response = requests.get(
            f"https://{domain}",
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        html = response.text

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # Forms
        forms = soup.find_all("form")

        result += f"Forms: {len(forms)}\n"


        # Inputs
        inputs = soup.find_all("input")

        result += f"Inputs: {len(inputs)}\n\n"


        if inputs:

            result += "Input sahələri:\n"

            for item in inputs:

                name = item.get(
                    "name",
                    "unknown"
                )

                typ = item.get(
                    "type",
                    "text"
                )

                result += (
                    f"- {name} "
                    f"({typ})\n"
                )


        result += "\n"


        # CSP
        if "Content-Security-Policy" in response.headers:

            result += (
                "CSP: Enabled ✅\n"
            )

        else:

            result += (
                "CSP: Missing ⚠️\n"
            )


        # Inline scripts
        scripts = soup.find_all("script")

        result += (
            f"Scripts: {len(scripts)}\n"
        )


        if scripts:

            result += (
                "Qeyd: "
                "Script elementləri mövcuddur\n"
            )


        return result


    except Exception as e:

        return f"XSS audit xətası: {e}"
