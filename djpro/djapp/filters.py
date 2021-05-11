from .models import jobPost
import django_filters


class job_filter(django_filters.FilterSet):
    class Meta():
        model = jobPost
        fields = ['company', 'position', 'location']
