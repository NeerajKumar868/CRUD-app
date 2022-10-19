from django.urls import path
from.views import *

urlpatterns=[
    path("home",home),
    path("save",save),
    path("delete/<int:empID>",delete),
    path("deleteAll",deleteAll),
    path("Edit/<int:empID>",Edit),
    path("update",update),
    path("sortname",sortname),
    path("searchname",searchname),
    
]