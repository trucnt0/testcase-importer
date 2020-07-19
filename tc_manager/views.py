from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import Project, TestCaseStatus, TestCase

def index(request):
    projects = Project.objects.all()
    assignees = User.objects.all()
    test_cases = TestCase.objects.all()
    status = TestCaseStatus.objects.all()
    model = {
        "projects": projects,
        "assignees": assignees,
        "test_cases": test_cases,
        "status": status
    }

    return render(request, 'tc/index.html', model)

def create(request):
    if request.method == "POST":
        new_testcase = {
            "title": request.POST.get('title'),
            "steps": request.POST.get('steps'),
            "project_id": request.POST.get("projectID"),
            "assignee_id": request.POST.get("assigneeID"),
            "priority": 1
        }
        create_test_case(new_testcase)

    return redirect('/')

def create_test_case(model):
    assignee = User.objects.get(pk=model['assignee_id'])
    project = Project.objects.get(pk=model['project_id'])
    
    tc = TestCase()
    tc.title = model['title']
    tc.reproduce_step = model['steps']
    tc.priority = 1
    tc.created_date = now()
    tc.assignee = assignee
    tc.project = project
    tc.status = TestCaseStatus.objects.filter(pk=1).get()
    tc.save()