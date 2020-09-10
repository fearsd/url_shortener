from django.db import models
from hashlib import blake2b

class URL(models.Model):
    # id = models.BigIntegerField(primary_key=True, blank=True)
    exact_url = models.URLField()
    hash_slug = models.CharField(max_length=6, blank=True)

    def save(self, *args, **kwargs):
        self.hash_slug = blake2b(self.exact_url.encode('utf-8'), digest_size=6).hexdigest()
        super(URL, self).save(*args, **kwargs)