from django.shortcuts import render
from .forms import PostForm
from django.views import View
import os

# Create your views here.

class IndexView(View):
    form_class = PostForm
    template_name = 'exportar/index.html'

    def get(self, request):
        pass


        # if request.method == 'POST':
        #     form = self.form_class(request.POST, request.FILES)
        #     if form.is_valid():
        #         print('tá válido')
        #         uploaded_file = request.FILES['pdf']
        #         file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        #         with open(file_path, 'wb+') as destination:
        #             for chunk in uploaded_file.chunks():
        #                 destination.write(chunk)
        #         return render(request, self.template_name, {'form': form})
        # else:
        #     return render(request, self.template_name)



# def file_upload(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
        
#     context = {'form': form}
#     return render(request, 'exportar', context)