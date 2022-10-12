from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [

    path("associates/", AssociateAPI.as_view(), name="associates"),
    path("associates/<int:pk>/", AssociateAPI.as_view(), name="associatesParameters"),

    path("machines/", MachineAPI.as_view(), name="machines"),
    path("machines/<int:pk>/", MachineAPI.as_view(), name="machinesParameters"),

    path("questions/", QuestionAPI.as_view(), name="questions"),
    path("questions/<int:pk>/", QuestionAPI.as_view(), name="questionsParameters"),

    path("greenbooks/", GreenBookAPI.as_view(), name="greenbooks"),
    path("greenbooks/<int:pk>/<int:tq>/", GreenBookAPI.as_view(), name="greenbooksParameters"),

    path("maintenances/", MaintenanceAPI.as_view(), name="maintenances"),
    path("maintenances/<int:pk>/", MaintenanceAPI.as_view(), name="maintenancesParameters"),

    path("releasemachines/", ReleaseMachineAPI.as_view(), name="releasemachines"),
    path("releasemachines/<int:pk>/", ReleaseMachineAPI.as_view(), name="releasemachinesParameters"),
    path("getreleasemachines/", GetReleaseMachineAPI.as_view(), name="releasemachines"),

    path("observations/", ObservationAPI.as_view(), name="observations"),
    path("observations/<int:pk>/", ObservationAPI.as_view(), name="observationsParameters"),

    path("maintenanceorders/", MaintenanceAPI.as_view(), name="maintenanceorders"),
    path("maintenanceorders/<int:pk>/", MaintenanceAPI.as_view(), name="maintenanceordersParameters"),

    path("areas/", AreaAPI.as_view(), name="areas"),
    path("areas/<int:pk>/", AreaAPI.as_view(), name="areasParameters"),

    path("requestLogins/", LoginAPI.as_view(), name="requestLogins"),
    path("requestLogins/<int:pk>/", LoginAPI.as_view(), name="requestLoginsParameters"),

]