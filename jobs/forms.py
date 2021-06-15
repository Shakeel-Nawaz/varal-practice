from django.forms import ModelForm

from .models import Microtasks


class MicrotasksForm(ModelForm):
    class Meta:
        model = Microtasks
        fields = ['job_name', 'cat_id', 'target_date', 'job_cost_AED', 'time_required', 'skills', 'number_of_people_required', 'job_description', 'upload_job_sample', 'upload_job_instructions', 'type_of_TC']
