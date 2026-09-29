from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "job_title",
        "status",
        "employment_type",
        "application_date",
        "interview_date",
    )

    list_filter = (
        "status",
        "employment_type",
        "application_date",
    )

    search_fields = (
        "company_name",
        "job_title",
        "location",
    )

    ordering = ("-application_date",)