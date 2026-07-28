import dns.resolver


def dns_recon(domain):

    result = "📡 DNS RECON\n\n"


    records = {
        "A": "IP",
        "MX": "Mail",
        "NS": "Name Server",
        "TXT": "TXT"
    }


    for record, name in records.items():

        result += f"{name} ({record}):\n"

        try:
            answers = dns.resolver.resolve(
                domain,
                record
            )

            for answer in answers:
                result += f"- {answer}\n"

        except:
            result += "- Tapılmadı\n"

        result += "\n"


    return result
