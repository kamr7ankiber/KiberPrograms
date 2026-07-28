import requests


def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"

    response = requests.get(url)

    if response.status_code != 200:
        return "IP məlumatı tapılmadı."

    data = response.json()

    result = (
        f"IP: {data.get('ip')}\n"
        f"Ölkə: {data.get('country')}\n"
        f"Şəhər: {data.get('city')}\n"
        f"Provayder: {data.get('org')}"
    )

    return result
