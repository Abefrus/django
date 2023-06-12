from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            # Додаткова логіка після збереження форми
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})