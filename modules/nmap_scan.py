import subprocess


def nmap_scan(target):

    result = "🔍 NMAP SCAN\n\n"
    result += f"Target: {target}\n\n"

    try:

        scan = subprocess.check_output(
            [
                "nmap",
                "-sV",
                "--top-ports",
                "20",
                target
            ],
            text=True,
            timeout=60
        )


        result += scan

        return result


    except subprocess.TimeoutExpired:

        return result + "Scan vaxt limiti aşdı"


    except Exception as e:

        return result + f"Nmap xətası: {e}"
