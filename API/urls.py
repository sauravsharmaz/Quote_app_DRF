from django.urls import path
from API import views

urlpatterns = [
    path('quotes',views.QuoteList.as_view()),
    path('quote/<int:pk>',views.Quote_retrieve_update_destroy.as_view()),
]
