import socket
import requests

from modules.ssl_check import check_ssl
from modules.dns_recon import dns_recon
from modules.whois_check import get_whois
from modules.tech_detect import detect_technology
from modules.security_headers import check_security_headers
from modules.subdomain import find_subdomains




def recon_domain(domain):

    result = "🔎 RECON ANALİZ\n\n"
    result += f"Domen: {domain}\n\n"


    # IP
    try:
        ip = socket.gethostbyname(domain)
        result += f"🌐 IP: {ip}\n\n"

    except:
        result += "🌐 IP tapılmadı\n\n"


    # DNS RECON
    try:
        dns_result = dns_recon(domain)
        result += dns_result + "\n"

    except:
        result += "📡 DNS məlumatı alınmadı\n\n"


    # HTTP
    try:
        response = requests.get(
            f"https://{domain}",
            timeout=5
        )

        result += "🌍 HTTP:\n"
        result += f"Status: {response.status_code}\n"
        result += (
            f"Server: "
            f"{response.headers.get('Server','Yoxdur')}\n\n"
        )

    except:
        result += "🌍 HTTP məlumatı alınmadı\n\n"

    # TECHNOLOGY

    try:
        tech_result = detect_technology(domain)
        result += tech_result + "\n\n"

    except:
        result += "🖥 Technology məlumatı alınmadı\n\n"

    # SECURITY HEADERS

    try:
        header_result = check_security_headers(domain)
        result += header_result + "\n\n"

    except:
        result += "🛡 Header məlumatı alınmadı\n\n"

    # SUBDOMAINS

    try:
        sub_result = find_subdomains(domain)
        result += sub_result + "\n\n"

    except:
        result += "🌐 Subdomain məlumatı alınmadı\n\n"



    # SSL
    try:
        ssl_result = check_ssl(domain)
        result += ssl_result + "\n"

    except:
        result += "🔒 SSL məlumatı alınmadı\n"

    # WHOIS

    try:
        whois_result = get_whois(domain)
        result += whois_result + "\n\n"

    except:
        result += "📋 WHOIS məlumatı alınmadı\n\n"


    return result
