from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DetailsForm
import requests
import json


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password'])

            # test url

            url = 'https://api.taiga.io/api/v1/auth'
            payload = '{\n        "password": "Youshallnotpass789",\n        "type": "normal",\n        "username": "rajukoushik"\n    }'
            headers = {'content-type': 'application/json'}

            r = requests.post(url, data=payload, headers=headers)

            #print (r.content)
            token = json.loads(r.content)
            print(token['auth_token'])

            url = 'https://api.taiga.io/api/v1/projects/by_slug?slug=truptikhatavkar-byte_me'
            payload = '{\n        Authorization:eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjozMjEyNzN9:1gHPxX:-C5UBh5DNPkX2EofAMlwGXMgh34\n    }'
            headers = {'content-type': 'application/json'}

            r = requests.get(url, data=payload, headers=headers)

            #print(r.content)

            data = json.loads(r.content)
            members = data['members']

            member_list = []
            for x in members:
                print(x['full_name'])
                member_list.append(x['full_name'])

            print (member_list)

            sprints = data['milestones']

            sprint_list = []
            for x in members:
                print(x['name'])
                sprint_list.append(x['name'])

            print (sprint_list)







            # test url end


            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DetailsForm()

    return render(request, 'api/login.html', {'form': form})
