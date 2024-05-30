from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('answer/', views.answer, name='answer'),
    path('contact/', views.ContactCreate.as_view(), name='contact_page'),
    path('success/', views.success, name='success_page'),
    path('favourites_routes/<int:id>/', views.favourites_routes, name='favourites_routes'),
    path('favourites/<int:id>/', views.favourites, name='favourites'),
     # Детальная страница интересного места
    path('interesting_places/<id>/', views.interesting_places_detail, name = 'interesting_places_detail'),
    # Детальная страница маршрута
    path('weekends_routes/<id>/', views.weekends_routes_detail, name = 'weekends_routes_detail'),
    # Страница с маршрутами
    path('weekends_routes/', views.weekends_routes_list, name = 'weekends_routes_list'),
    # Список интересных мест
    path('interesting_places/', views.interesting_places_list, name = 'interesting_places_list'),
    # Страница с картой
    path('route_map/', views.route_map, name = 'route_map'),
    # Главная страница
    path('', views.index, name = 'index'),
    path('about/', views.AboutPage.as_view(), name = 'about'),
    path('profile/<str:username>/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # чтобы картинки могли найтись и отобразиться