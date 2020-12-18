# Add a Model Form to our signupPro project (Create a simple Coming Soon Landing Page!).
# Create a single User class in its models, then connect it to a form allowing users to register their
# names and emails to the site. Once connected to a ModelForm, the user will sign up on the user page
# and be taken back to the home page.


from django.shortcuts import render
from .forms import NewUserForm


def index(request):
    return render(request, 'signupApp/index.html')


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # save data filled by the user
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'signupApp/users.html', {'form': form})
