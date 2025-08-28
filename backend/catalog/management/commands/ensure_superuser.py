import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a Django superuser from env if it doesn't exist. No-op if variables are missing."

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not (username and password):
            self.stdout.write(self.style.WARNING('DJANGO_SUPERUSER_* not set; skipping ensure_superuser'))
            return

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS('Superuser already exists; nothing to do'))
            return

        User.objects.create_superuser(username=username, email=email or '', password=password)
        self.stdout.write(self.style.SUCCESS(f'Created superuser "{username}"'))
