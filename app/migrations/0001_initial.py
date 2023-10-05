# Generated by Django 3.1.4 on 2023-09-11 19:59

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gridModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cols', models.IntegerField(default=4)),
                ('first_col', models.IntegerField(default=8)),
                ('strip_request', models.CharField(default='A08-T08,A09-T09', max_length=1000)),
                ('graph_types', models.CharField(default='d', max_length=1000)),
                ('img_test', models.FileField(upload_to=app.models.fileFormat, validators=[django.core.validators.validate_image_file_extension])),
                ('img_test_crop', models.ImageField(default='/Users/Tom/Python_Projects/pep_genie/app/dummy.png', null=True, upload_to=app.models.fileFormat)),
                ('img_test_coords', models.CharField(default='empty', max_length=200)),
                ('img_test_csv', models.FileField(upload_to=app.models.fileFormat)),
                ('img_con', models.FileField(upload_to=app.models.fileFormat)),
                ('img_con_crop', models.ImageField(default='/Users/Tom/Python_Projects/pep_genie/app/dummy.png', null=True, upload_to=app.models.fileFormat)),
                ('img_con_coords', models.CharField(default='empty', max_length=200)),
                ('img_con_csv', models.FileField(upload_to=app.models.fileFormat)),
                ('img_vis_crop', models.ImageField(default='/Users/Tom/Python_Projects/pep_genie/app/dummy.png', null=True, upload_to=app.models.fileFormat)),
                ('img_vis', models.FileField(upload_to=app.models.fileFormat)),
                ('img_vis_coords', models.CharField(default='empty', max_length=200)),
                ('img_vis_csv', models.FileField(upload_to=app.models.fileFormat)),
                ('user_id', models.CharField(max_length=100)),
                ('ppt_path', models.CharField(max_length=100)),
                ('full_grid', models.ImageField(default='/Users/Tom/Python_Projects/pep_genie/app/dummy.png', upload_to=app.models.fileFormat)),
                ('dens_list', models.CharField(default='null', max_length=1000)),
                ('config', models.CharField(default="{'c':0}", max_length=1000)),
                ('normalised_csv', models.FileField(upload_to=app.models.fileFormat)),
            ],
        ),
    ]
