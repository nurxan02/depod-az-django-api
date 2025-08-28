from django.db import models
from catalog.models import AboutPage, ContactPage, FooterSettings


class AboutPageProxy(AboutPage):
    class Meta:
        proxy = True
        verbose_name = "Haqqında Səhifəsi"
        verbose_name_plural = "Haqqında Səhifəsi"
        app_label = 'sitecontent'


class ContactPageProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "Əlaqə Səhifəsi"
        verbose_name_plural = "Əlaqə Səhifəsi"
        app_label = 'sitecontent'


class FooterSettingsProxy(FooterSettings):
    class Meta:
        proxy = True
        verbose_name = "Footer Hissəsi"
        verbose_name_plural = "Footer Hissəsi"
        app_label = 'sitecontent'
