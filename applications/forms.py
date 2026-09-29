from django import forms

from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "company_name",
            "job_title",
            "job_url",
            "location",
            "employment_type",
            "status",
            "application_date",
            "interview_date",
            "salary",
            "notes",
        ]

        widgets = {
            "company_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Google",
                }
            ),

            "job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Python Developer",
                }
            ),

            "job_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/job",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Bangalore",
                }
            ),

            "employment_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "application_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "interview_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "salary": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 500000",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Add notes about this application...",
                }
            ),
        }