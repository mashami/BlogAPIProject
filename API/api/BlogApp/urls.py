from django.urls import path

from rest import views

urlpatterns = [
    # path('articles/',views.Articles_list),
    #  path('articles/',views.ArticleAPIView.as_view()),
    # # path('articles/<int:pk>/',views.Article_details),
    # path('articles/<int:id>/',views.Details.as_view()),
    path('articles/generic',views.GenericAPIView.as_view()),
    path('articles/generic/<int:id>',views.GenericAPIViewDetails.as_view()),
]