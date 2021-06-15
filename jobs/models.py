from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _  # to make it easy for text in your site to be translated

# Create your models here.
class MtoJobCategories(models.Model):
    category_name = models.CharField(_('category'), max_length=20, help_text='e.g Data entry')

    def __str__(self):
        return self.category_name


class Microtasks(models.Model):
    job_name = models.CharField(max_length=300, help_text='e.g develop website')
    cat_id = models.ForeignKey(MtoJobCategories, on_delete=models.CASCADE)
    target_date = models.DateTimeField(null=True, help_text='e.g 2021-10-25 14:30:59')
    time_required = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], )
    job_description = models.CharField(_('job description'), max_length=1000,
                                       help_text='e.g car website', )
    upload_job_sample = models.FileField(upload_to='job_documents/job_samples/', )
    upload_job_instructions = models.FileField(upload_to='job_documents/job_instructions/', )
    Quantity_of_the_Job = models.IntegerField(default=0) 
    type_of_TC = models.CharField(_('type of tc to be done'), max_length=500,
                                  help_text='e.g Senior developer, tester & client')
    number_of_people_required = models.PositiveIntegerField(validators=[MinValueValidator(1)],
                                                            help_text='e.g 2')
    skills = models.CharField(_('skills'), max_length=500, help_text='e.g coding, data entry')
    job_cost_AED = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], )
    

    def __str__(self):
        return f'{self.job_name}'

class MAL_Requirements(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    MAL_Job_Identification_Number = models.CharField(max_length=50, blank=False, validators=[alphanumeric])
    Assembly_line_ID = models.CharField(max_length=50, blank=False, validators=[alphanumeric])
    Name_of_the_Assembly_line = models.TextField()
    Name_of_the_person_incharge_of_the_MAL = models.TextField()
    Link_of_the_output_folder = models.FilePathField(path='job_documents/output')
    microtask  = models.ForeignKey(Microtasks,max_length=100,on_delete=models.CASCADE,related_name='microtask')
    microtask_category = models.ForeignKey(Microtasks,max_length=100,on_delete=models.CASCADE,related_name='category')
    Target_date = models.DateField()
    Total_budget_allocated_for_the_job = models.IntegerField()
    Job_description = models.TextField()
    Uploadjob_sample = models.FileField(upload_to='jobsample')
    UploadJob_instructions = models.FileField(upload_to='jobsinstruction')
    Quantity_of_the_Job = models.IntegerField()
    Link_of_the_Input_folder = models.FilePathField(path='job_documents/input')

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Mal Requiremet'
        verbose_name_plural= 'Mal Requiremets'

    def __str__(self):
        return self.Job_description
