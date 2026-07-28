import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup


def sqliaudit(url):

    result = "💉 SQLi FULL AUDIT\n\n"
    result += f"URL:\n{url}\n\n"

    risk_words = [
        "id",
        "user",
        "username",
        "search",
        "query",
        "page",
        "item",
        "product",
        "cat"
    ]

    get_count = 0
    post_count = 0
    risk_count = 0


    try:

        # GET Parametr analizi

        parsed = urlparse(url)

        params = parse_qs(
            parsed.query
        )


        result += "🌐 GET Parameters:\n"

        if params:

            for param in set(params):

                get_count += 1

                result += f"- {param}\n"

                if param.lower() in risk_words:

                    risk_count += 1

                    result += (
                        "  Risk: 🟡 Medium\n"
                    )

        else:

            result += "Yoxdur\n"



        # HTML analiz

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        result += "\n📋 POST Forms:\n"


        forms = soup.find_all(
            "form"
        )


        if forms:

            for form in forms:

                method = form.get(
                    "method",
                    "GET"
                ).upper()


                if method == "POST":

                    result += (
                        "\nForm: POST\n"
                    )


                    names = set()


                    for inp in form.find_all(
                        "input"
                    ):

                        name = inp.get(
                            "name"
                        )

                        inp_type = inp.get(
                            "type",
                            "text"
                        )


                        if name:

                            names.add(
                                (name, inp_type)
                            )


                    for name, inp_type in names:

                        post_count += 1

                        result += (
                            f"- {name}\n"
                            f"  Type: {inp_type}\n"
                        )


                        if name.lower() in risk_words:

                            risk_count += 1

                            result += (
                                "  Risk: 🟡 Medium\n"
                            )


        else:

            result += "POST form yoxdur\n"



        result += "\n📊 Summary:\n\n"

        result += (
            f"GET Parameters: {get_count}\n"
        )

        result += (
            f"POST Inputs: {post_count}\n"
        )

        result += (
            f"Risk Indicators: {risk_count}\n"
        )


        if risk_count:

            result += (
                "\nStatus:\n"
                "🟡 Review Required"
            )

        else:

            result += (
                "\nStatus:\n"
                "🟢 No indicators found"
            )


        result += (
            "\n\nQeyd:\n"
            "Bu analiz risk göstəricisidir, "
            "zəifliyi təsdiqləmir."
        )


        return result


    except Exception as e:

        return f"SQLi audit xətası: {e}"
