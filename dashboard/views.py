from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.utils import timezone

from applications.models import JobApplication


@login_required

def home_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    return render(
        request,
        "dashboard/home.html"
    )


def dashboard_view(request):

    applications = JobApplication.objects.filter(
        user=request.user
    )

    # Statistics
    total_applications = applications.count()

    total_interviews = applications.filter(
        status="INTERVIEW"
    ).count()

    total_offers = applications.filter(
        status="OFFER"
    ).count()

    # Recent applications
    recent_applications = applications.order_by(
        "-application_date"
    )[:5]

    # Upcoming interviews
    upcoming_interviews = applications.filter(
        interview_date__gte=timezone.localdate()
    ).order_by(
        "interview_date"
    )[:5]

    # Status statistics
    status_counts = {
        "Applied": applications.filter(
            status="APPLIED"
        ).count(),

        "Screening": applications.filter(
            status="SCREENING"
        ).count(),

        "Interview": applications.filter(
            status="INTERVIEW"
        ).count(),

        "Offer": applications.filter(
            status="OFFER"
        ).count(),

        "Rejected": applications.filter(
            status="REJECTED"
        ).count(),

        "Withdrawn": applications.filter(
            status="WITHDRAWN"
        ).count(),
    }

    context = {
        "total_applications": total_applications,
        "total_interviews": total_interviews,
        "total_offers": total_offers,
        "recent_applications": recent_applications,
        "upcoming_interviews": upcoming_interviews,
        "status_counts": status_counts,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )