from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalog", "0012_alter_aboutpage_options_alter_category_options_and_more"),
    ]

    operations = [
        # Proxy models don't create DB tables, but having an initial migration with proper
        # dependency ensures Django can resolve bases during state rendering in migrate.
        migrations.RunPython(code=migrations.RunPython.noop, reverse_code=migrations.RunPython.noop),
    ]
