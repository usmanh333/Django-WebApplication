from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'location'

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'area'
        verbose_name_plural = 'areas'

    def __str__(self):
        return self.name


class PostServices(models.Model):
    service_title = models.CharField(max_length=100, verbose_name='<font size="3.5"><b>Enter Services Title:'
                                                                  '</b></font> <br>'
                                                                  ' (Hint: Usman Ahmad as a Web Developer) ')
    skills_description = models.TextField(verbose_name='<font size="3.5"><b>Enter Skills/Work Description</b></font> ')
    enter_price = models.TextField(verbose_name='<font size="3.5"><b>Enter Prices :- </b></font><br>'
                                                ' Related with Skills/Work/Product <br>'
                                                '(Hint: Logo Design Price = 1000Rs/$) etc')
    phone = models.IntegerField(verbose_name='<font size="3.5"><b>Enter Contact No.</b></font>'
                                                '<br>(Hint: 03xx xxxxxxx)')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='<font size="3.5"><b>Select Category Below:</b></font> ')
    location = models.ForeignKey(Location, verbose_name= '<font size="3.5"><b>Select Location Below:</b></font>', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, verbose_name= '<font size="3.5"><b>Select Area Below:</b></font> <br> (Select Area Nearest to your Location [Select Carefully])', on_delete=models.CASCADE)
    category_posted = models.BooleanField(default=True)
    select_image = models.ImageField(default='default.jpg', upload_to='post-services',
                                     verbose_name='<font size="3.5"><b>Select Image (Optional)</b></font>')

    def save(self, *args, **kwargs):
        super(PostServices, self).save(*args, **kwargs)

        img = Image.open(self.select_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.select_image.path)

    def __str__(self):
        return f' {self.author} (Posted Services)'

    def get_absolute_url(self):
        return reverse('post-services')
