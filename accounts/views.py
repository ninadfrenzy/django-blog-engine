from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('articles:list')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request,user)
            print(request.POST)
            if 'next' in request.POST:
                print('in if block')
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        print(request.GET)
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')