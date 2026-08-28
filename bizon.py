import requests
import random
import string

url = "https://api-promo.bizon.az/submit"

def random_code(length=7):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

payload = {
    "phone": input("Nomre daxil et: "),
    "code": random_code(7)
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

r = requests.post(url, json=payload, headers=headers, timeout=10)

print("="*40)
print("GÖNDERİLEN:")
print(payload)
print("="*40)
print("STATUS:", r.status_code)
print("RESPONSE:")
print(r.text)
print("="*40)