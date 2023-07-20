from django.shortcuts import render, redirect
from .forms import ProductForm
from .forms import ReviewForm
from .forms import SearchProduct
import pymongo
import django_tables2 as tables
from django_tables2 import RequestConfig

class ProductTable(tables.Table):
    name  = tables.Column(verbose_name="name")
    company  = tables.Column(verbose_name="company" )
    description  = tables.Column(verbose_name="description")
    price  = tables.Column(verbose_name="price")
   
class ReviewTable(tables.Table):
    ranking  = tables.Column(verbose_name="ranking")
    name  = tables.Column(verbose_name="name")
    company  = tables.Column(verbose_name="company")
    comments  = tables.Column(verbose_name="comments")
    rating  = tables.Column(verbose_name="rating")
    price  = tables.Column(verbose_name="price")



def index(request):
    if request.method == "GET":
        connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(connection_string)
                    #create database variable
        db = client['Feedback']
                    #store Users data in a dictionary
        user_details = list(db.Reviews.find({}))
                    
        table = ReviewTable(user_details)
     
        return render(request, "main_page.html",{"table":table})

    elif request.method == "POST":
        if "add_btn" in request.POST:
            return redirect(f"addproduct/")
        elif "review_btn" in request.POST:
            return redirect(f"review/")
        elif "submit_btn" in request.POST:
            return redirect(f"/")

def product_page(request):
    if request.method == "GET":
        context ={}
        context['form']= ProductForm()
        connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(connection_string)
                    #create database variable
        db = client['Feedback']
                    #store Users data in a dictionary
        user_details = list(db.Products.find({}))
                    # looks through dictionary of data
        table = ProductTable(user_details)
        return render(request, "product_page.html", {'form':context['form'], "table":table})
    elif "add_btn" in request.POST:

        form = ProductForm(request.POST)
        form.non_field_errors()
        field_errors = [ (field.label, field.errors) for field in form]
        print(field_errors)
        if form.is_valid(): 
            data = form.cleaned_data
            name = data['name']
            company = data['company']
            description = data['description']
            price = data['price']
             #accessing the db
            connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
            client = pymongo.MongoClient(connection_string)
            #create database variable
            db = client['Feedback']
            #store Users data in a dictionary

            dict = {"name":name,"company":company, "description":description, "price":price}
            db.Products.insert_one(dict)
            return redirect(f"/feedbackranker/addproduct")  
    elif "return_btn" in request.POST:
            return redirect(f"/feedbackranker")  
    return redirect(f"/feedbackranker") 


def review_page(request):
    
    if request.method == "GET":
        context ={}
        context['form']= SearchProduct()
        connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(connection_string)
        db = client['Feedback']
        user_details = list(db.Products.find({}))
        table = ProductTable(user_details)
        return render(request, "review_page.html", {'form':context['form'], "table":table})

    elif "review_btn" in request.POST:
        form = SearchProduct(request.POST)

        if form.is_valid():   
       
            data = form.cleaned_data
            name = data['product']
            connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
            client = pymongo.MongoClient(connection_string)
            db = client['Feedback']
            products = db.Products.find({})
        
            for r in products:
               
                print(r["name"])
                if r["name"] == name:
                    return redirect("/feedbackranker/enterreview/"+name) 
    elif "return_btn" in request.POST:
        return redirect(f"/feedbackranker")  
    return redirect(f"/feedbackranker/review") 


def backendalgo(comments, rating):
    positive=["excellent", "outstanding","amazing","wonderful","delightful", "good", "like"]
    negative=["bad", "horrible", "dislike"]
    counter = 0
    for i in positive:
        if i in comments:
            counter += 1
    for j in negative:
        if j in comments:
            counter -= 1
    counter *= int(rating)
    return counter

def enterreview(request, id):
    if request.method == "GET":
        context ={}
        context['form']= ReviewForm()
        return render(request, "enterreview.html",context)
    elif "enter_btn" in request.POST:
        form = ReviewForm(request.POST)
       
        if form.is_valid(): 
            connection_string='mongodb+srv://mongoman:mangoeatmongo@cluster0.y3jdu5m.mongodb.net/?retryWrites=true&w=majority'
            client = pymongo.MongoClient(connection_string)
            db = client['Feedback']


            data = form.cleaned_data
            comments = data['comments']
            rating = data['rating']

            num = backendalgo(comments, rating)
            print(num)
            print(num)

            reviews = db.Products.find({})
            for r in reviews:
                if r["name"] == id:
                     dict = {'ranking':num, 'name':r["name"], 'company':r["description"], 'comments':comments, 'rating':rating, 'price':r["price"]}
           
            db.Reviews.insert_one(dict)

            return redirect(f"/feedbackranker/review")
    return redirect(f"/feedbackranker/review")

