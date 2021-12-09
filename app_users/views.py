from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as django_logout
# AuthenticationForm is the pre-built Django form logging in a user
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
# personal import
from .forms import NewUserForm


# Create your views here.


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)  # data to name the parameter
        if form.is_valid():
            # retrieve the user
            user=form.get_user()
            # log the user in
            login(request, user)
            return redirect('/my_account/')
    else:
        #  if the request is not a POST, then return the blank form in the login HTML template
        form=AuthenticationForm()
        return render(request=request, template_name="login.html", context={"login_form": form})


class Validator:
    @staticmethod
    # verify single email in the database. Not by default on User Django model.
    def valid_email_didnt_exist(email):
        # return User.objects.get(email=email).exists()  # return true if the email already exists
        return User.objects.filter(email=email).exists()


def register_request(request):
    # checks if the form is posted
    if request.method == 'POST':  # detect if the request is POST for sending data to the server do:
        # .POST to access the data which comes along with the post request
        # we pass the data to a new instance of the NewUserForm (inherited from UserCreationForm)
        # kind of Validating data for us (pwd, user already exists or not, etc)
        form=NewUserForm(request.POST)

        # is_valid_username=validator.valid_username_didnt_exist(form.cleaned_data.get('username'))
        if form.is_valid():  # check if the form is valid, return true or false, name is validated here
            # execute the block only if the value is not empty or not False.
            validator=Validator()  # instantiation of the class
            is_valid_email=validator.valid_email_didnt_exist(form.cleaned_data.get('email'))
            # if not is_valid_email and not is_valid_username:
            if not is_valid_email:
                user=form.save()  # if the 3 are true (post, is_valid, validator) then information is saved under a user
                login(request, user)  # log the user in
                #  the user is redirected to my_account page showing a success message.
                return redirect('/my_account/')
            else:
                # if the form is not valid, an error message is shown
                # messages.error(request, "email déjà utilisé!")
                error="Username ou Addresse de courriel déjà utilisée par un autre utilisateur!"
                context={
                    "register_form": form,
                    "error": error,
                }
                return render(request, 'register.html', context)

                # return render(request=request, template_name="register.html", context={'error': error})
                # raise forms.ValidationError("Addresse de courriel ou mot de passe déjà utilisés")

    form=NewUserForm  # fresh version of the form if not POST and sending blank it
    return render(request=request, template_name="register.html", context={"register_form": form})


@login_required(login_url='/login/')
# login_required()
def my_account(request):
    user=request.user
    user=User.objects.filter(email=user.email).get()
    context={
        'user': user}
    return render(request, 'my_account.html', context)


def logout(request):
    """The logout view, handling logout requests
    :param request: provided by Django
    """
    django_logout(request)
    return redirect(reverse("index"))  # return ver url index after action
