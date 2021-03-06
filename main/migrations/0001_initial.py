# Generated by Django 3.2.9 on 2021-11-13 22:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='Autor')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('message', models.TextField(verbose_name='Mensagem')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_image', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Mídia',
                'verbose_name_plural': 'Mídias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Portfólio',
                'verbose_name_plural': 'Portfólios',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nome')),
                ('score', models.IntegerField(blank=True, default=80, null=True, verbose_name='Nível')),
                ('image', models.FileField(blank=True, null=True, upload_to='skills')),
                ('is_key_skill', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='testimonials')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.CharField(blank=True, max_length=200, null=True)),
                ('quote', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('skills', models.ManyToManyField(blank=True, to='main.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuário',
                'verbose_name_plural': 'Perfís de usuários',
            },
        ),
    ]
