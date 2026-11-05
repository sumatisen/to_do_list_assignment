from django.db import models
from django.utils import timezone


class Task(models.Model):
    """Model representing a daily task item in the To-Do List."""
    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, help_text="Detailed description of the task (optional)")
    done = models.BooleanField(default=False, verbose_name="Done")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")

    class Meta:
        ordering = ['done', '-created_at']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

    @property
    def created(self):
        """Format creation timestamp as YYYY-MM-DD HH:MM for template display."""
        if self.created_at:
            return self.created_at.strftime('%Y-%m-%d %H:%M')
        return ""
