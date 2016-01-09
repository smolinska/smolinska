import json

from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView
from photologue.models import Gallery

from apps.main.extra_logic import parse_SCSS_variables, find_custom_template
from apps.main.models import MenuItem


class MainView(TemplateView):
    template_name = 'index.html'
    scss_vars = parse_SCSS_variables()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tab_types = dict(filter(lambda x: str.isupper(x[0]), MenuItem.__dict__.items()))
        tab_urls = {
            MenuItem.GALLERY: reverse('gallery')
        }
        self.js_vars = {
            'SCSS_VARS': json.dumps(self.scss_vars),
            'TAB_TYPES': json.dumps(tab_types),
            'TAB_URLS': json.dumps(tab_urls),
        }

        self.tabs = MenuItem.objects.all()
        # TODO: This is fragile when client will change tab name
        self.tabs = list(map(find_custom_template, list(self.tabs)))

    def get(self, request, *args, **kwargs):
        context = {
            "tabs": self.tabs,
            "analytics_id": settings.GOOGLE_ANALYTICS_ID,
            "production": not settings.DEBUG,
            "js_vars": self.js_vars,
        }

        return self.render_to_response(context)


class GalleryView(TemplateView):
    template_name = 'gallery.html'
    MAX_PHOTOS_IN_ROW = 3
    MAX_GALERIES_IN_ROW = 3
    full_row_gallery_width = 12 // MAX_GALERIES_IN_ROW

    def get_col_width(self, i, count):
        cls = 'col-md-{}'
        galeries_in_last_row = count % self.MAX_GALERIES_IN_ROW
        rev = count - i
        if rev <= galeries_in_last_row:
            return cls.format(12 // galeries_in_last_row)
        else:
            return cls.format(self.full_row_gallery_width)

    def get(self, request, *args, **kwargs):
        galleries = Gallery.objects.is_public().prefetch_related('photos').order_by('-date_added')
        count = galleries.count()

        galleries = [{
                         'id': gallery.id,
                         'title': gallery.title,
                         'desc': gallery.description,
                         'images': gallery.public(),
                         'col_class': self.get_col_width(i, count),
                     } for i, gallery in enumerate(galleries)]

        return self.render_to_response({
            'galleries': galleries,
            'in_row': self.MAX_GALERIES_IN_ROW,
            'MAX_PHOTOS_IN_ROW': self.MAX_PHOTOS_IN_ROW,
        })
