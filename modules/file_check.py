import requests


def file_check(domain):

    result = "📂 FILE EXPOSURE CHECK\n\n"
    result += f"Target: {domain}\n\n"

    files = [
        "robots.txt",
        "sitemap.xml",
        ".env",
        "backup.zip",
        "backup.sql",
        "config.php",
        ".git/config"
    ]

    found = False


    for file in files:

        url = f"https://{domain}/{file}"

        try:

            response = requests.get(
                url,
                timeout=5,
                allow_redirects=True
            )


            if response.status_code == 200:

                result += (
                    f"⚠️ Found: /{file}\n"
                )

                found = True


            else:

                result += (
                    f"❌ /{file} "
                    f"({response.status_code})\n"
                )


        except:

            result += (
                f"❌ /{file} "
                "Yoxlanmadı\n"
            )


    if not found:

        result += "\nAçıq riskli fayl tapılmadı"


    return result
