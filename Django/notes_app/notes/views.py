from django.contrib.auth import authenticate, login
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NoteForm
from .models import Note, Category


# from forms import NoteForm


def index(request):
    return HttpResponse("Hello from 26.09.2023!")


def home_page(request):
    notes = Note.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'notes_list': notes, 'categories': categories})


def add_note_page(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = Note.objects.create(**form.cleaned_data)
            new_note.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = NoteForm()
        return render(request, 'add_note_page.html', {'form': form})


def edit_note_page(request, note_id):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            Note.objects.filter(pk=note_id).update(**form.cleaned_data)
            return HttpResponseRedirect(reverse('index'))
    else:
        note = Note.objects.get(id=note_id)
        form = NoteForm(
            initial={'title': note.title, 'text': note.text, 'reminder': note.reminder, 'category': note.category})
        return render(request, 'edit_note_page.html', {'form': form})


def filter_note(request):
    if request.method == 'GET':
        filtered = Note.objects.filter(category__title=request.GET.get('category'))
        if filtered:
            categories = Category.objects.all()
            return render(request, 'index.html', {'notes_list': filtered, 'categories': categories})
        else:
            return HttpResponseRedirect(reverse('index'))


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('index'))


def search_note(request):
    if request.method == 'GET':
        search = Note.objects.filter(title=request.GET.get('title', ''))
        if search:
            categories = Category.objects.all()
            return render(request, 'index.html', {'notes_list': search, 'categories': categories})
        else:
            return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.POST == 'post':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            HttpResponse('Invalid login or password')