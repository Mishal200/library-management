from django.urls import path
from . import views

urlpatterns = [

    path('', views.book_list, name='book_list'),

    path('book/<int:id>/', views.book_detail, name='book_detail'),

    path('issue/<int:book_id>/', views.issue_book, name='issue_book'),

    path('categories/', views.categories, name='categories'),

   path('wishlist/',views.wishlist,name='wishlist'),

    path('wishlist/add/<int:book_id>/',views.add_to_wishlist,name='add_to_wishlist'),

    path('wishlist/remove/<int:book_id>/',views.remove_from_wishlist,name='remove_from_wishlist'),

    path('profile/', views.profile, name='profile'),

    path('drama/', views.drama_books, name='drama'),

    path('romance/',views.romance_books,name='romance'),

   path('history/',views.history_books,name='history'),

    path('self-help/', views.self_help_books, name='self_help'),

    path('login/',views.login_view,name='login'),

]