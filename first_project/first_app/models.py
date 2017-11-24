from django.db import models

# Create your models here.

class Topic(models.Model):
	top_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.top_name
	"""docstring for Topic"models.Modelf 
	top_name = models.ChaField(max_length=264,unique=True)__init__(self, arg):
		super(Topic,models.Model._
		top_name = models.ChaField(max_length=264,unique=True)_init__()
		self.arg = arg
		"""

class Webpage(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=264,unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name
	"""docstring for Webpage"models.Modelf __init__(self, arg):
		super(Webpage,models.Model.__init__()
		self.arg = arg
		"""


class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage)
	date = models.DateField()

	def __str__(self):
		return str(self.date)

	"""docstring for AccessRecord"models.Modelf 
	name= models.Fo__init__(self, arg):
		super(AccessRecord,models.Model._
		name= models.Fo_init__()
		self.arg = arg
		"""