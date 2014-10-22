from django.contrib import admin
from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import  TabularDynamicInlineAdmin
from .models import Slide, IconBlurb,HomePage, Portfolio
# Register your models here.

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbline)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
