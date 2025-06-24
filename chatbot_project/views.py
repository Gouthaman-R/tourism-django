from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from transformers import pipeline

# Load the GPT-2 model using Hugging Face
chatbot = pipeline('text-generation', model='gpt2')

def get_response(request):
    if request.method == "POST":
        # Get the message sent by the user
        user_message = request.POST.get('message', '')
        
        if user_message:
            # Get the GPT-2 model's response
            output = chatbot(user_message, max_length=100, num_return_sequences=1)[0]['generated_text']
            
            # Return the model's response as JSON
            return JsonResponse({'response': output.strip()})
        else:
            return JsonResponse({'response': "Sorry, I couldn't understand that."})
    return JsonResponse({'response': 'Invalid request method.'})
