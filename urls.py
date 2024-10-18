from django.urls import path

from .import views

#-----defines what happens if you call a path of a url.

urlpatterns=[
	# this calling the home page "foodApp" will call the function index()
	path("",views.index,name="index"),
	#this calling the page "foodApp/login" will call the function index()
	path("login",views.login_view,name="login"),
	path("logout",views.logout_view,name="logout"),
	#this calling the page "foodApp/students" will call the function index()
	path("students",views.displayStudents,name="displaystudents"),

	#this calling the page "foodApp/addstudent" will call the function index()
	path("addstudent",views.addStudent,name="addstudent"),
	
	path("modifystudent",views.modifyStudent,name="modifystudent"),
	path("menu",views.menu,name="menu")



]