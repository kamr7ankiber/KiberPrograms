from urllib.parse import urlparse, parse_qs


def sqli_audit(url):

    result = "💉 SQLi AUDIT\n\n"
    result += f"URL:\n{url}\n\n"

    try:

        parsed = urlparse(url)

        params = parse_qs(
            parsed.query
        )


        if not params:

            result += "Parametr tapılmadı\n"

            return result



        result += "Parametrlər:\n"

        risk_words = [
            "id",
            "page",
            "cat",
            "item",
            "product",
            "user",
            "uid",
            "post"
        ]


        for param, value in params.items():

            result += f"- {param}\n"


        result += "\n🔎 Risk Analizi:\n\n"


        for param, value in params.items():

            if param.lower() in risk_words:

                result += (
                    f"Parameter: {param}\n"
                )

                result += (
                    "Tip: GET parameter\n"
                )

                result += (
                    "Risk: 🟡 Medium\n"
                )

                result += (
                    "Səbəb:\n"
                    "- Database query ilə əlaqəli "
                    "ola biləcək ad aşkarlandı\n\n"
                )

            else:

                result += (
                    f"Parameter: {param}\n"
                    "Risk: 🟢 Low\n\n"
                )


        result += (
            "Qeyd:\n"
            "Bu analiz risk göstəricisidir, "
            "zəifliyi təsdiqləmir."
        )


        return result



    except Exception as e:

        return f"SQLi audit xətası: {e}"
