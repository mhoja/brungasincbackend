# Generated by Django 3.2.6 on 2021-08-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brungasinc_app', '0003_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
