import httpx
from lxml import html

GOOGLE_SHOPPING_URL = "https://www.google.com/search?tbm=shop&q={}"

async def fetch_products(query):
    url = GOOGLE_SHOPPING_URL.format(httpx.utils.quote(query))
    async with httpx.AsyncClient(
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    ) as client:
        resp = await client.get(url)
    doc = html.fromstring(resp.text)
    product_cards = doc.xpath('//div[contains(@class,"sh-dgr__grid-result")]')
    results = []
    for card in product_cards:
        name = card.xpath('.//h4/text()') or [""]
        brand = card.xpath('.//*[@class="E5ocAb"]/text()') or [""]
        price = card.xpath('.//*[@class="a8Pemb OFFNJ"]/text()') or [""]
        
        weight = ""
        title_text = name[0]
        for word in title_text.split():
            if any(u in word.lower() for u in ["oz", "g", "kg", "lb", "ml", "l"]):
                weight = word
        results.append({
            "name": name[0],
            "brand": brand[0],
            "price": price[0],
            "weight": weight,
        })
    return results
