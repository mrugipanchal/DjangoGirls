from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from blog.forms import BlogAddForm


# Create your views here.
def blog_list(request):
	blog=Blog.objects.all()
	# return HttpResponse("<h1>create one blog</h1>")
	return render(request, "blog/list.html", {'blogs': blog})

def blog_new(request):
	if request.method == 'GET':
		form = BlogAddForm()
	if request.method == 'POST':
		form = BlogAddForm(request.POST)
		f = form.save(commit=False)
		f.created_by = request.user
		f.save()

	return render(request, "blog/create.html", {'form': form})
	#return HttpResponse("<h1>create new blog</h1>")

def blog_id(request, id):
	try:
		blog=Blog.objects.get(id=id)
	except:
		return HttpResponse("<h1>no blog found</h1>")
	return render(request, "blog/id.html", {'blog':blog})
	#return HttpResponse("<h1>create id blog {}</h1>".format(id))

def blog_edit(request, id):
	try:
		blog=Blog.objects.get(id=id)
	except:
		return HttpResponse("<h1>no blog found</h1>")
	if request.method == 'GET':
		form = BlogAddForm(instance=blog)
	if request.method == 'POST':
		form = BlogAddForm(request.POST, instance=blog)
		f = form.save(commit=False)
		f.created_by = request.user
		f.save()
	return render(request, "blog/create.html", {'form': form})

def blog_name(request, name):
	return HttpResponse("<h1>create name blog {}</h1>".format(name))