import requests


def cve_lookup(keyword):

    result = "🛡 CVE LOOKUP\n\n"
    result += f"Axtarış: {keyword}\n\n"

    try:
        url = (
            "https://services.nvd.nist.gov/rest/json/"
            "cves/2.0"
        )

        params = {
            "keywordSearch": keyword,
            "resultsPerPage": 5
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        vulnerabilities = data.get(
            "vulnerabilities",
            []
        )

        if not vulnerabilities:
            return result + "CVE tapılmadı"


        for item in vulnerabilities:

            cve = item["cve"]

            cve_id = cve["id"]

            result += f"🔴 {cve_id}\n"


            descriptions = cve.get(
                "descriptions",
                []
            )

            if descriptions:
                result += (
                    descriptions[0]
                    ["value"][:200]
                    + "\n"
                )

            result += "\n"


        return result


    except Exception as e:
        return f"CVE xətası: {e}"
