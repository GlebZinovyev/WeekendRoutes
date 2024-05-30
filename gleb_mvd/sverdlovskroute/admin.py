from django.contrib import admin
from .models import Weekend_rout, Interesting_place, Contact
from django.core.mail import send_mail


class Weekend_routAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'description', 'location') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('location',)
    empty_value_display = '-пусто-' 


class Interesting_placeAdmin(admin.ModelAdmin):
 # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'description', 'location') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('location',)
    empty_value_display = '-пусто-' 



# Функция отправки сообщения
def email(subject, content, email):
   send_mail(
    'Тема письма',
    content,
    '1@1.ru',  # Это поле "От кого" здесь от админа
    [email],  # Это поле "Кому" (можно указать список адресов) здесь email отправителя обратной связи
    fail_silently=False, # Сообщать об ошибках («молчать ли об ошибках?»)
)


class ContactAdmin(admin.ModelAdmin):
    actions = ["make_answer"]
    @admin.action(description="make_answer")
    def make_answer(self, request, queryset):
        a = []
        for obj in queryset:
            query = obj
        subject = f'Сообщение с формы от {admin.__name__} Почта отправителя: {"1@1.ru"}'
        quer = str(query).split('*')
        email(subject, quer[1], quer[0])


admin.site.register(Weekend_rout, Weekend_routAdmin) 
admin.site.register(Interesting_place, Interesting_placeAdmin) 
admin.site.register(Contact, ContactAdmin)