from bs4 import BeautifulSoup
import urllib.request
from pathlib import Path


def extract_table_data(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    column_data = {}

    if table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 2:
                key = columns[0].get_text().strip()
                value = columns[1].get_text().strip()
                column_data[key] = value
    return column_data


def main():
    extensions_page = "https://htmx.org/extensions/#included"
    table_data = extract_table_data(extensions_page)
    import json
    print(table_data.keys())
    exts = json.loads(Path("data/extensions.json").read_text())
    print(exts.keys())
    # for key, value in table_data.items():
    #     print(f"{key}: {value}\n\n")
    for key in exts.keys():
        if key not in table_data.keys():
            print(f"{key}: \n\n")


if __name__ == '__main__':
    main()