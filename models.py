from django.db import models

# Create your models here.
#This page deals with the creation of database
#it instead uses a class instead of sql queries

#creating a class that will be used to create a database
class Administrator(models.Model):
	username=models.CharField(max_length=16)
	password=models.CharField(max_length=16)

#The run this command :python manage.py makemigrations
#run this also :python manage.py migrate("this actually update the contents of DB")
class Student(models.Model):
	name=models.CharField(max_length=20)
	surname=models.CharField(max_length=20)
	studentNo=models.IntegerField(default=00000)
	mealPlan=models.CharField(max_length=25)

	jan = models.BooleanField(default=False)
	feb = models.BooleanField(default=False)
	mar = models.BooleanField(default=False)
	apr = models.BooleanField(default=False)
	may = models.BooleanField(default=False)
	jun = models.BooleanField(default=False)
	jul = models.BooleanField(default=False)
	aug=models.BooleanField(default=False)
	sep = models.BooleanField(default=False)

	#only oct is saved as octo because it seems as if oct is a build in function
	octo = models.BooleanField(default=False)
	nov = models.BooleanField(default=False)
	dec = models.BooleanField(default=False)
	


 