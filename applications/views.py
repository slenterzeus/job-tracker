from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def application_list(request):

    applications = JobApplication.objects.filter(
        user=request.user
    ).order_by("-application_date")

    # Search
    search_query = request.GET.get("search", "").strip()

    if search_query:
        applications = applications.filter(
            Q(company_name__icontains=search_query)
            | Q(job_title__icontains=search_query)
            | Q(location__icontains=search_query)
        )

    # Status filter
    status_filter = request.GET.get("status", "").strip()

    if status_filter:
        applications = applications.filter(
            status=status_filter
        )

    # Pagination - 5 applications per page
    paginator = Paginator(applications, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "applications": page_obj,
        "page_obj": page_obj,
        "search_query": search_query,
        "status_filter": status_filter,
    }

    return render(
        request,
        "applications/application_list.html",
        context
    )


@login_required
def application_create(request):

    if request.method == "POST":

        form = JobApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.user = request.user

            application.save()

            messages.success(
                 request,
                "Job application added successfully."
            )

        return redirect("application_list")

    else:

        form = JobApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form
        }
    )


@login_required
def application_update(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            messages.success(
                 request,
                "Job application updated successfully."
            )

        return redirect("application_list")

    else:

        form = JobApplicationForm(
            instance=application
        )

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "edit_mode": True
        }
    )


@login_required
def application_delete(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        application.delete()

        messages.success(
            request,
            "Job application deleted successfully."
        )

        return redirect("application_list")

    return render(
        request,
        "applications/application_confirm_delete.html",
        {
            "application": application
        }
    )