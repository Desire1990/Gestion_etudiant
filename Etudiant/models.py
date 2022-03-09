from datetime import date
from django.db import models

# Create your models here.
class Campus(models.Model):
	id = models.SmallAutoField(primary_key=True)
	name = models.CharField(max_length=120, null=False)

	def __str__(self):
		return f"{self.name}"


class Faculte(models.Model):
	id = models.SmallAutoField(primary_key=True)
	campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
	name = models.CharField(max_length=50, null=False, unique=True)
	address = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"


class Institut(models.Model):
	id = models.SmallAutoField(primary_key=True)
	campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
	name = models.CharField(max_length=50, null=False, unique=True)
	address = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

class Departement(models.Model):
	id = models.SmallAutoField(primary_key=True)
	faculte = models.ForeignKey(Faculte,null=True, on_delete=models.CASCADE)
	institut = models.ForeignKey(Institut,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=False, unique=True)

	def __str__(self):
		return self.name


class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
	numero_matricule = models.BigIntegerField(unique=True)
	first_name = models.CharField(max_length=50, null=False, blank=True)
	last_name = models.CharField(max_length=50, null=False, blank=True)
	classe = models.CharField(max_length=50, null=False, blank=True)

	def save(self, *args, **kwargs):
		if not self.numero_matricule :
			self.numero_matricule = self.generateMatricule()
		return super().save(*args, **kwargs)

	def generateMatricule(self):
		year = datetime.date.today().year
		return "{}{:0>2d}".format('E', self.student_id)
	
	def fullname(self):
		return self.first_name+" "+self.last_name

	def __str__(self):
		return self.fullname
	