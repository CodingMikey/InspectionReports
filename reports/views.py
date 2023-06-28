from django.shortcuts import render, get_object_or_404, redirect
from .models import InspectionReport
from .forms import InspectionReportForm

def report_list(request):
    reports = InspectionReport.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(InspectionReport, pk=pk)
    return render(request, 'reports/report_detail.html', {'report': report})

def report_create(request):
    form = InspectionReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('report_list')
    return render(request, 'reports/report_form.html', {'form': form})

def report_update(request, pk):
    report = get_object_or_404(InspectionReport, pk=pk)
    form = InspectionReportForm(request.POST or None, instance=report)
    if form.is_valid():
        form.save()
        return redirect('report_list')
    return render(request, 'reports/report_form.html', {'form': form, 'report': report})

def report_delete(request, pk):
    report = get_object_or_404(InspectionReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
