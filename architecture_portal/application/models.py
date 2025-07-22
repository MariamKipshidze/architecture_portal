from django.db import models
from django.core.validators import MinLengthValidator


class Application(models.Model):
    # Project Types (you can expand this list)
    PROJECT_TYPES = [
        ('RESIDENTIAL', 'Residential'),
        ('COMMERCIAL', 'Commercial'),
        ('INSTITUTIONAL', 'Institutional'),
        ('OTHER', 'Other'),
    ]

    # Client Information
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)

    # Project Information
    project_title = models.CharField(max_length=200)
    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES,
        default='RESIDENTIAL'
    )
    project_description = models.TextField(
        validators=[MinLengthValidator(20, "Description must be at least 20 characters")]
    )

    # Administrative Fields
    viewed = models.BooleanField(
        default=False,
        verbose_name="Processed",
        help_text="Mark as True when application has been reviewed"
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Internal admin notes about this application"
    )

    class Meta:
        verbose_name = "Project Application"
        verbose_name_plural = "Project Applications"
        ordering = ['-submission_date']
        permissions = [
            ("can_mark_processed", "Can mark application as processed"),
        ]

    def __str__(self):
        return f"{self.project_title} by {self.client_name} ({'✔' if self.viewed else '✖'})"
