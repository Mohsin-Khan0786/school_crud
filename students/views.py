from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, CustomUser
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            return render(request, 'login.html', {'error': 'User does not exist'})
        if user.password == password:
            request.session['user_id'] = user.id
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Incorrect password'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/login/')
def dashboard(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'students': students})

@login_required(login_url='/login/')
def create_student(request):
    if request.method == 'POST':
        Student.objects.create(
            user=request.user,
            name=request.POST['name'],
            age=request.POST['age'],
            course=request.POST['course']
        )
    return redirect('dashboard')

@login_required(login_url='/login/')
def update_student(request, id):
    student = Student.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
    return redirect('dashboard')
@login_required(login_url='/login/')
def delete_student(request, id):
    student = Student.objects.get(id=id, user=request.user)
    student.delete()
    return redirect('dashboard')
def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already in use'})
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})
        CustomUser.objects.create(
            email=email,
            username=username,
            password=password  
        )

        return redirect('login')

    return render(request, 'register.html')
def home_view(request):
    return render(request, 'home.html')
