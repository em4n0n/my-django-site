from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
# These are all properties of each post

    class Meta:
        ordering = ['-created']

        def __str__(self):
            return self.title
        
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

