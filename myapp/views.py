from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from myapp.models import Lance
# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    return redirect('login')
  lances = Lance.objects.all().order_by('-valor')
  primeiro = lances[0]
  resto = lances[1:]
  temLanceAtivo = False
  for lance in lances:
    usuario = str(request.user.username)
    jogador = str(lance.jogador)
    if usuario.upper()  == jogador.upper():
      temLanceAtivo = True

  return render(request, 'index.html', {'primeiro': primeiro, 'resto': resto, 'temLanceAtivo': temLanceAtivo})

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
        messages.info(request, 'Usuário já cadastrado')
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
      messages.info(request, 'Usuário ou senha inválidos.')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/')

def adicionarLance(request):
  if request.method == 'POST':
    valor = request.POST.get('valor')
    if int(valor) > 0:
      jogador_id = request.user
      Lance.objects.create(jogador= jogador_id,valor= valor).save()
      return redirect('index')
    else:
      messages.info(request, 'Digite um valor positivo.')
      return redirect('index')
  else: 
    return render(request, 'index.html')

def editarLance(request):
  if request.method == 'POST':
    valor = request.POST.get('valor')
    if int(valor) > 0:
      jogador_id = request.user.id
      Lance.objects.filter(jogador = jogador_id).update(valor = valor)
      return redirect('index')
    else:
      messages.info(request, 'Digite um valor positivo.')
      return redirect('index')
  else: 
    return render(request, 'index.html')

def deleteLance(request):
  jogador_id = request.user.id
  lance = Lance.objects.get(jogador = jogador_id)
  lance.delete()
  return redirect('index')