import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filmes_discord.settings")
django.setup()

from django.core.management import call_command

call_command("migrate")
