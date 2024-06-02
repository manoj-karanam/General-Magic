from django.db import models


class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Only store the hashed password

    class Meta:
        unique_together = ('email',)

    def __str__(self):
        return f"{self.fullname} ({self.email})"
    
class Experience(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('internship', 'Internship'),
        ('self-employed', 'Self-Employed'),
        ('freelance', 'Freelance'),
    ]
    
    LOCATION_TYPE_CHOICES = [
        ('on-site', 'On-site'),
        ('hybrid', 'Hybrid'),
        ('remote', 'Remote'),
    ]

    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    location_type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company_name}"