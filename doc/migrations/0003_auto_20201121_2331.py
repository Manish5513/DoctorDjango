# Generated by Django 3.1.3 on 2020-11-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_patient_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Service',
            field=models.CharField(max_length=20),
        ),
    ]
