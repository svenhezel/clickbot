# Fake Click Bot

⚠️ **For Educational and Awareness Purposes Only**

This repository contains an **educational example** of a Python-based ClickBot. The code was generated using a large language model to demonstrate how **click fraud** can be performed using fake IP addresses, rotating proxies, and deceptive traffic patterns. Its primary goal is to **raise awareness** about the risks of automated ad fraud and how such attacks are orchestrated.

> 💡 If you're a company or developer looking to **protect your ad spend from such threats**, reach out to us at [24metrics.com](https://24metrics.com).

---

## 🔍 Features

- ✅ Proxy support to simulate IPs from various locations and ISPs
- ⏱️ Randomized click intervals to mimic human behavior
- 🌍 Automatic IP location/ISP rotation
- 🌐 Spoofed HTTP headers (e.g. Referer) to fake origins from popular sites like YouTube, Facebook, or Google
- 🧪 Fully scriptable and extendable for demo or research use

---

## 🚨 Disclaimer

This project is intended **strictly for educational use**. Do **not** deploy this code for malicious or commercial purposes. Running a click bot against real platforms without permission **violates Terms of Service**, **ad network policies**, and potentially **local laws**.

We do **not condone** or support any misuse of this code. Use responsibly.

---

## 📖 Related Article

You can read the full breakdown and purpose of this project in our blog post:  
👉 [Building a Malicious Clickbot](https://24metrics.com/blog/building_a_malicious_clickbot)

---

## 🧰 Requirements

- Python 3.7+
- Standard Python libraries (e.g., `random`, `time`, `http.client`, etc.)
- A valid proxy provider account (e.g., [Geonode](https://geonode.com))

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/svenhezel/clickbot
cd clickbot-malicious

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run the script
python clickbot.py
