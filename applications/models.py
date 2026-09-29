from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("APPLIED", "Applied"),
        ("SCREENING", "Screening"),
        ("INTERVIEW", "Interview"),
        ("OFFER", "Offer"),
        ("REJECTED", "Rejected"),
        ("WITHDRAWN", "Withdrawn"),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ("FULL_TIME", "Full Time"),
        ("PART_TIME", "Part Time"),
        ("INTERNSHIP", "Internship"),
        ("CONTRACT", "Contract"),
        ("REMOTE", "Remote"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications"
    )

    company_name = models.CharField(max_length=150)

    job_title = models.CharField(max_length=150)

    job_url = models.URLField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default="FULL_TIME"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="APPLIED"
    )

    application_date = models.DateField()

    interview_date = models.DateField(
        blank=True,
        null=True
    )

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"