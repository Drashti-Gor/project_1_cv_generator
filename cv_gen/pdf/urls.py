from . import views
from django.urls import path

app_name = 'pdf'

urlpatterns = [
    path("",views.home,name="home"),
    path("accept/",views.accept,name="accept"),
    path("<int:id>/",views.resume,name="resume"),
    path("list/",views.list,name="list"),
    path("delete/<int:id>/", views.delete_resume, name = 'delete_resume'),
    path("gen_summary/<skill_list>/<int:n>/", views.generate_summary, name = 'gen_summary')
]