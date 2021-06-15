from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MicrotasksForm
from .models import Microtasks,MAL_Requirements
# Create your views here.

def microtask(request):
    if request.method == 'POST':
        form = MicrotasksForm(request.POST, request.FILES)
        if form.is_valid():

            job_name = form.cleaned_data['job_name']

            form.save()
            messages.success(request, f'Account created for {job_name}! You have to login')
            return redirect('/')
    else:
        form = MicrotasksForm()

    return render(request, 'microtask.html', {'form': form})


def index(request):
    microtask = Microtasks.objects.all()
    # category = MAL_Requirements.objects.get(microtask.Category_of_the_microtask)

    context = {'microtask':microtask}
    return render(request, 'MalForm.html', context)

def handleSubmit(request):
    if request.method == 'POST':
        MAL_Job_Identification_Number = request.POST['malno']
        Assembly_line_ID = request.POST['asi']
        Name_of_the_Assembly_line = request.POST['nameassembly']
        Name_of_the_person_incharge_of_the_MAL = request.POST['personname']
        Link_of_the_output_folder = request.POST['link1']
        Name_of_the_micro_task = request.POST['microtask']
        Category_of_the_Microtask = request.POST['category']
        Target_date = request.POST['td']
        Total_budget_allocated_for_the_job = request.POST['budget']
        Job_description = request.POST['jd']
        Upload_job_sample = request.POST['jobsample']
        Upload_Job_instructions = request.POST['instruction']
        Quantity_of_the_Job = request.POST['quantity']
        Link_of_the_Input_folder = request.POST['link2']
        data = MAL_Requirements(
                        MAL_Job_Identification_Number=MAL_Job_Identification_Number, 
                        Assembly_line_ID=Assembly_line_ID,
                        Name_of_the_Assembly_line=Name_of_the_Assembly_line, 
                        Name_of_the_person_incharge_of_the_MAL=Name_of_the_person_incharge_of_the_MAL, 
                        Link_of_the_output_folder=Link_of_the_output_folder,
                        microtask=Name_of_the_micro_task, 
                        microtask_category=Category_of_the_Microtask, 
                        Target_date=Target_date, 
                        Total_budget_allocated_for_the_job=Total_budget_allocated_for_the_job,
                        Job_description=Job_description,
                        Uploadjob_sample=Upload_job_sample, 
                        UploadJob_instructions=Upload_Job_instructions, 
                        Quantity_of_the_Job=Quantity_of_the_Job, 
                        Link_of_the_Input_folder=Link_of_the_Input_folder
                        )
        data.save()
    return redirect('index')
    
def posting_page(request,pk=None):
    if request.user.is_active:    
        if pk is not None:
            try:
                data = Microtasks.objects.get(id=pk)
            except:
                data = "NA"
            return render(request,'JobPosting_Page.html', {'datas': data})
    return render(request,'JobPosting_Page.html')    