from django.contrib.auth.models import User
from django.db import models

class TestCaseStatus(models.Model):
    name=models.CharField(max_length=50)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    project_manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    target_date = models.DateField

class TestCase(models.Model):
    title = models.CharField(max_length=50)
    reproduce_step = models.CharField(max_length=1000)
    priority = models.IntegerField
    created_date = models.DateTimeField
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(TestCaseStatus, on_delete=models.DO_NOTHING)