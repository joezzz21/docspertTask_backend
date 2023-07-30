from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('books/', views.getBooks),  # of a certain author  #updated
    path('allbooks/', views.getAllBooks),
    path('book/<int:id>', views.getBook),
    path('createbook/', views.createBook),
    path('editbook/<int:id>', views.editBook),
    path('deletebook/<int:id>', views.deleteBook),

    path('pages/<int:id>', views.getAllPages),
    path('createpage/<int:id>', views.createPage),
    path('editpage/<int:id>', views.editPage),
    path('deletepage/<int:id>', views.deletePage),

    path('createuser/', views.createUser),
    path('testtoken/', views.testToken),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
