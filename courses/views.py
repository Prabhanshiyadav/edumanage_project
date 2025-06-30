from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'instructor', 'duration']  # ✅
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'instructor_name', 'duration']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
