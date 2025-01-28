from django.db import models
from django.contrib.auth import get_user_model
from blogs.models.tags_model import Tag
from django.utils.timezone import now
from django.utils.text import slugify

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=60,unique=True)
    banner = models.ImageField(upload_to='images/',default="images/Default_banner.jpg",blank=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    publishable = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,related_name='blogs')
    categories = models.ManyToManyField('Category',related_name='blogs')
    slug = models.SlugField(max_length=60,unique=True)
    published_date = models.DateTimeField(default=now,blank=False)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

