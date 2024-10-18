
// gets triggered when submit button is clicked
//check whether the the username and password are empty and alert the user to enter his/her details
function funcLogin(){
	if( document.myForm.AdminPassword.value == "" || document.myForm.AdminPassword.value == "" ) {
    	alert( "Username or password field cannot be empty!!!" );
    }
    
    else if(document.myForm.AdminPassword.value == "Admin" && document.myForm.AdminPassword.value == "Admin" ) {
        redirect();
    }
    else{
    	alert("Incorrect username or password");
    }

			
}
//This fuction redirect the page to this website
function redirect() {
    window.location = "menu.html";
}

function funcLogout(){
    window.location = "Adminlogin.html";

}
function toViewPage() {
    window.location = "displayStudents.html";
}
function toAddPage() {
    window.location = "studentForm.html";
}
function toModifyPage() {
    window.location = "modifyStudent.html";
}
