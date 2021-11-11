from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):

    name = models.CharField(verbose_name='Nome',
                            max_length=20, blank=True, null=True)
    score = models.IntegerField(
        verbose_name='Nível', default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    class Meta:
        verbose_name = 'Perfil de usuário'
        verbose_name_plural = 'Perfis de usuário'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField(verbose_name='Mensagem')

    class Meta:
        verbose_name = 'Perfil de contato'
        verbose_name_plural = 'Perfis de contato'
        ordering = ['timestamp']

    def __str__(self) -> str:
        return f'{self.name}'


class Testimonial(models.Model)


17: 30
