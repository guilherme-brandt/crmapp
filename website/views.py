from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carregar o arquivo .env
load_dotenv()
from .forms import SignUpForm, AddRecord, ContactForm
from .models import Record
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('records')
        else:
            messages.success(request, "There was an error, please try again!")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")    
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            if user is not None:
                messages.success(request, "Account created successfully! Welcome!")
                return redirect('login')
        else:
            messages.success(request, "There was an error! Please try again!")
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def records(request):
    records = Record.objects.all()
    return render(request, 'records.html', {'records': records})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
    else:
        messages.success(request, "You're not logged in!")
    return render(request, 'record.html', {'customer_record': customer_record})

def delete_record(request, pk):
    if request.user.is_authenticated:
        to_delete = Record.objects.get(id=pk)
        to_delete.delete()
        records = Record.objects.all()
        messages.success(request, "Record deleted successfully!")
    else:
        messages.success(request, "You must be logged in to delete records!")
    
    return render(request, 'records.html', {'records': records})

def add_record(request):
    form = AddRecord(request.POST or None)
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            if form.is_valid():
                form.save()
                messages.success(request, "Record added successfully!")
                return redirect('records')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to create record!")
        return redirect('home')
    
def confirm_delete(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
    else:
        messages.success(request, "You're not logged in!")
    return render(request, 'confirm_delete.html', {'customer_record': customer_record})

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!")
            return redirect('records')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You're not logged in!")
        return redirect("login")
    
def search_records(request):
    query = request.GET.get('q', '')
    records = Record.objects.filter(first_name__icontains=query) | Record.objects.filter(last_name__icontains=query) | Record.objects.filter(city__icontains=query)

    data = []
    for record in records:
        data.append({
            'id': record.id,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'city': record.city,
            'phone': record.phone,
        })

    return JsonResponse({'records': data})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Montando os dados do e-mail
            email_message = '''
            From:\n\t\t{}\n
            Message:\n\t\t{}\n
            Email:\n\t\t{}\n
            '''.format(name, message, email)
            
            # Definindo o e-mail
            msg = MIMEMultipart()
            msg['From'] = 'glbfaria42@gmail.com'
            msg['To'] = 'guiloubrandt@hotmail.com'
            msg['Subject'] = 'Você recebeu uma mensagem!'

            # Codificar o corpo do e-mail em UTF-8
            msg.attach(MIMEText(email_message, 'plain', 'utf-8'))

            try:
                # Enviando o e-mail via servidor SMTP do Gmail
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login('glbfaria42@gmail.com', os.getenv('EMAIL_PASSWORD'))
                    server.sendmail(msg['From'], msg['To'], msg.as_string())
                print("Email enviado com sucesso")
                messages.success(request, "Obrigado " + name + ", entraremos em contato em breve!")
            except Exception as e:
                print("Erro ao enviar o email:", str(e))
                messages.error(request, 'Erro ao enviar o email. Tente novamente.')

    return render(request, 'home.html', {'form': form})

from django.http import HttpResponseRedirect
from django.utils import translation

def set_language(request):
    # Obtém o parâmetro 'language_id' da URL
    language_id = request.GET.get('language_id')
    
    if language_id:
        # Define o idioma no objeto de tradução e na sessão
        request.session['django_language'] = language_id
        translation.activate(language_id)
    
    # Redireciona para a página inicial
    return HttpResponseRedirect('/')