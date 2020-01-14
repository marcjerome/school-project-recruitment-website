from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, help_text= "Name of the subject")

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, help_text= "Name of the project")
    slug = models.SlugField(max_length=280, null=False, blank=True, unique=True)
    date = models.DateField(null=False, blank=False, help_text="Date when the project was started")
    access_code = models.CharField(max_length=6, blank=True, help_text="Code for accessing the project. This prevents spamming")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, help_text="The subject of the project ")
    is_completed = models.BooleanField(default=False, null=False, blank=False)
    members = models.ManyToManyField(User, through='Membership')

    class Meta:
        verbose_name_plural = 'Projects'
        unique_together = ['name', 'slug']

    def get_all():
        return Project.objects.all()

    def save(self):
        self.slug = slugify(self.name)
        super().save()
       

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    proposal_text = models.TextField(null=False, blank=False, help_text="The proposal of the User for joining a project")
    is_approve = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        unique_together = ['user', 'project']

    def __str__(self):
        return '[' + self.user.username + '] ' + ' [' + self.project.name + ']'