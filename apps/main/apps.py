from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class MainConfig(AppConfig):
    name = 'apps.main'
    verbose_name = _("Website Manager")

    def ready(self):
        super().ready()
        if settings.DEBUG:
            # monkey patch, prevents django compressor from adding hash to compiled coffe/scss
            import compressor.base as cb
            cb.get_hexdigest = lambda x, y='': 'compiled'
