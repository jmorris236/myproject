# behavior_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Note, Behavior
from .forms import NoteForm, AddStudentsForm
from django.contrib.auth.decorators import login_required


@login_required
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'student_list.html', {'students': students})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    notes = student.notes.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = student
            note.save()
            return redirect('student_detail', pk=pk)
    else:
        form = NoteForm()

    return render(request, 'student_detail.html', {'student': student, 'notes': notes, 'form': form})


@login_required
def student_add(request):
    if request.method == 'POST':
        form = AddStudentsForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student_list')
    else:
        form = AddStudentsForm()

    return render(request, 'student_add.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_delete.html', {'student': student})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, student__user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('student_detail', pk=note.student.pk)

    return render(request, 'note_delete.html', {'note': note})


def default_page(request):
    return render(request, 'default_page.html')
