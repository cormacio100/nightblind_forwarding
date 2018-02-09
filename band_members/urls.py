from django.conf.urls import url
from band_members.views import BandMemberView

urlpatterns = [
    url(r'^$',BandMemberView.as_view()),
    url(r'(?P<pk>[0-9]+)/$',BandMemberView.as_view())   #   url to pass values to the PUT method by <pk>
]