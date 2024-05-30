from django.shortcuts import render, get_object_or_404, redirect
from .models import Weekend_rout, Interesting_place, Favorite_place, Favorite_rout, Contact
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.http import Http404
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

send_mail(
    'Тема письма',
    'Текст письма.',
    'from@example.com',  # Это поле "От кого"
    ['1@1.ru'],  # Это поле "Кому" (можно указать список адресов) Здесь указан админ
    fail_silently=False, # Сообщать об ошибках («молчать ли об ошибках?»)
) 


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'sverdlovskroute/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Маршруты выходного дня по Свердловской области'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)

def interesting_places_detail(request, id):
    interesting_places_detail = Interesting_place.objects.get(pk=id)
    template = 'sverdlovskroute/interesting_places_detail.html'
    title = 'Маршруты выходного дня по Свердловской области'
    is_favourite = False
    
    if interesting_places_detail.favourites.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'title': title,
        'interesting_places_detail': interesting_places_detail,
        'is_favourite': is_favourite,
    }
    return render(request, template, context)

def weekends_routes_detail(request, id):
    weekends_routes_detail = Weekend_rout.objects.get(id=id)
    template = 'sverdlovskroute/weekends_routes_detail.html'
    title = 'Маршруты выходного дня по Свердловской области'
    context = {
        # В словарь можно передать переменную
        'title': title,
        'weekends_routes_detail': weekends_routes_detail,
    }
    return render(request, template, context)

def weekends_routes_list(request):
    weekends_routes_list = Weekend_rout.objects.all()
    # В словаре context отправляем информацию в шаблон
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'sverdlovskroute/weekends_routes_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Маршруты выходного дня по Свердловской области'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        'weekends_routes_list': weekends_routes_list,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)

def interesting_places_list(request):
    interesting_places_list = Interesting_place.objects.all()
    template = 'sverdlovskroute/interesting_places_list.html'
    title = 'Маршруты выходного дня по Свердловской области'
    context = {
        'title': title,
        'interesting_places_list': interesting_places_list,
    }
    return render(request, template, context)

def route_map(request):
    title = 'Маршруты выходного дня по Свердловской области'
    template = 'sverdlovskroute/route_map.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


class AboutPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'sverdlovskroute/about.html' 


def profile(request, username):
    user=request.user
    places = user.favourites.all()
    routes = user.favourites_routes.all()
    context = {
        'places': places,
        'routes': routes
    }
    return render(request, 'sverdlovskroute/profile.html', context)


@login_required
def favourites(request, id):

    place = get_object_or_404(Interesting_place, pk=id)
    try:
        place.favourites.filter(id=request.user.id).exist()
        place.favourites.remove(request.user)
    except:
        place.favourites.add(request.user)
        
    
    return render(request, 'sverdlovskroute/place_favourite_list.html')

def place_favourite_list(request):
    user=request.user
    favourite_place = user.favourites.all()
    
    context = {
        'favourite_place': favourite_place
    }

    return render(request, 'sverdlovskroute/place_favourite_list.html', context)

@login_required
def favourites_routes(request, id):

    route = get_object_or_404(Weekend_rout, pk=id)
    try:
        route.favourites_routes.filter(id=request.user.id).exist()
        route.favourites_routes.remove(request.user)
    except:
        route.favourites_routes.add(request.user)
        route.save()
   
    return render(request, 'sverdlovskroute/route_favourite_list.html')


def route_favourite_list(request):
    user=request.user
    favourite_route = user.favourites_routes.all()
    
    context = {
        'favourite_route': favourite_route
    }

    return render(request, 'sverdlovskroute/route_favourite_list.html', context)


class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'отправитель@gmail.com',
      ['получатель1@gmail.com']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   context = {
        'text': 'Письмо отправлено!'
    }
   return render(request, 'sverdlovskroute/success.html', context)
   #return HttpResponse('Письмо отправлено!')


def answer(request):
    #contact = get_object_or_404(Contact, pk=id)
    template = 'sverdlovskroute/answer.html'
    answer = Contact.objects.filter(user=request.user.id)

    context = {
        'answer': answer
    }
    return render(request, template, context)
