from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import BookSerializer, PageSerializer, UserSerializer
from base.models import Book, User, Page


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
def getBooks(request, id):
    user = User.objects.get(id=id)
    if user.role == "Author":
        books = user.book_set.all()
    else:
        return Response(status=400, data={"Message": "Can't access"})
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def createBook(request, id):
    user = User.objects.get(id=id)  # needs to be changed
    book = Book.objects.create(
        title=request.data['title'], description=request.data['description'], author=user, authorName=user.name)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['PUT'])
def editBook(request, id):
    # user = User.objects.get(id=1) #needs to be changed
    book = Book.objects.get(
        id=id)
    book.title = request.data['title']
    book.description = request.data['description']
    book.save()
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBook(request, id):
    # user = User.objects.get(id=1) #needs to be changed
    book = Book.objects.get(
        id=id)
    book.delete()
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def createPage(request, id):
    book = Book.objects.get(id=id)
    page = Page.objects.create(book=book, text=request.data['text'])
    serializer = PageSerializer(page)
    return Response(serializer.data)


@api_view(['GET'])
def getAllPages(request, id):
    book = Book.objects.get(id=id)
    pages = book.page_set.all()
    serializer = PageSerializer(pages, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def editPage(request, id):
    # user = User.objects.get(id=1) #needs to be changed
    page = Page.objects.get(
        id=id)
    page.text = request.data['text']
    page.save()
    serializer = PageSerializer(page)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePage(request, id):
    # user = User.objects.get(id=1) #needs to be changed
    page = Page.objects.get(
        id=id)
    page.delete()
    serializer = PageSerializer(page)
    return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    user = User.objects.create(
        username=request.data['username'], password=request.data['password'], role=request.data['role'], name=request.data['name'])
    serializer = UserSerializer(user)
    return Response(serializer.data)
