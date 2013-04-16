from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from blogster.models import Post, Category

def index(request):
	return render(request, 'index.html')

def getPosts(request, selected_page=1):
	#get all blog posts
	posts = Post.objects.all().order_by('-pub_date')

	#get recent blog posts
	recent_posts = []
	for post in posts:
		if post.was_recently_published():
			recent_posts.append(post)

	#Add pagination
	pages = Paginator(posts, 5)

	try:
		returned_page = pages.page(selected_page)
	except EmptyPage:
		returned_page = pages.page(pages.num_page)

	#get all the categories available
	categories = Category.objects.all()
	
	#create a context of data to pass to template
	context = {'posts': returned_page.object_list, 'page': returned_page, 'categories': categories, 'recent_posts': recent_posts}

	#display all the posts
	return render(request, 'posts.html', context)

def getPost(request, postSlug):
	#get specified posts
	post = Post.objects.filter(slug=postSlug)

	#get all the available categories
	categories = Category.objects.all()

	#get all blog posts
	posts = Post.objects.all().order_by('-pub_date')

	#get recent posts
	recent_posts = []
	for pst in posts:
		if pst.was_recently_published():
			recent_posts.append(pst)

	#creating context to pass to template
	context = {'posts': post, 'categories': categories, 'recent_posts': recent_posts}

	#display the post
	return render(request, 'single.html', context)

def getCategory(request, categorySlug, selected_page=1):
	#get specified category
	posts = Post.objects.all().order_by('-pub_date')
	category_posts = []

	for post in posts:
		if post.categories.filter(slug=categorySlug):
			category_posts.append(post)

	#add pagination
	pages = Paginator(category_posts, 5)

	#get the category
	category = Category.objects.filter(slug=categorySlug)[0]

	#get the specified page
	try:
		returned_page = pages.page(selected_page)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	#creating a context
	context = {'posts':returned_page.object_list, 'category':category, 'page':returned_page}
	
	#passing the value to the template
	return render(request, 'category.html', context)