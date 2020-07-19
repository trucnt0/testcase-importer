import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core import serializers
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
        "status": status,
        "priorities": [1,2,3,4,5,6,7,8,9]
    }

    return render(request, 'tc/index.html', model)

def get(request, testcase_id):
    result = TestCase.objects.filter(pk=testcase_id) 
    response = serializers.serialize("json", result)
    return HttpResponse(response, content_type="application/json")

def save(request):
    if request.method == "POST":
        testcase = {
            "title": request.POST.get('title'),
            "steps": request.POST.get('steps'),
            "project_id": request.POST.get("projectID"),
            "assignee_id": request.POST.get("assigneeID"),
            "status_id": request.POST.get('statusID'),
            "priority": request.POST.get('priority')
        }

        action = request.POST.get('action')
        
        if action == 'edit':
            id = request.POST.get('testcaseID')
            edit_test_case(id, testcase)
        elif action == 'add':
            create_test_case(testcase)
        
    return redirect('/')

def edit_test_case(id, model):
    print('Editing testcase',id)
    assignee = User.objects.get(pk=model['assignee_id'])
    project = Project.objects.get(pk=model['project_id'])
    status = TestCaseStatus.objects.get(pk=model['status_id'])

    tc = TestCase.objects.filter(pk=id).first()
    tc.title = model['title']
    tc.reproduce_step = model['steps']
    tc.assignee = assignee
    tc.project = project
    tc.status = status
    tc.priority = model['priority']
    tc.save()

def create_test_case(model):
    print('Create new testcase')
    assignee = User.objects.get(pk=model['assignee_id'])
    project = Project.objects.get(pk=model['project_id'])
    status = TestCaseStatus.objects.filter(pk=1).get()
    
    tc = TestCase()
    tc.title = model['title']
    tc.reproduce_step = model['steps']
    tc.priority = 1
    tc.created_date = now()
    tc.assignee = assignee
    tc.project = project
    tc.status = status
    tc.save()