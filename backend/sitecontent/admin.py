from django.contrib import admin
from .models import AboutPageProxy, ContactPageProxy, FooterSettingsProxy


# Reuse existing ModelAdmin classes from catalog
from catalog.admin import (
    AboutPageAdmin as BaseAboutAdmin,
    ContactPageAdmin as BaseContactAdmin,
    FooterSettingsAdmin as BaseFooterAdmin,
)


@admin.register(AboutPageProxy)
class AboutPageAdmin(BaseAboutAdmin):
    pass


@admin.register(ContactPageProxy)
class ContactPageAdmin(BaseContactAdmin):
    pass


@admin.register(FooterSettingsProxy)
class FooterSettingsAdmin(BaseFooterAdmin):
    pass
