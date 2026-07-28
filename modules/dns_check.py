import dns.resolver


def check_dns(domain):
    result = []

    try:
        answers = dns.resolver.resolve(domain, "A")
        ips = []

        for answer in answers:
            ips.append(str(answer))

        result.append("A record:\n" + "\n".join(ips))

    except:
        result.append("A record tapılmadı.")

    try:
        answers = dns.resolver.resolve(domain, "MX")

        mx = []

        for answer in answers:
            mx.append(str(answer))

        result.append("MX record:\n" + "\n".join(mx))

    except:
        result.append("MX record tapılmadı.")

    return "\n\n".join(result)
