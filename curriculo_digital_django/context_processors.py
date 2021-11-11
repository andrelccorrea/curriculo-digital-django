from django.contrib.auth.models import User


def project_context(request):

    context = {
        'eu': User.objects.first()
    }

    return context
