from django.shortcuts import render

# Create your views here.


def signup(request):
    if request.method == 'POST':
        user=User.objects.create_user(
            request.POST['username'], password=request.POST['password1'])
        auth.login(request, user)
        return redirect('blog')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'username or password is not correct'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'signup.html')