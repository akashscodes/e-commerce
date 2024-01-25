from django.shortcuts import render


def register(request):
    return render(request=request, template_name='account/register.html')
