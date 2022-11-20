from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from myapp.models import Item
# Create your views here.
def index(request):
  items = Item.objects.all()
  return render(request, 'index.html', {'items': items})

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email já cadastrado')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Usuário já existe')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
      messages.info(request, 'Digite a mesma senha')
      return redirect('register')
  else:
    return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    if user:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Usuário não existe')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/')

def post(request, pk):
  return render(request, 'post.html', {'pk': pk})

def counter(request):
  text = request.POST['text']
  amount = len(text.split())
  return render(request, 'counter.html', {'amount': amount})
