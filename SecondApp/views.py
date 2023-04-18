from django.shortcuts import render

# Create your views here.
def students1(request):
    return render(request,'SecondApp/students1.html');

def students2(request):
    return render(request,'SecondApp/students2.html');


#student-data & date-time using {{templ-tags}}
import datetime
import time
def student_datetime(request):
	date1=datetime.datetime.now();
	date2=time.ctime();
	rollno = 1001;
	sname='sai';
	marks=95;
	dict1 = {'server_datetime':date1,'server_datetime2':date2,'rollno':rollno,'sname':sname,'marks':marks};
	return render(request,'FirstApp/studentdatetime.html',dict1);
