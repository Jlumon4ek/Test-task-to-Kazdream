import aiohttp
from bs4 import BeautifulSoup
from config import settings
from datetime import datetime
from zoneinfo import ZoneInfo

utc_plus_5 = ZoneInfo("Asia/Almaty")


class Parser:
    def __init__(self, domain_name):
        self.domain_name = domain_name

    async def fetch_domain_info(self):
        url = f"{settings.BASE_URL}{self.domain_name}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                html = await response.text()
                return html

    def parse_domain_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        error_message = soup.find('div', class_='alert alert-danger')
        if error_message and 'Некорректное доменное имя / IP-адрес.' in error_message.text:
            return {"error": "Некорректное доменное имя / IP-адрес."}

        server_issue_message = soup.find('div', class_='domains-whois__result domains-whois--busy')
        if server_issue_message and 'Возникли непредвиденные проблемы. Попробуйте еще раз через несколько минут.' in server_issue_message.text:
            return {"error": "Возникли непредвиденные проблемы. Попробуйте еще раз через несколько минут."}

        data = {}
        rows = soup.select('table.table tbody tr')
        for row in rows:
            key_cell = row.find('td', class_='valign-top')
            value_cell = key_cell.find_next_sibling('td')

            key = key_cell.text.strip().replace(':', '')
            value = ' '.join(value_cell.get_text(separator=' ').split()).strip()

            data[key] = value
            
        data['Дата парсинга'] = datetime.now(utc_plus_5).isoformat()

        return data

    async def run(self):
        html = await self.fetch_domain_info()
        data = self.parse_domain_info(html)

        return data 
