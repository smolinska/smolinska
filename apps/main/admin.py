from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from ordered_model.admin import OrderedModelAdmin
from photologue.admin import PhotoAdmin
from photologue.models import Watermark, PhotoEffect

from apps.main.extra_logic import obfuscate_emails, deobfuscate_emails
from apps.main.models import MenuItem, Project

# disabling redundant auth admin stuff
admin.site.unregister(Group)


class MenuItemAdmin(OrderedModelAdmin):
    list_display = ('title', 'human_order', 'move_up_down_links')

    def save_model(self, request, obj, form, change):
        obj.content = obfuscate_emails(obj.content)
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None:
            obj.content = deobfuscate_emails(obj.content)
        return super(MenuItemAdmin, self).get_form(request, obj, **kwargs)


class ProjectAdmin(OrderedModelAdmin):
    list_display = (
        'order',
        'start_date',
        'end_date',
        'name',
        'description',
        'type',
        'move_up_down_links',
    )
    list_filter = ('start_date', 'end_date')
    raw_id_fields = ('images', 'technologies')
    search_fields = ('name',)


admin.site.register(Project, ProjectAdmin)


admin.site.register(MenuItem, MenuItemAdmin)

admin.site.unregister(Site)

# Overriding Photologue default admin settings
PhotoAdmin.exclude = ('effect',)

# unregistering Photologue admin for unused models
admin.site.unregister(Watermark)
admin.site.unregister(PhotoEffect)

PhotoAdmin.exclude = ('sites',) + PhotoAdmin.exclude
