import socket
import requests

from modules.ssl_check import check_ssl


def generate_report(domain):

    report = "📄 SECURITY REPORT\n\n"
    report += f"Target: {domain}\n\n"

    risks = []


    # IP
    try:
        ip = socket.gethostbyname(domain)
        report += f"🌐 IP:\n{ip}\n\n"
    except:
        report += "🌐 IP: Tapılmadı\n\n"
        risks.append("IP məlumatı alınmadı")


    # HTTP
    try:
        response = requests.get(
            f"https://{domain}",
            timeout=5
        )

        report += "🌍 HTTP:\n"
        report += f"Status: {response.status_code}\n"

        server = response.headers.get(
            "Server",
            "Yoxdur"
        )

        report += f"Server: {server}\n\n"


        if response.status_code >= 400:
            risks.append(
                f"HTTP status {response.status_code}"
            )

        if server == "Yoxdur":
            risks.append(
                "Server məlumatı gizlədilir"
            )


    except:
        report += "🌍 HTTP: Alınmadı\n\n"
        risks.append("HTTP yoxlaması uğursuz oldu")


    # SSL
    try:
        ssl_result = check_ssl(domain)

        report += "🔒 SSL:\n"
        report += ssl_result + "\n\n"

    except:
        report += "🔒 SSL: Alınmadı\n\n"
        risks.append("SSL yoxlaması uğursuz oldu")


    # Risk hesablaması

    if len(risks) == 0:
        risk = "🟢 LOW"

    elif len(risks) <= 2:
        risk = "🟡 MEDIUM"

    else:
        risk = "🔴 HIGH"


    report += f"⚠️ Risk: {risk}\n\n"


    if risks:
        report += "Qeydlər:\n"

        for item in risks:
            report += f"- {item}\n"

    else:
        report += "Qeydlər:\n- Problem aşkar edilmədi"


    return report
