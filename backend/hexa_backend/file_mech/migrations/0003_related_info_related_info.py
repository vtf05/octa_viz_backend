# Generated by Django 3.2.7 on 2022-03-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_mech', '0002_auto_20220325_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='related_info',
            name='related_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
