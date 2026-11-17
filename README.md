# Ex.03 Design a Website for Server Side Processing
## Date: 12/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
    <head>
        <title>Calculation1</title>
    </head>
    <body>
        <center>
            <h1>KANISHKA B</h1>
            <h1>(26010203)</h1>
        
        <form method="POST">
            {%csrf_token%}
            <label>Initial_Customer</label>
            <input type="number" name="initial_Customer" value="{{ initial }}" required> <br><br>
            <label>Present_Customer</label>
            <input type="number" name="present_Customer" value="{{ present }}" required> <br><br>
            <h2>Calculate Churn Rate</h2>
            <input type="submit" value="Calculate" >
            <input type="text" value="{% if result is not None %}{{ result }}%{% endif %}" readonly>
            <input type="reset" value="Clear All">



        </form> 
        {% if result is not None %}
            <h2>Churn Rate: {{ result }}%</h2>
        {% endif %}
        </center>
    </body>
</html>
```
python
```
from django.shortcuts import render

def calculate_Churn(request):
    result = None
    initial = ""
    present = ""
    if request.method == "POST":
        initial = request.POST.get("initial_Customer")
        present = request.POST.get("present_Customer")
        if initial and present and int(initial) != 0:
            result = round(((int(initial) - int(present)) / int(initial)) * 100, 2)
    return render(request, "mysivan/mysivan.html", {
        "result": result,
        "initial": initial,
        "present": present
    })
from django.contrib import admin
from django.urls import path
from mysivan import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_Churn,name='calculate'),
]

```

## OUTPUT 
![alt text](<Screenshot (15).png>)
![alt text](<Screenshot (14).png>)



## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
