from django.http import JsonResponse
import datetime

def current_datetime(request):
	time = datetime.datetime.now()
	text = "It is now %s." % time
	json = {'status': "OK", 'message': "Correct checking", 'time': text }
	return JsonResponse(json)