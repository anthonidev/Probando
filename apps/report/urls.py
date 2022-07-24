from django.urls import path

from apps.report.views import ReportView

app_name = "report"
urlpatterns = [
    path('', ReportView.as_view()),
]