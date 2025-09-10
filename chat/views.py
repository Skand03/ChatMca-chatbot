from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# Azure settings from .env
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)

def index(request):
    return render(request, "chat/index.html")

@require_POST
def ask(request):
    data = json.loads(request.body.decode("utf-8"))
    user_message = data.get("message", "").strip()

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        max_completion_tokens=16384

    )

    assistant_reply = response.choices[0].message.content
    return JsonResponse({"reply": assistant_reply})
