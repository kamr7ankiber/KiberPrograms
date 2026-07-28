import socket
import requests


def find_subdomains(domain):

    result = "🌐 SUBDOMAIN DISCOVERY\n\n"

    subdomains = [
        "www",
        "mail",
        "api",
        "dev",
        "test",
        "admin",
        "portal",
        "ftp"
    ]

    found = False


    for sub in subdomains:

        host = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(host)

            result += f"✅ {host}\n"
            result += f"IP: {ip}\n"


            try:
                response = requests.get(
                    f"https://{host}",
                    timeout=5
                )

                result += (
                    f"HTTP: "
                    f"{response.status_code}\n"
                )

                result += (
                    f"Server: "
                    f"{response.headers.get('Server','Unknown')}\n"
                )

            except:
                result += "HTTP: Alınmadı\n"


            result += "\n"

            found = True


        except:
            pass


    if not found:
        result += "Subdomain tapılmadı"


    return result
