from django.contrib import admin
from .models import Project, TestCase, TestCaseStatus

admin.site.register(Project)
admin.site.register(TestCaseStatus)
admin.site.register(TestCase)