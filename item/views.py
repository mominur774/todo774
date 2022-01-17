from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import PlanForm
from .models import Plan


# Create your views here.


def addPlanView(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plan added!')
            form = PlanForm()
        else:
            return HttpResponse('Correct your form data.')
    else:
        form = PlanForm()

    plans = Plan.objects.all()

    context = {
        'form': form,
        'plans': plans
    }
    return render(request, 'todo/addplan.html', context)


def updatePlanView(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    if request.method == 'POST':
        # plan = Plan.objects.get(slug=plans)
        form = PlanForm(data=request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plan updated!')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Correct your form data.')
    else:
        # plan = Plan.objects.get(slug=plans)
        form = PlanForm(instance=plan)

    context = {
        'form': form
    }
    return render(request, 'todo/updateplan.html', context)


def deletePlanView(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    return HttpResponseRedirect('/')
