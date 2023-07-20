from django.shortcuts import render, redirect
import pymongo
from .forms import RegisterForm
from .forms import LoginForm

def index(request):
    if request.method == "GET":
        context ={}
        context['form']= LoginForm()
        return render(request, "landing.html", context)

    elif request.method == "POST":
      
        if "login" in request.POST:
            form = LoginForm(request.POST)

            if form.is_valid(): 

                data = form.cleaned_data
                logusername = data['logusername']
                logpassword = data['logpassword']
                print(type(logusername))

             #accessing the db
                connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
                client = pymongo.MongoClient(connection_string)
                    #create database variable
                db = client['Feedback']
                    #store Users data in a dictionary
                user_details = db.Users.find({})
                    # looks through dictionary of data
                for r in user_details:
                    if(r["username"]== logusername):
                        if(r["password"] == logpassword):
                            return redirect(f"/feedbackranker")
                
            return redirect(f"/")
         
            
        elif "register" in request.POST:
            return redirect(f"register/")



def register(request):
    if request.method == "GET":
        context ={}
        context['form']= RegisterForm()
        return render(request, "register.html", context)
    elif request.method == "POST":
        
        if "register_btn" in request.POST:
            form = RegisterForm(request.POST)

            if form.is_valid(): 

                data = form.cleaned_data
                username = data['username']
                email = data['email']
                password = data['password']
                confirmpassword = data['confirmpassword']

            
                dict = {'username':username,'email': email, 'password': password}

                #accessing the db
                connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
                client = pymongo.MongoClient(connection_string)

                #create database variable
                db = client['Feedback']
               
                #insert into Users collection on database
                db.Users.insert_one(dict)

                return redirect(f"/feedbackranker")
         
            return redirect(f"/feedbackranker")


        elif "login_btn" in request.POST:
            return redirect(f"/feedbackrankers")

  

def review_view(request):
    return render(request, 'review_page.html')
