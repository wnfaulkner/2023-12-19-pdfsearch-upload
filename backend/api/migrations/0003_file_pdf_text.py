# Generated by Django 4.1.4 on 2023-12-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_files_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='pdf_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
