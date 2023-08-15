from django.shortcuts import render
from .models import City, Year, Plan, Fact

def index(request):
    cities = City.objects.all()
    if request.method == "POST":
        selected_cities = request.POST.getlist('city')
        data = {}
        for city_name in selected_cities:
            city = City.objects.get(name=city_name)
            years = Year.objects.filter(city=city)
            data[city_name] = {
                'years': [],
                'plan': [],
                'fact': []
            }
            for y in years:
                data[city_name]['years'].append(y.year)
                plan = Plan.objects.filter(year=y).first()
                fact = Fact.objects.filter(year=y).first()
                data[city_name]['plan'].append(plan.amount if plan else 0)
                data[city_name]['fact'].append(fact.amount if fact else 0)

        return render(request, 'index.html', {'cities': cities, 'data': data}) 
    return render(request, 'index.html', {'cities': cities})