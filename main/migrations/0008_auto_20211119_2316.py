# Generated by Django 3.2.9 on 2021-11-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_title_certificate_issuer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='date',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='certificate',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]