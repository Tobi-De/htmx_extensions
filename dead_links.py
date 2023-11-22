import json
from pathlib import Path
import urllib.request
import concurrent.futures
import os
import datetime as dt

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "Tobi-De/htmx_extensions"


def check_link(url):
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {url} {e.code}")
        return url
    except urllib.error.URLError as e:
        print(f"URLError: {url} {e.reason}")
        return url
    else:
        print(f"OK: {url}")


def check_dead_links():
    extensions = Path("data/extensions.json")
    extensions = extensions.read_text()
    extensions = json.loads(extensions)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {
            executor.submit(check_link, url): url
            for extension in extensions.values()
            for url in (extension["doc_url"], extension["download_url"])
        }
    dead_links = [
        future.result()
        for future in concurrent.futures.as_completed(future_to_url)
        if future.result() is not None
    ]
    return dead_links


def create_github_issue(dead_links):
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "title": f"Dead links - {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "body": "\n".join(dead_links),
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    urllib.request.urlopen(req)
  



if __name__ == "__main__":
    dead_links = check_dead_links()
    if dead_links:
        create_github_issue(dead_links)
