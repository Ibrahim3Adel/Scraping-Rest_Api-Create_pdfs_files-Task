# Generated by Django 3.2.9 on 2021-11-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0002_rename_novel_novel_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel_auth',
            name='Pdf_File_Path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
