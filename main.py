import requests

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter (X)": f"https://x.com/{username}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (OSINT-Tool)"
    }

    results = {}

    for site, url in sites.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                results[site] = f"Найдено: {url}"
            elif response.status_code == 404:
                results[site] = "Не найдено"
            else:
                results[site] = f"Неопределённый ответ: {response.status_code}"

        except Exception as e:
            results[site] = f"Ошибка: {e}"

    return results



username = input("Введите никнейм: ")
result = check_username(username)

print("\nРЕЗУЛЬТАТЫ ПОИСКА:")
for site, status in result.items():
    print(f"{site}: {status}")
