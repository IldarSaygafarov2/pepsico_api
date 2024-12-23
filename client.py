import requests


BASE_URL = "http://127.0.0.1:8000/api/v1"
HEADERS = {
    "Accept-Language": "en",
}

# print("categories", "=" * 50)
# print(requests.get(f"{BASE_URL}/homepage/categories", headers=HEADERS).json())

# print("history", "=" * 50)
# print(requests.get(f"{BASE_URL}/history/brand", headers=HEADERS).json())
