import asyncio
import aiohttp

username = "example_user"

SITES = {
    "GitHub": f"https://github.com/{username}",
    "Twitter": f"https://x.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Instagram": f"https://www.instagram.com/{username}",
}

async def check_profile(session, site, url):
    try:
        async with session.get(url, allow_redirects=True) as r:
            if r.status == 200:
                return site, True, url
            else:
                return site, False, None
    except:
        return site, False, None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [check_profile(session, site, url) for site, url in SITES.items()]
        results = await asyncio.gather(*tasks)

        print("\nРезультат:")
        for site, found, link in results:
            if found:
                print(f"[+] Найдено на {site}: {link}")
            else:
                print(f"[-] Нет профиля на {site}")

asyncio.run(main())
