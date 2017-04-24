import random
from collections import namedtuple
from io import BytesIO
from urllib.request import urlopen

from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from photologue.models import Gallery, Photo

Size = namedtuple('Size', ['x', 'y'])


class Command(BaseCommand):
    help = 'Fetches random images and inits some galeries'
    image_sizes = [Size(400 + 100 * x, 200 + 200 * x) for x in range(1, 8)]

    def yes_no(self, question):
        yes = {'yes', 'y', 'ye', ''}
        no = {'no', 'n'}

        choice = input(question).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            self.stdout.write(self.style.ERROR("Please respond with 'yes' or 'no'"))
            return self.yes_no(question)

    def handle(self, *args, **options):
        if Gallery.objects.exists() and not self.yes_no('There are galleries in db, remove all?'):
            self.stdout.write(self.style.SUCCESS('Done nothing'))
            exit(0)
        else:
            Gallery.objects.all().delete()
            Photo.objects.all().delete()
        for i in range(5):
            g_name = 'Test gallery {}'.format(i)
            gallery = Gallery(title=g_name, slug=slugify(g_name))
            gallery.save()
            for j in range(random.randrange(4, 7, 2)):
                size = random.choice(self.image_sizes)
                url = 'http://lorempixel.com/{}/{}/'.format(size.x, size.y)
                result = urlopen(url)
                self.stdout.write('.', ending='')
                self.stdout.flush()
                slug = '{}x{}_p{}_g{}'.format(size.x, size.y, j, i)
                name = 'test{}.jpg'.format(slug)
                photo = Photo(title=slug, slug=slug)
                io = BytesIO(result.read())
                photo.image.save(name, File(io))
                photo.save()
                gallery.photos.add(photo)
            gallery.save()
            self.stdout.write('|', ending='')
            self.stdout.flush()

        self.stdout.write(self.style.SUCCESS('\nSuccessfully initialized galeries'))
