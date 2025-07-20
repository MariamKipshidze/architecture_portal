from django.db import models


class TeamMember(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    position = models.CharField(verbose_name="Position", max_length=100)
    bio = models.TextField(verbose_name="bio")
    photo = models.ImageField(verbose_name="photo", upload_to='team_photos/')
    is_active = models.BooleanField(verbose_name="Active", default=True)
    order = models.PositiveIntegerField(verbose_name="Order", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.position}"
