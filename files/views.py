from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *
from .models import Notes
from django.contrib.auth import authenticate, logout, login
from datetime import date

# Create your views here.

def file_home(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # user = User.objects.get(id=request.user.id)
    # notes = Notes.objects.filter(user = user)
    notes = Notes.objects.all()
    # d = {'notes':notes}
    # return render(request,'files_homepage/index-Homepage.html',d)
    # q=[notes.values("uploadingdate","branch","subject","filetype","description")]
    d={
        'Note':notes
        }
    

    
    # queryset = User.objects.all()
    # values = queryset.values('uploadingdate', 'branch', 'subject', 'filetype', 'description')

    # d={
    #     'New':values,
    #     }

    return render(request,'files_homepage/index-Homepage.html',d)
    # d={
    #     'New':'RRR',
    #     }
    # return render(request,'files_homepage/index-Homepage.html',d)

def file_Submit(request):
    return render(request,"files_homepage/index-Submit-file.html")
def file_upload(request):

    error=""
    if request.method=='POST':
        u = User.objects.filter(username=request.user.username).first()
        print(u)
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        # value=Notes(branch=b,subject=s,notesfile=n,filetype=f,description=d)
        # value.save()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,
                                filetype=f,description=d)
            
            error="no"
        except:
            error="yes"

    return render(request,"files_homepage/index-Submit-file.html", locals())

def view_mynotes(request):
    
    d={
        'New':'RRR',
        }
    return render(request,'files_homepage/index-Homepage.html',d)
    # user = User.objects.get(id=request.user.id)
    # notes = Notes.objects.filter(user = user)
    # print(user)
    # a=2
    # d = {'notes':a,}
    # data=Notes.objects.all()
    # for i in data:
    #     print(i)
    # d={
    #     'New':'RRR',
    #     }
    # return render(request,'files_homepage/hi.html',d)


