import ssl
import socket
from datetime import datetime


def check_ssl(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

        issuer = dict(x[0] for x in cert["issuer"])
        subject = dict(x[0] for x in cert["subject"])

        expire = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        today = datetime.utcnow()
        days_left = (expire - today).days

        result = (
            f"🔒 SSL Analiz\n\n"
            f"Domen: {domain}\n"
            f"Sahib: {subject.get('commonName')}\n"
            f"Verən: {issuer.get('organizationName')}\n"
            f"Bitmə tarixi: {expire}\n"
            f"Qalan gün: {days_left}"
        )

        return result

    except Exception as e:
        return f"SSL yoxlanmadı: {e}"
