'''
The purpose of this is to support compressing statics and pushing them to the S3 bucket

The docs:
 https://django_compressor.readthedocs.org/en/latest/remote-storages/index.html?highlight=s3#using-staticfiles

Helpful stackoverflow for the error I was getting on heroku logs:
 OfflineGenerationError: You have offline compression enabled but key "4fb....7257" is missing from offline manifest.
 You may need to run "python manage.py compress".

 http://stackoverflow.com/questions/20947447/how-to-setup-django-compressor-on-heroku-offline-compression-to-s3
'''
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage


class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class("compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name
