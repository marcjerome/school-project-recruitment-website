from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Membership
from .forms import MembershipForm
from json import load as json_load, dumps as json_dump

# Create your views here.
def home(request):
    projects = Project.get_all()

    return render(request, 'groupprojects/home.html', {'projects': projects})

def notification(request):
        notifications = request.user.notifications.all()

        data = {
            "notification_count": str(notifications.count()),  
        }

        return HttpResponse(json_dump(data))

def access(request):

    '''
    method for accessing a project that is secured with an access code
    status_code 0: the access code input is invalid
    status_code 1: the access code is valid and will no longer be asked for an access 
                   code in a span of time. 
    status_code 2: no access code is entered, this will trigger a modal in the website for the 
                   user to enter an access coded
    '''

    status_code = 0
    text = "Invalid Access Code"

    response_data = {
        "status_code": status_code,
        "text": text,
    }

    if request.method == 'POST':
        data = json_load(request)
        project_slug = data.get('project-slug', None) 
        access_code = data.get('access-code', None)

        if project_slug in request.session:
            response_data["status_code"] = 1
            return HttpResponse(json_dump(response_data))

        if access_code is not None:
            project = get_object_or_404(Project, slug=project_slug)

            if project.access_code == access_code:
                response_data["status_code"] = 1
                response_data["text"] = 'Access Code Valid'
                request.session[project_slug] = True
                return HttpResponse(json_dump(response_data))
            return HttpResponse(json_dump(response_data))
        response_data["status_code"] = 2
        return HttpResponse(json_dump(response_data))
    return redirect('home')


def proposal(request, the_slug):
    proposal_text = None

    if the_slug in request.session:

        project = get_object_or_404(Project, slug=the_slug)
        membership = Membership()
        member = membership.get_member(user=request.user, project=project) 

        if project.is_completed:
            return redirect('home')

        elif member is not None:
            proposal_text = member.proposal_text
            form = MembershipForm(request.POST or None, instance=member)
            
            if request.POST.get('delete'):
                member.delete()
                form = MembershipForm(initial={'user': request.user, 'project': project})
                proposal_text = None 

            elif form.is_valid():
                form.save()
                proposal_text = form.cleaned_data['proposal_text']
                
        else:
            form = MembershipForm(request.POST or None, initial={'user': request.user, 'project': project})
            print('waka')
            if form.is_valid():
                print('save')
                form.save()
                proposal_text = form.cleaned_data['proposal_text']

        context = {
            'project': project,
            'slug': the_slug,
            'form': form,
            'proposal_text': proposal_text,
        }

        return render(request, 'groupprojects/proposal.html', context)

    return redirect('home')

