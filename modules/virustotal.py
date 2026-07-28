import requests

from config import VT_API_KEY


def vt_lookup(domain):

    result = "🦠 VIRUSTOTAL\n\n"
    result += f"Target: {domain}\n\n"


    try:

        url = (
            "https://www.virustotal.com/api/v3/domains/"
            f"{domain}"
        )

        headers = {
            "x-apikey": VT_API_KEY
        }


        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )


        if response.status_code != 200:
            return (
                result +
                "VirusTotal məlumatı alınmadı\n"
                f"Status: {response.status_code}"
            )


        data = response.json()


        stats = data["data"]["attributes"]["last_analysis_stats"]


        result += f"Malicious: {stats.get('malicious',0)}\n"
        result += f"Suspicious: {stats.get('suspicious',0)}\n"
        result += f"Harmless: {stats.get('harmless',0)}\n"
        result += f"Undetected: {stats.get('undetected',0)}\n"


        return result


    except Exception as e:

        return f"VirusTotal xətası: {e}"
