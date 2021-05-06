from .models import TaskModel, TextModel
from .forms import TaskForm, TextForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

def create_view(request):
    # Создание шаблона
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on 
                                <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        form = TaskForm()
        context = {'form':form}
        return render(request, 'firstapp/create.html', context)


def create_text(request):
    # Создание текста шаблона
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on 
                                <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        form = TextForm()
        context = {'form':form}
        return render(request, 'firstapp/createtext.html', context)

                        
def list_view(request):
    # отображение всех шаблонов
    dataset = TaskModel.objects.all()
    textset = TextModel.objects.all()
    return render(request, 'firstapp/listview.html', 
                  {'dataset':dataset, 'textset':textset})

def template_detail_view(request, recv_id):
    # отображение конкретного шаблона по адресу <int:recv_id>/
    try:
        data = TaskModel.objects.get(id=recv_id)
        text = TextModel.objects.get(id=recv_id)
        q = TaskModel(name=data,text_template=text)
        #q.save()
    except TaskModel.DoesNotExist:
        return render(request, 'This template not Exist! ')
    return render(request, 'firstapp/detailview.html', {'data': data,'text':text,'id':id, 'q':q})

def update_view(request, recv_id):
    try:
        old_data = get_object_or_404(TaskModel, id=recv_id)
    except Exception:
       return redirect('index')
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance = old_data)
        context ={
            'form':form, 'id':recv_id
        }
        return render(request, 'firstapp/update.html', context)
    
def update_text_view(request, recv_id):
    try:
        old_data = get_object_or_404(TextModel, id=recv_id)
    except Exception:
       return redirect('index')
    if request.method =='POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TextForm(instance = old_data)
        context ={
            'form':form, 'id':recv_id
        }
        return render(request, 'firstapp/updatetext.html', context)

def delete_view(request, recv_id):
    try:
        data = get_object_or_404(TaskModel, id=recv_id)
    except Exception:
        raise Http404('This template is not exist!')
    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        return render(request, 'firstapp/delete.html')

def generate_message(request):
    dataset = TaskModel.objects.all()
    return render(request, 'firstapp/genermessage.html', 
                  {'dataset':dataset})
