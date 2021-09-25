from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=D41B438E-031F-4CB7-BD18-4182DFFEB85D')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error ...'

        if api[0]['Category']['Name'] == 'Good': 
            category_description = '(0-50) Air quality is satisfactory, and air pollution poses little or no risk.'
            category_color = 'good'
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = '(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            category_color = 'moderate'
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups': 
            category_description = '(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_color = 'usg'
        elif api[0]['Category']['Name'] == 'Unhealthy': 
            category_description = 	'(1515-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = 'unhealthy'
        elif api[0]['Category']['Name'] == 'Very Unhealthy': 
            category_description = '(201-300) Health alert: The risk of health effects is increased for everyone.'
            category_color = 'very_unhealthy'
        elif api[0]['Category']['Name'] == 'Hazardous': 
            category_description = '(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected.'
            category_color = 'hazardous'

        return render(request, 'home.html', {'api': api,
        'category_color': category_color,
        'category_description': category_description})
    else:
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D41B438E-031F-4CB7-BD18-4182DFFEB85D')
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error ...'

        if api[0]['Category']['Name'] == 'Good': 
            category_description = '(0-50) Air quality is satisfactory, and air pollution poses little or no risk.'
            category_color = 'good'
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = '(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            category_color = 'moderate'
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups': 
            category_description = '(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_color = 'usg'
        elif api[0]['Category']['Name'] == 'Unhealthy': 
            category_description = 	'(1515-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = 'unhealthy'
        elif api[0]['Category']['Name'] == 'Very Unhealthy': 
            category_description = '(201-300) Health alert: The risk of health effects is increased for everyone.'
            category_color = 'very_unhealthy'
        elif api[0]['Category']['Name'] == 'Hazardous': 
            category_description = '(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected.'
            category_color = 'hazardous'

        return render(request, 'home.html', {'api': api,
        'category_color': category_color,
        'category_description': category_description})

def about(request):
    return render(request, 'about.html', {})