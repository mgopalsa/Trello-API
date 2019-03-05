from django.urls import path, re_path
from . import views
from rest_framework.authtoken import views as authviews
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Trello API')
urlpatterns = [
    path('boards/', views.BoardList.as_view()),
    re_path(r'^boards/(?P<pk>[0-9]+)/$', views.BoardDetail.as_view()),
    path('lists/', views.ListList.as_view()),
    re_path(r'^lists/(?P<pk>[0-9]+)/$', views.ListDetail.as_view()),
    path('cards/', views.CardList.as_view()),
    re_path(r'^cards/(?P<pk>[0-9]+)/$', views.CardDetail.as_view()),
    path('labels/', views.LabelList.as_view()),
    re_path(r'^labels/(?P<pk>[0-9]+)/$', views.LabelDetail.as_view()),
    path("users/", views.UserCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="login"),
    path('api-token-auth/', authviews.obtain_auth_token),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Trello API')),
]
