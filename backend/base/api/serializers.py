from rest_framework.serializers import ModelSerializer
from base.models import Book, Page, User


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
