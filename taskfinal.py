import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re

urls = [
    "https://www.python.org",
    "https://www.github.com"
]

email_pattern = r"[a-zA-Z0-9.\-_+]+@[a-zA-Z0-9._\-]+\.[a-zA-Z]+"

async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

           
            emails = list(set(re.findall(email_pattern, html)))
            if not emails:
                emails = ["Не найдено"]

            
            links = [a.get("href") for a in soup.find_all("a", href=True)]
            if not links:
                links = ["Не найдено"]

            return url, emails, links

    except Exception as e:
        return url, [f"Ошибка: {e}"], []

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, u) for u in urls]
        results = await asyncio.gather(*tasks)

        for site, emails, links in results:
            print(f"\nСайт: {site}")
            print("Emails:")
            for e in emails:
                print(" -", e)
            print("Ссылки:")
            for l in links[:10]:  
                print(" -", l)

asyncio.run(main())
