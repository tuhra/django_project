from django.shortcuts import render

posts = [
	{
		'author': 'Thura',
		'title': 'Lorem Ipsum One',
		'content': 'Blog Content One',
		'date_posted': 'Jun 2, 2022'
	},
	{
		'author': 'Sandi',
		'title': 'Lorem Ipsum Two',
		'content': 'Blog Content Two',
		'date_posted': 'Jun 2, 2022'
	},
	{
		'author': 'Thura',
		'title': 'Lorem Ipsum Three',
		'content': 'Blog Content Three',
		'date_posted': 'Jun 2, 2022'
	},
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})	