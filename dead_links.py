import json
from pathlib import Path
import urllib.request
import threading


def check_link(url):
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {url} {e.code}")
    except urllib.error.URLError as e:
        print(f"URLError: {url} {e.reason}")
    else:
        print(f"OK: {url}")


def check_dead_links():
    extensions = Path("data/extensions.json")
    extensions = extensions.read_text()
    extensions = json.loads(extensions)
    threads = []
    for extension in extensions.values():
        doc_url = extension["doc_url"]
        download_url = extension["download_url"]
        thread1 = threading.Thread(target=check_link, args=(doc_url,))
        thread2 = threading.Thread(target=check_link, args=(download_url,))
        thread1.start()
        thread2.start()
        threads.append(thread1)
        threads.append(thread2)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    check_dead_links()
