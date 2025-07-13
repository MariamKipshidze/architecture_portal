from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name="Project Title", max_length=200)
    description = models.TextField(verbose_name="Description")
    location = models.CharField(verbose_name="Location", max_length=200, blank=True)
    client = models.CharField(verbose_name="Client", max_length=200, blank=True)
    start_date = models.DateField(verbose_name="Start Date", null=True, blank=True)
    end_date = models.DateField(verbose_name="End Date", null=True, blank=True)
    is_published = models.BooleanField(verbose_name="Is Published", default=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Project"
    )
    image = models.ImageField(verbose_name="Image", upload_to='project_images/')
    caption = models.CharField(verbose_name="Caption", max_length=255, blank=True)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Image for {self.project.title}"

