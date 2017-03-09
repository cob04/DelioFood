from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.admin import SingletonAdmin

from .models import HomePage, Slide


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):
    inlines = [SlideInline,]

