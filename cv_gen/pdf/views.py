from django.shortcuts import redirect, render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import description_generator as dg
import json

# def base(request):
#     return render(request,'pdf/base.html')

def home(request):
    return render(request,'pdf/home.html')

@login_required
def accept(request):
    if request.method == "GET":
        return render(request,'pdf/accept.html')
    if request.method == "POST":
        author = request.user.username
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        total_experience = request.POST.get("total_experience","")
        experience = request.POST.get("experience","")
        skills = request.POST.get("skills","")
        soft_skills = request.POST.get("soft_skills","")


        profile = Profile(author=author, name=name, email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,total_experience=total_experience,experience=experience,skills=skills,soft_skills=soft_skills)
        profile.save()
        profiles = Profile.objects.all()
        return redirect('pdf:list')

def resume(request,id):

    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    
    config = pdfkit.configuration(wkhtmltopdf='C:/Users/DrashtiGor/Downloads/wkhtmltox/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response
    
@login_required
def list(request):
    profiles = Profile.objects.filter(author=request.user.username)
    return render(request,'pdf/list.html',{'profiles':profiles})

@csrf_exempt
def delete_resume(request, id):
    if request.method == 'DELETE':
        try:
            resume = Profile.objects.get(id=id)
            resume.delete()
            return JsonResponse({'message': 'Object deleted successfully'}, status=200)
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'Object not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
            

@csrf_exempt
def generate_summary(request, skill_list, n):
    if request.method == 'GET':
        # print(type(skill_list))
        skill_list = skill_list.split(',')
        # print(skill_list)
        summary = dg.gen_description(skill_list, n)
        # print(summary)
        json_data = json.dumps({'summary': summary})
        return JsonResponse(json_data, status=200, safe = False)