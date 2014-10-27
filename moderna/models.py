from django.db import models

# Create your models here.

from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs", null=True,  blank=True)
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading", null=True,  blank=True)
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works", null=True,  blank=True)
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!", null=True,  blank=True)
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts", null=True,  blank=True)

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")
        
class AboutPage(Page, RichText):
    '''
    A page representing the format of the About page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs", null=True,  blank=True)
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading", null=True,  blank=True)
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works", null=True,  blank=True)
    featured_members_heading = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!", null=True,  blank=True)
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts", null=True,  blank=True)

    class Meta:
        verbose_name = _("About page")
        verbose_name_plural = _("About pages")



class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    boxtitle = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=2000, 
        help_text="Optional, if provided clicking the blurb will go here.", null=True,  blank=True)



class AboutSlide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    aboutpage = models.ForeignKey(AboutPage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    boxtitle = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=2000, 
        help_text="Optional, if provided clicking the blurb will go here.", null=True,  blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255, null=True,  blank=True)
    title = models.CharField(max_length=200, null=True,  blank=True)
    content = models.TextField(null=True)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.", null=True)


class BoardMembers(Orderable):
    '''
    An icon box on a HomePage
    '''
    aboutpage = models.ForeignKey(AboutPage, related_name="members")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255, null=True,  blank=True)
    title = models.CharField(max_length=200, null=True,  blank=True)
    content = models.TextField(null=True)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.", null=True)


class Works(Orderable):
    '''
    An icon box on a HomePage
    '''
    aboutpage = models.ForeignKey(AboutPage, related_name="works")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Work.image", "icons"),
        format="Image", max_length=255, null=True,  blank=True)
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Work.image", "icons"),
        format="Image", max_length=255, null=True,  blank=True)
    title = models.CharField(max_length=200, null=True,  blank=True)
    content = models.TextField(null=True)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.", null=True)

class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

