from django.shortcuts import render, redirect

from charts.models import City, Sales


def index(request):  
    """
    This view handles the rendering of an 'index' page with city data and sales information.
    
    Args:
        request: An HTTP request object.
        
    Returns:
        A rendered HTML template displaying city data and sales information.
    """
    cities = City.objects.all() 
    context = { 
        'cities': cities, 
    } 
    if request.method == "POST":  
        selected_cities = request.POST.getlist('city')  
        data = {} 
        for city_name in selected_cities:  
            city = City.objects.get(name=city_name) 
            sales = Sales.objects.filter(city=city) 
            data[city_name] = {  
                'years': [],  
                'plan': [],  
                'fact': []  
            }  
            for sale in sales:  
                data[city_name]['years'].append(sale.year)  
                data[city_name]['plan'].append(float(sale.plan))  
                data[city_name]['fact'].append(float(sale.fact)) 
        # Save 'data' to the session for future use 
        request.session['data'] = data 
        # Redirect to the 'index' page using a GET request 
        return redirect('charts:index')  
    # If 'data' exists in the session, add it to the context 
    if 'data' in request.session: 
        context['data'] = request.session['data'] 
        # Optionally: Remove data from the session after use 
        del request.session['data'] 
    return render(request, 'index.html', context)
