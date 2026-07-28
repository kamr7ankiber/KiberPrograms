import requests


def get_whois(domain):

    result = "📋 WHOIS\n\n"

    try:
        url = f"https://rdap.org/domain/{domain}"

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:
            return "WHOIS məlumatı tapılmadı"

        data = response.json()

        result += f"Domen:\n{data.get('ldhName')}\n\n"

        events = data.get("events", [])

        for event in events:
            action = event.get("eventAction")
            date = event.get("eventDate")

            result += f"{action}: {date}\n"

        return result

    except Exception as e:
        return f"WHOIS xətası: {e}"
