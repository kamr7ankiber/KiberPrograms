import requests


def sensitive_file_check(domain):

    result = "📂 SENSITIVE FILE DISCOVERY v2\n\n"
    result += f"Target: {domain}\n\n"


    files = {

        "robots.txt": "Information",
        "sitemap.xml": "Information",

        ".env": "Configuration",
        ".git/config": "Source Control",

        "backup.zip": "Backup",
        "backup.sql": "Database Backup",
        "database.sql": "Database Backup",
        "dump.sql": "Database Backup",

        "config.php": "Configuration",
        "wp-config.php": "WordPress Configuration",

        "debug.log": "Debug File",
        "error.log": "Log File",

        "phpinfo.php": "Information Disclosure"
    }


    public = 0
    possible = 0
    protected = 0


    for file, category in files.items():

        url = f"https://{domain}/{file}"


        try:

            response = requests.get(
                url,
                timeout=8,
                allow_redirects=False,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )


            length = len(response.content)

            content_type = response.headers.get(
                "Content-Type",
                ""
            )


            # 403

            if response.status_code == 403:

                protected += 1

                result += (
                    f"🔒 Protected: /{file}\n"
                    f"Category: {category}\n"
                    "Status: Forbidden\n\n"
                )


            # 200 analiz

            elif response.status_code == 200:


                text = response.text.lower()


                error_words = [
                    "not found",
                    "404",
                    "access denied",
                    "forbidden",
                    "page not found"
                ]


                fake_page = any(
                    word in text
                    for word in error_words
                )


                if fake_page:

                    result += (
                        f"⚠️ Possible False Positive: /{file}\n"
                    )

                    result += (
                        "Reason: Error page detected\n\n"
                    )


                else:

                    possible += 1

                    result += (
                        f"⚠️ Possible Exposure: /{file}\n"
                    )

                    result += (
                        f"Category: {category}\n"
                    )

                    result += (
                        f"Size: {length} bytes\n"
                    )

                    result += (
                        f"Content-Type: {content_type}\n\n"
                    )


        except Exception:

            pass



    result += "📊 Summary:\n\n"

    result += (
        f"Possible Exposure: {possible}\n"
    )

    result += (
        f"Protected: {protected}\n"
    )


    if possible:

        result += (
            "\nRisk:\n"
            "🟡 Review Required"
        )

    else:

        result += (
            "\nRisk:\n"
            "🟢 No confirmed exposure"
        )


    return result
