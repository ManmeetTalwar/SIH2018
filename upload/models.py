from django.db import models
from django.contrib.auth.models import User
import hashlib as hasher
# Create your models here.
class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    datestamp = models.DateTimeField()
    language = models.CharField(max_length=255)
   
class BlockModel(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    previous_hash = models.CharField(max_length=256)
    block_hash = models.CharField(max_length=256)
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(self.text.encode('utf-8') + self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

