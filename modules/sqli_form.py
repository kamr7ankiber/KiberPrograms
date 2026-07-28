import requests
from bs4 import BeautifulSoup


def sqli_form_audit(url):

    result = "💉 SQLi FORM AUDIT\n\n"
    result += f"URL:\n{url}\n\n"

    try:

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


        forms = soup.find_all("form")


        if not forms:

            result += "Form tapılmadı\n"
            return result


        for form in forms:

            method = form.get(
                "method",
                "GET"
            ).upper()


            result += (
                f"Form Method: {method}\n"
            )


            inputs = form.find_all(
                "input"
            )


            if inputs:

                result += "Inputs:\n"

                for inp in inputs:

                    name = inp.get(
                        "name"
                    )

                    if name:

                        result += (
                            f"- {name}\n"
                        )


                        if name.lower() in [
                            "id",
                            "user",
                            "username",
                            "search",
                            "query",
                            "product"
                        ]:

                            result += (
                                "  Risk: 🟡 Review\n"
                            )


            result += "\n"


        result += (
            "Qeyd:\n"
            "Input sahələri təhlükəsizlik "
            "auditində yoxlanmalıdır."
        )


        return result


    except Exception as e:

        return f"Form audit xətası: {e}"
