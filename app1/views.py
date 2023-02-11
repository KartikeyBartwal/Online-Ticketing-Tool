from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from keras.models import load_model
import random
# Load the model from the .h5 file
model = load_model("C:\\Users\\hp\\Priority of ticket.h5")

all_tickets = [
 	['TI1002' ,	'Request', 	'Junior', 	'Critical', 	'Hardware' ,	'10', 	'very high'],
	['TI1001' ,	'Issue' ,	'Senior', 	'Minor' ,	'Software' 	,'7', 	'high'],
	['TI203', 	'Request', 	'Junior', 	'Normal', 	'Hardware' 	,'8' ,	'normal'],
	['TI513' ,	'Request', 	'Senior', 	'Normal', 	'Software' 	'10' ,	'normal'],
	['TI1000' ,	'Issue', 	'Management', 	'Minor', 	'Access/Login' ,	'2' ,	'low'],
]
# For priority ordering

# def array_to_html_table(array):
#     # Start the table
#     html = "<table>"

#     # Add the header row
#     html += "<tr>"
#     for header in array[0]:
#         html += "<th>" + str(header) + "</th>"
#     html += "</tr>"

#     # Add the data rows
#     for row in array[1:]:
#         html += "<tr>"
#         for cell in row:
#             html += "<td>" + str(cell) + "</td>"
#         html += "</tr>"

#     # End the table
#     html += "</table>"

#     return html

# all_tickets = [
#  	['TI1002' ,	'Request', 	'Junior', 	'Critical', 	'Hardware' ,	'10', 	'very high'],
# 	['TI1001' ,	'Issue' ,	'Senior', 	'Minor' ,	'Software' 	,'7', 	'high'],
# 	['TI203', 	'Request', 	'Junior', 	'Normal', 	'Hardware' 	,'8' ,	'normal'],
# 	['TI513' ,	'Request', 	'Senior', 	'Normal', 	'Software' 	'10' ,	'normal'],
# 	['TI1000' ,	'Issue', 	'Management', 	'Minor', 	'Access/Login' ,	'2' ,	'low'],
# ]

# html = array_to_html_table(all_tickets)
# print(html)

def addTicketandSortPriority(ticket,all_tickets):
   mydict= {
    "Issue" : 1,
    "Request": 2,
    'Junior' :1,
    'Regular' : 2,
    'Senior' : 3,
    'Management':4,
    '0 - Unclassified': 0,
    "1 - Minor" : 1,
    "2 - Normal" : 2,
    "3 - Major" : 3,
    "4 - Critical" : 4,
    'Access/Login' : 1,
    'Hardware' : 3,
    'Software' : 2,
    'Systems': 4,
    "Low": 1,
    "Medium": 2,
    "High": 3,
   }
    # Generate a unique ticket id
   ticket_id = "TI" + random.randint(1000)
   # Predicting its priority
   input_ = []
   for detail in ticket:
        input_.append(mydict[detail])
   priority = model.predict(input_)
   ticket.append(ticket_id)
   ticket.append(priority)
   all_tickets.sort(key=lambda x: x[-1])



# Now send this array to 

# Create your views here.
def HomePage (request):
    return render (request,'user.html')

def FAQPage(request):
    return render (request,"FAQ.html")

def AdminDashboard(request):
    return render(request,"Admin Dashboard.html")

def AdminTicketDashboard(request):
    return render(request,"Admin Ticket Dashboard.html")

def TicketHistoryPage(request):
    return render (request,"Ticket History.html")

def FileticketPage(request):
    TicketType = request.GET.get('TicketType')
    RequestorSeniority = request.GET.get('RequestorSeniority')
    Severity = request.GET.get("Severity")
    FiledAgainst = request.GET.get("FiledAgainst")

    print(TicketType,RequestorSeniority,Severity,FiledAgainst)

    # addTicketandSortPriority(ticket,all_tickets)
    return render(request,"File ticket.html")


def AdminTicketTable(request):
    return render(request,"Admin Ticket table.html")

def AboutPage(request):
    return render(request,"index.html")

def SignupPage(request):
    if(request.method == "POST"):
        uname =  request.POST.get('username')
        email =  request.POST.get('email')
        pass1 =  request.POST.get('password1')
        pass2 =  request.POST.get('password2')
        my_user = User.objects.create_user(uname,email,pass1)

        if(pass1 != pass2):
            return HttpResponse("Your passwords do not match")
        my_user.save()
        print(uname,email,pass1,pass2)

        return redirect('login')
    
    return render (request,"signup.html")

def LoginPage(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username = username, password = pass1)
        print(username,pass1)

        if(user != None):
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

    return render(request,'login.html')

def premium(request):
    return render (request,"premium.html")
def Company(request):
    return render (request,"Company.html")
def free(request):
    return render (request,"free.html")
def premiumticket(request):
    return render (request,"premiumticket.html")
def companyticket(request):
    return render (request,"companyticket.html")