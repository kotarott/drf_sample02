from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=150)
    jod_description = models.TextField()
    salary = models.FloatField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.company_name } : { self.job_title }"
