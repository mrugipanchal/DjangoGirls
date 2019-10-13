from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField('date published', auto_now_add=True)
	content = models.TextField()
	published = models.BooleanField(default=False)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.title
 