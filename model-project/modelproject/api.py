from db_manage import redis_manage
from django.http import JsonResponse, HttpResponse

def upload_dir_memory(request):
    value = request.body
    print(value)
    db_obj = redis_manage.REDIS_MANAGE()
    db_obj.set_dir_memory(value)

    return HttpResponse("Sucess")

def get_dir_memory(request):
    db_obj = redis_manage.REDIS_MANAGE()
    