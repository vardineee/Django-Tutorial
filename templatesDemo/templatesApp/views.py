from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict = {"name": "Varduhi"}
    return render(request,'templatesApp/firstTemplate.html', context = myDict)


def renderemployee(request):
    myDict = {"id": 5, "name": "Joe", "salary": 55}
    return render(request, 'templatesApp/employeeTemplate.html', myDict)
