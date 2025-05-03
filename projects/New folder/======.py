blocked_sites = ["Daily News Egypt.com", "bCNN..com"]


text = "You should visit example.com and badwebsite.com for more information."

def web_filter_interactive(text, blocked_sites):

    for site in blocked_sites:
        if site in text:
            if input(f"Block '{site}'? (yes/no): ").strip().lower() == 'yes':
                text = text.replace(site, "BLOCKED")
    return text

print(f"{text}")

filtered_text = web_filter_interactive(text, blocked_sites)

print(f"{filtered_text}")
