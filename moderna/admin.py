from django.contrib import admin
from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import  TabularDynamicInlineAdmin
from mezzanine.forms.admin import FormAdmin

from .models import Contact, Slide, IconBlurb, HomePage, Portfolio, BoardMembers, Works, AboutPage
# Register your models here.

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbline(TabularDynamicInlineAdmin):
    model = IconBlurb

class Membersline(TabularDynamicInlineAdmin):
    model = BoardMembers

class Worksline(TabularDynamicInlineAdmin):
    model = Works

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbline)
    
class AboutPageAdmin(PageAdmin):
    inlines = (Membersline, Worksline)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)

