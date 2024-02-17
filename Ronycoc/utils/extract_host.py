import re

def extract_host(string: str) -> str:
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    second_lvl_domain_pattern = r'([a-zA-Z0-9-]+\.[a-zA-Z]+)'
    third_lvl_domain_pattern = r'([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z]+)'
    forth_lvl_domain_pattern = r'[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z]+'
    port_pattern = r':((\d+)?)'

    ip_match = re.search(ip_pattern, string)
    second_lvl_domain_match = re.search(second_lvl_domain_pattern, string)
    third_lvl_domain_match = re.search(third_lvl_domain_pattern, string)
    forth_lvl_domain_match = re.search(forth_lvl_domain_pattern, string)
    port_match = re.search(port_pattern, string)

    if port_match and (int (port_match.group(1)) >= 65536 or int (port_match.group(1)) <= 1):
        raise ValueError

    if ip_match:
        result = ip_match.group()
        if port_match and port_match.group(1):
            result += ':' + port_match.group(1)
        return result
    elif forth_lvl_domain_match:
        result = forth_lvl_domain_match.group(1)
        if port_match and port_match.group(1):
            result += ':' + port_match.group(1)
        return result
    elif third_lvl_domain_match:
        result = third_lvl_domain_match.group(1)
        if port_match and port_match.group(1):
            result += ':' + port_match.group(1)
        return result
    elif second_lvl_domain_match:
        result = second_lvl_domain_match.group(1)
        if port_match and port_match.group(1):
            result += ':' + port_match.group(1)
        return result
    else:
        raise ValueError
