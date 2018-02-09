from django.conf.urls import url
from band_members.views import BandMemberView

urlpatterns = [
    url(r'^$',BandMemberView.as_view())
]