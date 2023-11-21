from pathlib import Path

from coltrane.config.paths import get_data_directory
from coltrane.management.commands.build import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):  # noqa: ARG002
        super().handle(*args, **options)

        source = Path(get_data_directory() / "extensions.json")
        destination = Path(self.output_directory / "extensions.json")

        destination.write_text(source.read_text())
