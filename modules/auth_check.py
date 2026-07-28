import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def auth_check(url):

    result = "🔐 AUTHENTICATION SECURITY AUDIT\n\n"
    result += f"Target:\n{url}\n\n"


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


        forms = soup.find_all(
            "form"
        )


        login_found = False


        result += "Login Analysis:\n\n"


        for form in forms:

            inputs = form.find_all(
                "input"
            )

            names = []


            for inp in inputs:

                name = inp.get(
                    "name"
                )

                inp_type = inp.get(
                    "type",
                    "text"
                )


                if name:

                    names.append(
                        (name, inp_type)
                    )


            has_password = any(
                x[1] == "password"
                for x in names
            )


            if has_password:

                login_found = True

                result += (
                    "Login Form: Detected ✅\n\n"
                )


                for name, inp_type in names:

                    result += (
                        f"- {name}\n"
                        f"  Type: {inp_type}\n"
                    )


                result += "\n"



        if not login_found:

            result += (
                "Login form tapılmadı\n"
            )



        # endpoint izləri

        result += "\nPossible Endpoints:\n"


        paths = [
            "login",
            "admin",
            "wp-admin",
            "signin"
        ]


        for path in paths:

            check = urljoin(
                url,
                path
            )

            result += (
                f"- {check}\n"
            )


        result += (
            "\nQeyd:\n"
            "Bu modul authentication "
            "nöqtələrini analiz edir."
        )


        return result



    except Exception as e:

        return f"Auth audit xətası: {e}"
