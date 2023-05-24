from django.urls import path, include

from . import views
urlpatterns = [
    path('one',views.one),
    path('two',views.two),
    path('tre',views.tre),
    path('man',views.man),
    path('form',views.form),
    path('post',views.post),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]