import requests
import time


def wp_cve_lookup(component):

    result = f"🔍 {component}\n"

    try:

        url = (
            "https://services.nvd.nist.gov/rest/json/"
            "cves/2.0"
        )

        params = {
            "keywordSearch": component,
            "resultsPerPage": 3
        }


        response = requests.get(
            url,
            params=params,
            timeout=15,
            headers={
                "User-Agent": "SecurityBot"
            }
        )


        if response.status_code != 200:

            return (
                result +
                f"CVE API cavabı: {response.status_code}\n\n"
            )


        data = response.json()


        total = data.get(
            "totalResults",
            0
        )


        result += (
            f"CVE nəticəsi: {total}\n"
        )


        for item in data.get(
            "vulnerabilities",
            []
        ):

            result += (
                f"- {item['cve']['id']}\n"
            )


        time.sleep(1)

        return result + "\n"



    except Exception as e:

        return (
            result +
            f"CVE xətası: {e}\n\n"
        )
