from django.shortcuts import render
from . models import Stamp , Theme
from django.http import JsonResponse
from django.template.loader import render_to_string

def stamp_list(request):

    if 'term' in request.GET:
        qs = Theme.objects.filter(name__icontains=request.GET.get('term'))
        print(request.GET.get('term'))
        themes = [theme.name for theme in qs]
        return JsonResponse(themes, safe=False)

    themes = Theme.objects.all()
    stamps = Stamp.objects.all()
    
    if request.method == "GET" and request.is_ajax():
        theme = request.GET.get('theme')
        stamps = Stamp.objects.filter(theme__name=theme)
        
        context = {'themes':themes , 'stamps':stamps}
        html = render_to_string('stamp/stamp_table_list.html' , context , request=request)
        return JsonResponse({'form':html})
    
    else:
        context = {'themes':themes , 'stamps':stamps}
    return render(request,'stamp/stamp_list.html',context)