# Generated by Django 3.0.5 on 2020-04-12 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'location',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PostServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=100, verbose_name='<font size="3.5"><b>Enter Services Title:</b></font> <br> (Hint: Usman Ahmad as a Web Developer) ')),
                ('skills_description', models.TextField(verbose_name='<font size="3.5"><b>Enter Skills/Work Description</b></font> ')),
                ('enter_price', models.TextField(verbose_name='<font size="3.5"><b>Enter Prices :- </b></font><br> Related with Skills/Work/Product <br>(Hint: Logo Design Price = 1000Rs/$) etc')),
                ('phone', models.IntegerField(verbose_name='<font size="3.5"><b>Enter Contact No.</b></font><br>(Hint: 03xx xxxxxxx)')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category_posted', models.BooleanField(default=True)),
                ('select_image', models.ImageField(default='default.jpg', upload_to='post-services', verbose_name='<font size="3.5"><b>Select Image (Optional)</b></font>')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubiquityOSI.Area', verbose_name='<font size="3.5"><b>Select Area Below:</b></font>')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='ubiquityOSI.Category', verbose_name='<font size="3.5"><b>Select Category Below:</b></font> ')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubiquityOSI.Location', verbose_name='<font size="3.5"><b>Select Location Below:</b></font>')),
            ],
        ),
    ]
