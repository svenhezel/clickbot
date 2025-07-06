import urllib.request
import random
import time

# Proxy configuration
proxy_url = "https:/user_name:password@proxyprovider.com:port_number"
proxy_handler = urllib.request.ProxyHandler({
    'http': proxy_url,
    'https': proxy_url
})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

# User agents (modern desktop & mobile devices)
user_agents = [
    # Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",

    # Mobile
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
]

# Browser languages
languages = ["en-US", "en-CA", "es-ES"]

# Referrers
referrers = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://twitter.com/",
    "https://www.instagram.com/"
]

# Target URL
target_url = "https://example.com"

def make_request():
    user_agent = random.choice(user_agents)
    accept_language = random.choice(languages)
    referer = random.choice(referrers)

    headers = {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
        "Referer": referer
    }

    req = urllib.request.Request(url=target_url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read()
            print(f"Request successful, status: {response.status}, length: {len(content)} bytes")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    while True:
        make_request()
        pause = random.uniform(1, 10)
        print(f"Waiting {pause:.2f} seconds before next Click...")
        time.sleep(pause)
