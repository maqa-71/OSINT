import aiohttp
import asyncio
from bs4 import BeautifulSoup

urls = [
    "https://github.com",
    "https://python.org",

]

async def fetch_title(session, url):
    try:
        async with session.get(url) as r:
            html = await r.text()
            soup = BeautifulSoup(html, "html.parser")
            title = soup.find("title").text.strip()
            return url, title
    except Exception as e:
        return url, f"Ошибка: {e}"

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_title(session, u) for u in urls]
        results = await asyncio.gather(*tasks)

        for url, title in results:
            print(f"{url} → {title}")

asyncio.run(main())
