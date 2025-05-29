# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils import timezone
# from django.http import response

# # Temporary message store (use DB in real app)
# latest_message = {"text": "", "timestamp": None}

# '''@csrf_exempt
# def receive_message(request):
#     if request.method == "POST":
#         message_body = request.POST.get("Body")
#         if message_body:
#             latest_message["text"] = message_body
#             latest_message["timestamp"] = timezone.now()
#             return JsonResponse({"status": "success", "received": message_body})
#     else:
#         return JsonResponse({"status": "error", "reason": "Only POST allowed"})
# '''
# @csrf_exempt
# def receive_message(request):
#     # Dump everything we got
#     method = request.method
#     post_dict = request.POST.dict()            # parsed form fields
#     raw_body = request.body.decode('utf-8')     # raw payload
    
#     print("=== Twilio webhook hit ===")
#     print("Method:", method)
#     print("POST fields:", post_dict)
#     print("Raw body: ", raw_body)
    
#     # Respond with a JSON echo for our debugging client
#     return JsonResponse({
#         "status": "debug",
#         "method": method,
#         "post": post_dict,
#         "body": raw_body
#     })

# # def  receive_message(request):
# #     return response("hello world")
# def get_latest_message(request):
#     return JsonResponse(latest_message)
# whatsapp/views.py
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# In‐memory store; replace with a Model for production
latest_message = {"text": "", "timestamp": None}

@csrf_exempt
def receive_message(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    
    body = request.POST.get("Body")
    if not body:
        return JsonResponse({"status": "error", "reason": "No Body parameter"}, status=400)
    
    latest_message["text"] = body
    latest_message["timestamp"] = timezone.now()
    return JsonResponse({"status": "success"})
def get_latest_message(request):
    return JsonResponse(latest_message)
