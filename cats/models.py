from django.db import models
from django.template.defaultfilters import slugify

class Student(models.Model):
    DEFAULT_MAX_LEN = 128
    forename = models.CharField(max_length=DEFAULT_MAX_LEN)
    surname = models.CharField(max_length=DEFAULT_MAX_LEN)
    numCats = models.IntegerField(default=0)
    
    def __str__(self):
        return self.forename + " " + self.surname
    
class Cat(models.Model):
    DEFAULT_MAX_LEN = 128
    name = models.CharField(max_length=DEFAULT_MAX_LEN)
    age = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    cat_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        nameSlug = slugify(self.name)
        ownerSlug = slugify(self.owner.forename)
        self.cat_slug = nameSlug + "_" + ownerSlug
        super(Cat, self).save(*args, **kwargs)

    def __str__(self):
        return self.name