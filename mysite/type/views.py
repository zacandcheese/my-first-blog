from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Info
from .models import Summary
from .form import PostForm
from django.shortcuts import redirect

def post_list(request):
	people = Info.objects.all()
	return render(request, 'type/post_list.html', {'posts':people})

def post_detail(request, pk):
	final = None
	print("pk is this",pk)
	for e in Summary.objects.all():
		if(int(e.ID) == int(pk)):
			print(e.author)
			final = e
		elif(e.author == pk):
			final = e
		else:
			print(e.author)
	if(final == None):
		final = Summary.objects.first()
		
	combo=final.comboListText
	times=final.medListText
	
	return render(request, 'type/post_detail.html', {'post': final,'combo':combo,'times':times,})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('get_name', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'type/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Info, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post.author)
            return redirect('get_name', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'type/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Info.objects.all()
    return render(request, 'type/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Info, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
	
from .form import NameForm

def get_name(request, pk):
    # if this is a POST request we need to process the form data
	final = None
	for e in Summary.objects.all():
		if(int(e.id) == int(pk)):
			return redirect('post_detail', pk=pk)
			
	for e in Info.objects.all():
		if(int(e.id) == int(pk)):
			final = e
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('post_detail', pk=post.pk)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
	author = final.author
	l1,l2,l3 = Summary.getData(final)
	return render(request, 'type/name.html', {'form': form,'combo':l1,'times':l2,'author':author,'newId':l3})
	
def validate(request):
	list = Info.objects.all()
	