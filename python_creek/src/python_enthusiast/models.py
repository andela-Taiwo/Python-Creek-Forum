from django.db import models

# Create your models here.
class SignUp(models.Model):

	email = models.EmailField()
	first_name=models.CharField(max_length=25,default="First Name", blank=True, null=True)
	time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now_add=True, auto_now=False)
	upload = models.FileField(upload_to=None ,max_length=100)

	def __unicode__(self):
		return str(self.email)


