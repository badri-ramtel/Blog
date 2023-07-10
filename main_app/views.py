from django.shortcuts import render, redirect
from main_app.models import Blog
# from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# @login_required
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'main_app/home.html', {'blogs': blogs})

    # query = request.GET.get('query')
    # if query is None:
    #     blogs = Blog.objects.all()      
    # else:
    #     blogs = Blog.objects.filter(title__icontains=query)
    #     request.session['query'] = query
    # return render(request, 'main_app/home.html', {'blogs': blogs})


    # paginator = Paginator(todo_list,3)  # Show 3 todo list per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # print('********************')
    # print(page_obj)
   
        
    # return render(request, 'main_app/home.html', )

# # @login_required
def add(request):
    if request.method == 'GET':
        return render(request, 'main_app/add.html')
    else:
        title = request.POST['title']
        intro = request.POST['introduction']
        blist = request.POST['body_list']
        cons = request.POST.get('conclusion') if request.POST.get('conclusion') else False

        Blog.objects.create(title=title, introduction=intro, body_list=blist, conclusion=cons, user_id=1)
        messages.success(request, 'Added successfully......')
        return redirect('mainapp-home')

# # @login_required
def edit(request, id):
    blogs = Blog.objects.get(id=id)
    try:
        blogs = Blog.objects.get(id=id)

    except Blog.DoesNotExist:
        return redirect('404notfound')

    if request.method == 'GET':
        return render(request, 'main_app/edit.html', {'blogs' : blogs})
    
    else:
        blogs.title = request.POST['title']
        blogs.introduction = request.POST['introduction']
        blogs.body_list = request.POST['body_list']
        blogs.conclusion = request.POST.get('conclusion') if request.POST.get('conclusion') else False
        
        blogs.save()
        messages.success(request, 'Updated Successfully!!!...')
        return redirect('mainapp-home')

# # @login_required()
def delete(request, id):
    try:
        blogs = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return redirect('404notfound')
    blogs.delete()
    return redirect('mainapp-home')

# def not_found(request):
#     return render(request, 'core/404.html')

def blogsview(request, id):
    bloger = Blog.objects.get(id=id)
    if request.method == 'GET':
        print(bloger)
        return render(request, 'main_app/blogsview.html', {'bloger' : bloger})
    
    
    else:
        bloger.title = request.POST['title']
        bloger.introduction = request.POST['introduction']
        bloger.body_list = request.POST['body_list']
        bloger.conclusion = request.POST.get('conclusion') if request.POST.get('conclusion') else False
        print(bloger)