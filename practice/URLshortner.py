import requests
api_key = "b1d8c235f95a083ddbc6f65e06fa2afab6a55f69"
url = input("enter url")
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)