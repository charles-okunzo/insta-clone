# Generated by Django 4.0.5 on 2022-06-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]