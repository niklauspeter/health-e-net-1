from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/original/$',views.OriginalList.as_view()),
    url(r'^api/extracts/$',views.ExtractedList.as_view()),
]