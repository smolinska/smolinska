from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ordered_model.models import OrderedModel
from django.utils.text import slugify


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
