from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	email = models.EmailField(max_length=264,unique=True)

	"""docstring for User"models.Modelf 
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	email = models.EmailField(max_length=264,unique=True)
	__init__(self, arg):
		super(User,models.Model._
		first_name = models.CharField(max_length=128)
		last_name = models.CharField(max_length=128)
		email = models.EmailField(max_length=264,unique=True)
		_init__()
		self.arg = arg
		"""