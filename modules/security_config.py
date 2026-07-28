import requests


def security_config_check(url):

    result = "🛡 SECURITY MISCONFIGURATION CHECK v2\n\n"
    result += f"Target:\n{url}\n\n"

    issues = 0


    try:

        session = requests.Session()

        response = session.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        headers = response.headers



        # SECURITY HEADERS

        result += "🔒 Security Headers:\n\n"


        security_headers = {

            "Strict-Transport-Security": "HSTS",
            "Content-Security-Policy": "CSP",
            "X-Frame-Options": "X-Frame",
            "X-Content-Type-Options": "X-Content-Type"

        }


        for header, name in security_headers.items():

            if header in headers:

                result += (
                    f"{name}: Enabled ✅\n"
                )

            else:

                issues += 1

                result += (
                    f"{name}: Missing ⚠️\n"
                )



        # SERVER

        result += "\n🖥 Server Information:\n\n"


        server = headers.get(
            "Server"
        )


        if server:

            issues += 1

            result += (
                f"Server: {server}\n"
            )

            result += (
                "Risk: Information Disclosure ⚠️\n"
            )

        else:

            result += (
                "Server: Hidden ✅\n"
            )



        # COOKIE CHECK

        result += "\n🍪 Cookie Security:\n\n"


        cookies = headers.get(
            "Set-Cookie"
        )


        if cookies:

            if "httponly" in cookies.lower():

                result += (
                    "HttpOnly: Enabled ✅\n"
                )

            else:

                issues += 1

                result += (
                    "HttpOnly: Missing ⚠️\n"
                )


            if "secure" in cookies.lower():

                result += (
                    "Secure: Enabled ✅\n"
                )

            else:

                issues += 1

                result += (
                    "Secure: Missing ⚠️\n"
                )

        else:

            result += (
                "Cookie: Not Found\n"
            )



        # HTTP METHODS

        result += "\n🌐 HTTP Methods:\n\n"


        try:

            opt = requests.options(
                url,
                timeout=5
            )


            allow = opt.headers.get(
                "Allow"
            )


            if allow:

                result += (
                    f"Allowed: {allow}\n"
                )


                if "TRACE" in allow:

                    issues += 1

                    result += (
                        "TRACE enabled ⚠️\n"
                    )


            else:

                result += (
                    "Method info unavailable\n"
                )


        except:

            result += (
                "Method check failed\n"
            )



        # DEFAULT FILES

        result += "\n📂 Default Files:\n\n"


        test_files = [

            "server-status",
            "phpinfo.php",
            "test.php"

        ]


        for file in test_files:

            try:

                r = requests.get(
                    url.rstrip("/") + "/" + file,
                    timeout=5
                )


                if r.status_code == 200:

                    issues += 1

                    result += (
                        f"Found: /{file} ⚠️\n"
                    )


            except:

                pass



        # SUMMARY

        result += "\n📊 Summary:\n\n"

        result += (
            f"Issues Found: {issues}\n"
        )


        if issues:

            result += (
                "Risk: 🟡 Review Required"
            )

        else:

            result += (
                "Risk: 🟢 No issues detected"
            )


        return result



    except Exception as e:

        return f"Security config error: {e}"
