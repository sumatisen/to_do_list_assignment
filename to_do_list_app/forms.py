from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Form used for creating new tasks."""

    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
                'required': True,
                'id': 'task-title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description (optional)...',
                'rows': 4,
                'id': 'task-description',
            }),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
        }


class TaskEditForm(forms.ModelForm):
    """Form used for updating existing tasks, including status."""

    class Meta:
        model = Task
        fields = ['title', 'description', 'done']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
                'required': True,
                'id': 'task-title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description...',
                'rows': 4,
                'id': 'task-description',
            }),
            'done': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
                'id': 'task-done',
            }),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'done': 'Done',
        }
