from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=100, db_index=True, help_text='The todo task') #, null=True, blank=True,
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False, help_text='The todo task status')

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'

    def __str__(self) -> str:
        return self.task

