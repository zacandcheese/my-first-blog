from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Info, Summary, Applying, ApplyingAs
from .form import PostForm, ApplyForm, ChoiceForm
from django.views.generic import FormView
from django.http import HttpResponse
from django.shortcuts import redirect

def post_list(request):
	people = Info.objects.all()
	return render(request, 'type/post_list.html', {'posts':people})

def post_detail(request, pk):
	final = None
	print("pk is this",pk)
	for e in Summary.objects.all():
		if(int(e.newID) == int(pk)):
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
        #passage = " the sun did not shine. it was too wet to play. so we sat in the house all that cold, cold, wet day. i sat there with sally. we sat there, we two. and i said,“how i wish we had something to do. too wet to go out and too cold to play ball. so we sat in the house. we did nothing at all. so all we could do was to sit. sit. sit. sit. and we did not like it. not one little bit. and then something went bump. how that bump made us jump. we looked. then we saw him step in on the mat. we looked. and we saw him. the cat in the hat."
        passage = " A certain king had a beautiful garden, and in the garden stood a tree which bore golden apples."+"These apples were always counted, and about the time when they began to grow ripe it was found that every night one of them was gone."+"The king became very angry at this, and ordered the gardener to keep watch all night under the tree."+		"The gardener set his eldest son to watch but about twelve o'clock he fell asleep, and in the morning another of the apples was missing."+		"Then the second son was ordered to watch and at midnight he too fell asleep, and in the morning another apple was gone."+"Then the third son offered to keep watch but the gardener at first would not let him, for fear some harm should come to him however, at last he consented, and the young man laid himself under the tree to watch."+		"As the clock struck twelve he heard a rustling noise in the air, and a bird came flying that was of pure gold and as it was snapping at one of the apples with its beak, the gardener's son jumped up and shot an arrow at it."+		"But the arrow did the bird no harm only it dropped a golden feather from its tail, and then flew away."+		"The golden feather was brought to the king in the morning, and all the council was called together."+		"Everyone agreed that it was worth more than all the wealth of the kingdom but the king said, One feather is of no use to me, I must have the whole bird."
		#passage = ["the sun did not shine."," it was too wet to play. so we sat in the house all that cold, cold, wet day."," i sat there with sally."," we sat there, we two."," and i said,“how i wish we had something to do."," too wet to go out and too cold to play ball."," so we sat in the house."," we did nothing at all."," so all we could do was to sit."," sit."," sit."," sit."," and we did not like it."," not one little bit."," and then something went bump."," how that bump made us jump."," we looked."," then we saw him step in on the mat."," we looked."," and we saw him."," the cat in the hat and he said to us, why do you sit there like that.","i know it is wet and the sun is not sunny."]
        #passage = ["you took care of the other bare man."," you gave the bare man ate a hare. "," you are mean"]
    return render(request, 'type/post_edit.html', {'form': form,'passage':passage})

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
		if(int(e.newID) == int(pk)):
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
	user = Applying.objects.last()
	list = Summary.objects.all()
	answer = Applying.getAnswer(user, list)
	return render(request, 'type/answer.html', {'answer':answer})
		
def apply_new(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('validate')
    else:
        form = ApplyForm()
        who = ApplyingAs.objects.last()
        print(who, who.choice)
        combos = Applying.getMostUniqueCombo(Info.objects.filter(author=who.choice)[0],Summary.objects.all())
        passage = Applying.getSentences(combos)
        return render(request, 'type/post_edit.html', {'form': form,'passage':passage,'who':who.choice})

class PostChoicesPage(FormView):
	template_name = 'choice.html'
	success_url = '/post/applying/'
	form_class = ChoiceForm
	
	def form_valid(self, form):
		return HttpResponse("Sweet.")
		
def choice_new(request):
	if request.method == "POST":
		form = ChoiceForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('apply')
	else:
		form = ChoiceForm()
	return render(request, 'type/choice.html', {'form': form})
