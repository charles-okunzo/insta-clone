# Generated by Django 4.0.5 on 2022-06-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0007_remove_post_comments_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followers',
            new_name='followed',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='follower',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
