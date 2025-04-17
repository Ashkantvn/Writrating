from django.db import models


class Report(models.Model):
    report_title = models.CharField(max_length=100)
    report_content = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.report_title
