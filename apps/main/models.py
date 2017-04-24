from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ordered_model.models import OrderedModel
from django.utils.text import slugify
from photologue.models import Photo

WEBPAGE = 0
GAME = 1
OTHER = 3
PROJECT_TYPES = ((WEBPAGE, 'Webpage'), (GAME, 'Game'), (OTHER, 'Other'))


class OrderedModelEx(OrderedModel):
    def human_order(self):
        return self.order + 1

    human_order.short_description = _('Order')


class MenuItem(OrderedModelEx):
    STANDARD = 0
    GALLERY = 1
    TYPES = (
        (STANDARD, 'Standard'),
        (GALLERY, 'Gallery'),
    )

    title = models.CharField(_("Title"), max_length=50, null=False, blank=False)
    content = RichTextField(_("Content"), null=False, blank=True)
    type = models.SmallIntegerField(_("Tab type"), choices=TYPES, default=STANDARD)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)

    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
        ordering = ['order']


class Technology(models.Model):
    name = models.CharField(max_length=100)
    _icon_url = models.URLField()
    icon = models.ImageField(blank=True, null=True, upload_to='tech')

    @property
    def icon_url(self):
        try:
            if self.icon.file:
                return self.icon.url
        except:
            pass
        return self._icon_url

    class Meta:
        verbose_name_plural = "Technologies"


class Project(OrderedModelEx):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100)
    repository = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = RichTextField(null=False, blank=True)
    images = models.ManyToManyField(Photo, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    type = models.PositiveSmallIntegerField(choices=PROJECT_TYPES)
