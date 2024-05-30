from .models import Favorite_place, Contact
from django.forms import ModelForm, Textarea


class Favorite_placeForm(ModelForm):

    class Meta:
        # Названием модели на основе которой
        # нужно создать форму.
        model = Favorite_place
        # Поля модели, которые нужно вывести
        fields = ('user', 'interesting_place')


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }