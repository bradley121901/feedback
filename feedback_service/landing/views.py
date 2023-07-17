from django.shortcuts import render, redirect

def index(request):
    if request.method == "GET":
        return render(request, "landing.html")

    elif request.method == "POST":
    
        if "login" in request.POST:
            return redirect(f"/feedbackranker")
        elif "register" in request.POST:
            return redirect(f"register/")



def register(request):
    if request.method == "GET":
        return render(request, "register.html")
  