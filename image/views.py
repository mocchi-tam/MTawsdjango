from django.shortcuts import render_to_response
from django.views import generic
from .forms import UploadForm
from .models import Image
from mtsoft.face import detect

class ImageList(generic.ListView):
    model = Image

class ImageForm(generic.FormView):
    form_class = UploadForm
    template_name = 'image/image_form.html'

    def form_valid(self, form):
        file = form.cleaned_data['file']
        result_img, char_names = detect(file)
        image_model = Image(file=result_img, names=char_names)
        image_model.save()
        
        return render_to_response('image/image_list.html', 
                                  {'img': image_model })
        