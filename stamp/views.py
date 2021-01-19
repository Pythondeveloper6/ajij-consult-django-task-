from django.shortcuts import render
from . models import Stamp , Theme
from django.http import JsonResponse
from django.template.loader import render_to_string

def stamp_list_filter(request):
    ''' the view filter the themes using the jquery autocomplete widget & return the stamps for the selected them using ajax  '''

    # filter the theme name using the jquery autocompelete widget
    if 'term' in request.GET:
        qs = Theme.objects.filter(name__icontains=request.GET.get('term'))
        themes = [theme.name for theme in qs]
        return JsonResponse(themes, safe=False)


    # check if the request came from ajax and filter the stamps using the theme name 
    if request.method == "GET" and request.is_ajax():
        theme = request.GET.get('theme')
        stamps = Stamp.objects.filter(theme__name=theme)
        
        context = {'stamps':stamps}
        html = render_to_string('stamp/stamp_table_list.html' , context , request=request)
        return JsonResponse({'form':html})
    
    # the the request not for the automcomplete widget or not for the ajax call , return all the stamps  
    else:
        stamps = Stamp.objects.all()
        context = {'stamps':stamps}
    return render(request,'stamp/stamp_list.html',context)