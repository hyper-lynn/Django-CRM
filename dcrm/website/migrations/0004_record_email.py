# Generated by Django 4.2.3 on 2023-07-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_record_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]