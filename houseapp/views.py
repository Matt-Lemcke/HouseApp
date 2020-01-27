from django.utils import timezone

from .models import Task, House, Membership, Message, Notification
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, RedirectView, TemplateView
from datetime import date

def house(request):
    return render(request, 'houseapp/house_settings.html')


def tasks(request):
    content = {
        'tasks': Task.objects.all()
    }
    return render(request, 'houseapp/tasks.html', content)

# def addnote(request):
#     return render(request, 'houseapp/addnot.html')

def notifications(request):
    content = {
        'notification': Notification.objects.all()
    }
    return render(request, 'houseapp/home.html', content)


def calendar(request):
    return render(request, 'houseapp/calendar.html')


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('splash')

    try:
        user_house = Membership.objects.get(person=request.user).house

        #print(Notification.objects.all())

        context = {
            'tasks': Task.objects.filter(user__in=user_house.members.all()),
            #'notifications': Notification.objects.filter(house_=user_house),
            'messages': Message.objects.filter(author__in=user_house.members.all())
        }
        ##################################################################################################################

        if request.method == 'POST':
            content = request.POST['message-text']
            if len(content) > 0:
                msg = Message(content=content, author=request.user, timestamp=timezone.now())
                msg.save()

        return render(request, 'houseapp/home.html', context)
    except Exception:
        return HttpResponseRedirect('registration/createorjoin')


class TaskListView(ListView):
    model = Task
    template_name = 'houseapp/home.html'
    context_object_name = 'tasks'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('splash')



class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'due_date', 'user']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class MessageView(CreateView):
    model = Message
    fields = ['content', 'timestamp', 'author']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


def createhouse(request):
    return render(request, 'registration/CreateHouse.html')

def createorjoin(request):
    return render(request, 'registration/createorjoin.html')


def joinhouse(request):
    if request.method == 'POST':
        inv = request.POST['InputHouseID']
        h = None
        try:
            h = House.objects.get(invite_code=inv)
        except Exception:
            return HttpResponseRedirect('registration/JoinHouse.html')
        mem = Membership(person=request.user, house=h, date_joined=date.today())
        mem.save()
        return HttpResponseRedirect('/')

    return render(request, 'registration/JoinHouse.html')

def splash(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    return render(request, 'houseapp/splash.html')
  
class TaskCompleteView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.completed = True
        task.save(update_fields=['completed'])
        print("Completed", task)
        return super().get_redirect_url(*args)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"


# class CreateHouseView(CreateView):
#     model = House
#     fields = ['name', 'address', 'invite_code']
#     success_url = '/'
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#
# class JoinHouseView(TemplateView):
#     def post(self, request):
#         inv = request.POST['invite-code-input']
#         print(inv)
#         h = House.objects.get(invite_code=inv)
#         mem = Membership(person=request.user, house=h, date_joined=date.today())
#         mem.save()
#
#         return HttpResponseRedirect('/tasks/')
