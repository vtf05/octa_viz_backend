# Generated by Django 3.2.7 on 2022-03-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replication_mech', '0005_alter_status_type_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='type_of',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
