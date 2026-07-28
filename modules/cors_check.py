import requests


def cors_check(domain):

    result = "🌐 CORS ANALYZER\n\n"
    result += f"Target: {domain}\n\n"

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "Origin": "https://test.example"
            }
        )

        headers = response.headers


        allow_origin = headers.get(
            "Access-Control-Allow-Origin",
            "Missing"
        )

        allow_methods = headers.get(
            "Access-Control-Allow-Methods",
            "Missing"
        )

        allow_credentials = headers.get(
            "Access-Control-Allow-Credentials",
            "Missing"
        )


        result += (
            f"Allow-Origin: "
            f"{allow_origin}\n"
        )

        result += (
            f"Allow-Methods: "
            f"{allow_methods}\n"
        )

        result += (
            f"Allow-Credentials: "
            f"{allow_credentials}\n\n"
        )


        if allow_origin == "*":

            result += (
                "⚠️ Risk:\n"
                "Wildcard origin istifadə olunur"
            )

        else:

            result += (
                "✅ Risk:\n"
                "Wildcard tapılmadı"
            )


        return result


    except Exception as e:

        return f"CORS xətası: {e}"
