from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Administrator,Student
from django.contrib.auth import authenticate,login,logout
#-------------------------this page is responsible for defining functions that return pages --------
def index(request):
	return HttpResponse("hello,world!!")

# Create your views here.
# will return login html page when requested
def login_view(request):
		if request.method=="POST":
			username=request.POST["userName"]
			password=request.POST["userPassword"]
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect("menu")
			else:
				return render(request,"foodApp/Adminlogin.html",{"message":"incorrect credentials"})
		
		return render(request,"foodApp/Adminlogin.html")


			


# will return displayStudents html page when requested
def displayStudents(request):
	
	

	return render(request,"foodApp/displayStudents.html",{"Student":Student.objects.all()})



# will return displayStudent html page when requested
def addStudent(request):
	if request.method=="POST":
			name=request.POST["name"]
			surname=request.POST["surname"]
			studentNo=request.POST["studentNo"]

			mealPlan=request.POST.get('mealPlan')

			jan=request.POST.get('jan')
			feb=request.POST.get('feb')
			mar=request.POST.get('mar')
			apr=request.POST.get('apr')
			may=request.POST.get('may')
			jun=request.POST.get('jun')
			jul=request.POST.get('jul')
			aug=request.POST.get('aug')
			sep=request.POST.get('sep')
			octo=request.POST.get('oct')
			nov=request.POST.get('nov')
			dec=request.POST.get('dec')

			if jan is not None:
				jan=True

			else:

				jan=False
				#--------------------------------------------------------
			if feb is not None:
				feb=True

			else:

				feb=False
			#--------------------------------------------------------------------

			if mar is not None:
				mar=True

			else:

				mar=False

			#--------------------------------------------------------------------

			if apr is not None:
				apr=True

			else:

				apr=False


			#--------------------------------------------------------------------

			if may is not None:
				may=True

			else:

				may=False

			#--------------------------------------------------------------------

			if jun is not None:
				jun=True

			else:

				jun=False

			#--------------------------------------------------------------------

			if jul is not None:
				jul=True

			else:

				jul=False

			#--------------------------------------------------------------------

			if aug is not None:
				aug=True

			else:

				aug=False

			#--------------------------------------------------------------------

			if sep is not None:
				sep=True

			else:

				sep=False

			#--------------------------------------------------------------------

			if octo is not None:
				octo=True

			else:

				octo=False

			#--------------------------------------------------------------------

			if nov is not None:
				nov=True

			else:

				nov=False

			#--------------------------------------------------------------------

			if dec is not None:
				dec=True

			else:

				dec=False

			#----------------------------------------------------------------------


			mystudent=Student(name=name,surname=surname,studentNo=studentNo,mealPlan=mealPlan,jan=jan,feb=feb,mar=mar,apr=apr,may=may,jun=jun,jul=jul,aug=aug,sep=sep,octo=octo,nov=nov,dec=dec)
			mystudent.save()










			



			#print(mealPlan)
			#print(studentNo)


				

	return render(request,"foodApp/studentForm.html")

# will return displayStudent html page when requested
def menu(request):
	

	return render(request,"foodApp/menu.html")


# will return displayStudent html page when requested
def modifyStudent(request):

	return render(request,"foodApp/modifyStudent.html")

def logout_view(request):
	logout(request)
	return render(request,"foodApp/Adminlogin.html")


