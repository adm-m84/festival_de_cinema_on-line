# Generated by Django 2.2.5 on 2019-09-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realizadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizadormodel',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
