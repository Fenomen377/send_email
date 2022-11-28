from django.conf.urls import url

from main.views import FollowerView

urlpatterns = [
    url('', FollowerView.as_view(), name='follower')
]
