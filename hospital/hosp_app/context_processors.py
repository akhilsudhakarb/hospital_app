from .models import Department

def cat(request):
    departments = Department.objects.all()
    return {'dept': departments}