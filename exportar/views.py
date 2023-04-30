from django.shortcuts import render
from .forms import PostForm
from django.views import View
import PyPDF2


class IndexView(View):
    form_class = PostForm
    template_name = 'exportar/index.html'

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                pdf_file = request.FILES['pdf_file']
                print(pdf_file.name)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                number_pages = len(pdf_reader.pages)
                page = pdf_reader.pages[0]
                text = page.extract_text()
                print(text)
                print(f'Número de páginas: {number_pages}')
            else:
                form = self.form_class(request.POST, request.FILES)
                print(form.errors)
                print('aqui')
            return render(request, self.template_name, {'form': form})
