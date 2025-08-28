from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import shutil


class Command(BaseCommand):
    help = "Copy default media from repo 'media' folder into MEDIA_ROOT if missing."

    def handle(self, *args, **options):
        src = Path(settings.BASE_DIR) / 'media'
        dst = Path(settings.MEDIA_ROOT)

        if not src.exists() or not src.is_dir():
            self.stdout.write(self.style.WARNING("No repo media folder found; skipping."))
            return

        dst.mkdir(parents=True, exist_ok=True)

        copied = 0
        for path in src.rglob('*'):
            rel = path.relative_to(src)
            target = dst / rel
            if path.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                # Always overwrite to keep repo media in sync
                shutil.copy2(path, target)
                copied += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Failed to copy {path} -> {target}: {e}"))

        # Log a quick summary of known subfolders for debug
        cats = (dst / 'categories')
        prods = (dst / 'products')
        cats_n = sum(1 for _ in cats.rglob('*') if _.is_file()) if cats.exists() else 0
        prods_n = sum(1 for _ in prods.rglob('*') if _.is_file()) if prods.exists() else 0
        self.stdout.write(self.style.SUCCESS(
            f"sync_default_media done. Copied {copied} files. categories={cats_n}, products={prods_n}"
        ))
