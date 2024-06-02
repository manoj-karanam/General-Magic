from django.db import models


class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Only store the hashed password

    class Meta:
        unique_together = ('email',)

    def __str__(self):
        return f"{self.fullname} ({self.email})"


class UserDetails(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    child_id = models.CharField(max_length=50, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_user_id()
        super(UserDetails, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_id})"

    def generate_user_id(self):
        return (self.last_name[:4] + self.birthday.strftime('%Y')).lower()
    


# class Experience(models.Model):
#     EMPLOYMENT_TYPE_CHOICES = [
#         ('full-time', 'Full-Time'),
#         ('part-time', 'Part-Time'),
#         ('internship', 'Internship'),
#         ('self-employed', 'Self-Employed'),
#         ('freelance', 'Freelance'),
#     ]
    
#     LOCATION_TYPE_CHOICES = [
#         ('on-site', 'On-site'),
#         ('hybrid', 'Hybrid'),
#         ('remote', 'Remote'),
#     ]

#     user_id = models.CharField(max_length=50)
#     title = models.CharField(max_length=255)
#     employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES)
#     company_name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     location_type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#     job_description = models.TextField()
#     skills = models.TextField()

#     def __str__(self):
#         return f"{self.title} at {self.company_name}"
    


# class Education(models.Model):
#     user_id = models.OneToOneField(Registration, on_delete=models.CASCADE, primary_key=True, related_name='education')
#     school_name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=100)
#     field_of_study = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#     grade = models.CharField(max_length=50, blank=True)
#     description = models.TextField(blank=True)
#     skills = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.degree} in {self.field_of_study} at {self.school_name}"
    

