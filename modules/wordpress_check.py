import requests
import re
from modules.wp_cve import wp_cve_lookup


def wordpress_check(domain):

    result = "📝 WORDPRESS SECURITY CHECK\n\n"
    result += f"Target: {domain}\n\n"

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        html = response.text


        if "wp-content" in html or "wp-includes" in html:

            result += "WordPress: Detected ✅\n\n"

        else:

            result += "WordPress izi tapılmadı\n"
            return result



        version = re.search(
            r'content="WordPress ([0-9.]+)"',
            html
        )


        if version:

            result += f"Version: {version.group(1)}\n"

        else:

            result += "Version: Gizlədilib\n"



        themes = re.findall(
            r'wp-content/themes/([^/]+)',
            html
        )


        if themes:

            result += "\nTheme:\n"

            for theme in set(themes):

                result += f"- {theme}\n"



        plugins = re.findall(
            r'wp-content/plugins/([^/]+)',
            html
        )


        if plugins:

            result += "\nPlugins + CVE:\n\n"
            

            plugins = [
    p for p in set(plugins)
    if p.isalnum() or "-" in p
]

 
            for plugin in set(plugins):

                result += f"🔌 Plugin: {plugin}\n"

                cve = wp_cve_lookup(plugin)

                result += cve
                result += "\n"


        else:

            result += "\nPlugin izi tapılmadı\n"



        return result


    except Exception as e:

        return f"WordPress yoxlama xətası: {e}"
