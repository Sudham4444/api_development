from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'enroll/student_manage.html'
    context_object_name = 'students'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'enroll/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'enroll/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'enroll/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
