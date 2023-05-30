from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from loginsystem.settings import BASE_DIR
from .forms import ImageForm, RegistrationForm
from .models import Image
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import os


class Home(TemplateView):
    template_name = "home.html"


class Images(TemplateView):
    template_engine = "images.html"


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Your profile was created successfully"


# class ImageView(View):
#     def get(self, request, *args, **kwargs):
#         form = ImageForm()
#         img = Image.objects.all()
#         return render(request, 'myapp/image.html', {'img': img, 'form': form})

#     def post(self, request, *args, **kwargs):
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         img = Image.objects.all()
#         return render(request, 'myapp/image.html', {'img': img, 'form': form})

@method_decorator(login_required, name='dispatch')
class ImageView(View):
    def get(self, request, *args, **kwargs):
        # print("Get Method", type(request.GET.get('uploaded_by')),
        #       request.GET.get('uploaded_by') == str(request.user), type(request.user))

        if (request.GET.get('uploaded_by') == str(request.user)):
            try:
                img = Image.objects.filter(
                    id=request.GET.get('id'), uploaded_by=request.user)
                os.remove(str(BASE_DIR) + "/media/" + request.GET.get('image'))
                img.delete()
                message = "Image successfully deleted"
                return redirect('myapp')
            except Image.DoesNotExist:
                message = "Image not found"

        form = ImageForm()
        img = Image.objects.filter(uploaded_by=request.user)
        return render(request, 'myapp/image.html', {'img': img, 'form': form})

    def post(self, request, *args, **kwargs):
        print("post Method", request.user)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # set the uploaded_by field to the current user
            image.uploaded_by = request.user
            image.save()
            return redirect('myapp')
        img = Image.objects.filter(uploaded_by=request.user)
        return render(request, 'myapp/image.html', {'img': img, 'form': form})
