from django.contrib import admin
from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
#from mezzanine.forms.models import Form
from mezzanine.core.admin import  TabularDynamicInlineAdmin
from .models import AboutSlide, Slide, IconBlurb,HomePage, Portfolio, BoardMembers, Works, AboutPage
# Register your models here.

class AboutSlideInline(TabularDynamicInlineAdmin):
    model = AboutSlide
    
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
    inlines = (AboutSlideInline, Membersline, Worksline)

#class ContactForm(PageAdmin):
#    inlines = (Contact, Form)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
#admin.site.register(Contact, ContactForm)

