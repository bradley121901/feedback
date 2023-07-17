from django.shortcuts import render, redirect

def index(request):
    if request.method == "GET":
      
        return render(request, "main_page.html")

    elif request.method == "POST":
        if "product" in request.POST:
            return redirect(f"addproduct/")
        elif "review" in request.POST:
            return redirect(f"review/")

def product_page(request):
    if request.method == "GET":
        return render(request, "product_page.html")
    elif "add_btn" in request.POST:
        print(1)

def review_page(request):
    if request.method == "GET":
        return render(request, "review_page.html")


