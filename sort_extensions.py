import json
from operator import itemgetter
from pathlib import Path


def sort_extensions():
    extensions_file = Path("data/extensions.json")
    extensions = extensions_file.read_text()
    extensions = json.loads(extensions)
    sorted_extensions = dict(sorted(extensions.items(), key=lambda item: item[1]["is_official"], reverse=True))
    extensions_file.write_text(json.dumps(sorted_extensions, indent=2))


if __name__ == "__main__":
    sort_extensions()
