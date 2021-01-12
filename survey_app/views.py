from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def process_survey(request):
    print("Getting Post info...")
    print(request.POST)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['location'] = request.POST['location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comments'] = request.POST['comments']
    request.session['ref'] = request.POST.get('ref', False)

    comm_opt= []
    for val in request.POST:
        if request.POST[val] == "on":
            comm_opt.append(val)
    
    request.session['comm_options'] = comm_opt
    print(request.session)
    return redirect('/results')


def results(request):
    return render(request, 'results.html')


def render_time(request):
    context = {
        "time": strftime("%A, %B %d, %Y %H:%M:%S %p", localtime())
    }
    print(context)
    return render(request, "index.html", context)