from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import response

# Temporary message store (use DB in real app)
latest_message = {"text": "", "timestamp": None}

# @csrf_exempt
# def receive_message(request):
#     if request.method == "POST":
#         message_body = request.POST.get("Body")
#         if message_body:
#             latest_message["text"] = message_body
#             latest_message["timestamp"] = timezone.now()
#             return JsonResponse({"status": "success"})
#     return JsonResponse({"status": "error"})

def  receive_message(request):
    return response("hello world")
def get_latest_message(request):
    return JsonResponse(latest_message)
