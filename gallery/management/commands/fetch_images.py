from django.core.management.base import BaseCommand
from gallery.models import Image
from firebase_admin import storage
from datetime import timedelta

class Command(BaseCommand):
    help = 'Fetch images from Firebase and store their URLs'

    def handle(self, *args, **kwargs):
        bucket = storage.bucket()
        blobs = bucket.list_blobs()
        image_count = 0

        for blob in blobs:
            if blob.content_type and blob.content_type.startswith('image/'):
                image_url = blob.generate_signed_url(timedelta(seconds=300), method='GET')
                Image.objects.get_or_create(title=blob.name, image_url=image_url)
          
                image_count += 1



        self.stdout.write(self.style.SUCCESS(f'Successfully fetched and stored {image_count} image URLs'))
