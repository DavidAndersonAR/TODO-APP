from django.shortcuts import render, redirect
from . models import  Category, TodoList

# Create your views here.


def index(request):
    todo = TodoList.objects.all() # consultando todas as tarefas com o gerenciador de objetos
    categories = Category.objects.all() # pegando todas as categorias com o gerenciador de objetos

    if request.method == 'POST':  # checando se o método request é POST
        if 'taskAdd' in request.POST:  # checando se há requisição para add uma tarefa

            title = request.POST['description'] # titulo
            date = str(request.POST['date']) # data
            category = request.POST["category_select"] # categoria
            content = title + "--" + date + " " + category # conteudo

            todo = TodoList(title=title, content = content, due_date = date, category = Category.objects.get(nome=category))
            todo.save() # salvando a tarefa

            return redirect('/') # recarregando a página
        
        if 'taskdelete' in request.POST:
            checkedlist = request.POST['checkedbox']  # checando tarefas a serem deletadas

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) # pegando id da tarefa
                todo.delete() # deletando tarefa
    return render(request, 'index.html', {'todos': todo, 'categories' : categories})