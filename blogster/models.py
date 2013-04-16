from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200, unique=True)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return 'categories/%s' % self.slug

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	pub_date = models.DateTimeField()
	description = models.TextField(max_length=250)
	text = models.TextField()
	slug = models.SlugField(unique=True, max_length=40)
	author = models.ForeignKey(User)
	categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "%s/%s/%s/%s" % ("blog", self.pub_date.year, self.pub_date.month, self.slug)

class CategoryToPost(models.Model):
	post = models.ForeignKey(Post)
	category = models.ForeignKey(Category)