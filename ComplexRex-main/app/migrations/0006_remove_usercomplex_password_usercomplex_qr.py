# Generated by Django 4.0.2 on 2022-04-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_user_usercomplex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomplex',
            name='password',
        ),
        migrations.AddField(
            model_name='usercomplex',
            name='QR',
            field=models.ImageField(blank=True, upload_to='static/app/QRS'),
        ),
    ]
