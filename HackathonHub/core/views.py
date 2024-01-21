import textwrap
from IPython.display import Markdown
import google.generativeai as genai
from .models import ClassSchedule

from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import textwrap
from IPython.display import Markdown
import google.generativeai as genai

# chat_project/chat_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
import textwrap
from IPython.display import Markdown
import openai

def to_markdown(text):
    text = text.replace('•', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_chatgpt_response(user_input):
    # Set your OpenAI GPT-3 API key
    openai.api_key = "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"

    # Make a request to the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=user_input,
        max_tokens=50
    )

    return response.choices[0].text

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Use ChatGPT to generate a response
        response = generate_chatgpt_response(user_input)

        # Convert the response to Markdown
        markdown_response = to_markdown(response)

        return JsonResponse({'response': str(markdown_response)})

    return render(request, 'chat.html')

# Create your views here.

@login_required
def index(request):
    return  render(request,"core/index.html")


from .models import Subject, ClassSchedule, Faculty

@login_required
def subjects_and_schedules(request):
    # Fetch all subjects
    subjects = Subject.objects.all()

    # Fetch all class schedules
    class_schedules = ClassSchedule.objects.all()

    # Fetch all faculty members
    faculties = Faculty.objects.all()

    # You can add more context data if needed

    context = {
        'subjects': subjects,
        'class_schedules': class_schedules,
        'faculties': faculties,
    }
    print(context)
    return render(request, 'core/index.html', context)

# views.py

def assigments(request):
    return render(request,"assigment.html")




def calendra(request):
    return render(request,"calendar.html")