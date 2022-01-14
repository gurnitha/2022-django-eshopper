from django.shortcuts import render

# Create your views here.


def posts(request):
	return render(request, 'posts.html')


def post_detail(request):
	return render(request, 'post_detail.html')
