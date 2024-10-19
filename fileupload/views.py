import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import UploadFileForm
from .models import UploadFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Process the uploaded file
            file_instance = form.instance
            df = pd.read_excel(file_instance.file.path)  # For Excel files
            # df = pd.read_csv(file_instance.file.path)  # Uncomment for CSV

            # Generate the summary report
            report = generate_report(df)

            # Send the report via email
            send_report_via_email(report)

            return render(request, 'fileupload/success.html', {'report': report})
    else:
        form = UploadFileForm()

    return render(request, 'fileupload/upload.html', {'form': form})

def generate_report(df):
    total_records = df.shape[0]
    dpd_sum = df['DPD'].sum()
    dpd_avg = df['DPD'].mean()
    dpd_max = df['DPD'].max()

    summary = {
        'total_records': total_records,
        'dpd_sum': dpd_sum,
        'dpd_avg': dpd_avg,
        'dpd_max': dpd_max
    }
    return summary

def send_report_via_email(report):
    subject = 'Python Assignment - Your Name'
    message = f"""
    Summary Report:
    Total Records: {report['total_records']}
    Total DPD: {report['dpd_sum']}
    Average DPD: {report['dpd_avg']}
    Maximum DPD: {report['dpd_max']}
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['vkorat50@gmail.com'],
        fail_silently=False,
    )
