# Generated by Django 4.0.5 on 2022-06-16 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_skill_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='soft_skills',
            field=models.ManyToManyField(blank=True, to='main.softskill'),
        ),
    ]
