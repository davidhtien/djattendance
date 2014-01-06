from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.utils.safestring import mark_safe
from nvd3 import lineWithFocusChart

import datetime
import time

from utilities.models import Location, Bill

#base = datetime.datetime.today()
#dateList = [ base - datetime.timedelta(days=x) for x in range(0,numdays) ]

@login_required
def home(request):
    test_location = Location.objects.order_by('name')[0]
    query_data = Bill.objects.filter(location=test_location)
    
    xdata = [];
    ydata = [];
    for bill in query_data:
        value=bill.electricity/float(bill.days)*24
        
        xdata.append(int(time.mktime(bill.start_date.timetuple())) * 1000)
        ydata.append(value)
        
        xdata.append(int(time.mktime((bill.end_date-datetime.timedelta(days=1)).timetuple())) * 1000)
        ydata.append(value)
    
    tooltip_date = "%d %b"
    extra_series = {"tooltip": {"y_start": "", "y_end": " kW"},
                   "date_format": tooltip_date}
    series = {
        'x': xdata,
        'name1': test_location.name, 'y1': ydata, 'extra1': extra_series
        }
    chart_type = "lineWithFocusChart"
    
    data = {
        'charttype': chart_type,
        'chartdata': series,
        'kw_extra' : {
            'x_is_date'     : True,
            'x_axis_format' : '%d %b'
        },
        'query_data' : query_data
    }
    return render(request,'utilities/year_chart.html', dictionary=data)

@login_required
def all_data(request):
    test_location = Location.objects.order_by('name')[0]
    query_data = Bill.objects.filter(location=test_location)
    
    xdata = [];
    ydata = [];
    for bill in query_data:
        value=bill.electricity/float(bill.days)*24
        
        xdata.append(int(time.mktime(bill.start_date.timetuple())) * 1000)
        ydata.append(value)
        
        xdata.append(int(time.mktime((bill.end_date-datetime.timedelta(days=1)).timetuple())) * 1000)
        ydata.append(value)
    
    tooltip_date = "%d %b"
    extra_series = {"tooltip": {"y_start": "", "y_end": " kW"},
                   "date_format": tooltip_date}
    series = {
        'x': xdata,
        'name1': test_location.name, 'y1': ydata, 'extra1': extra_series
        }

    # Build chart
    chart = lineWithFocusChart(
           x_is_date=True,
           x_axis_format='%d %b',
           color_category='category20',
           tag_script_js=True,
           name='linewithfocuschart_container'
       )
    
    for loc in Location.objects.order_by('name'):
        if not "Grace" in loc.name:
            continue;
        xdata = [];
        ydata = [];
        add_series=True
        for bill in Bill.objects.filter(location=loc):
            if(bill.electricity is None):
                add_series=False
                break;
            value=bill.electricity/float(bill.days)*24
            
            xdata.append(int(time.mktime(bill.start_date.timetuple())) * 1000)
            ydata.append(value)
            
            xdata.append(int(time.mktime((bill.end_date-datetime.timedelta(days=1)).timetuple())) * 1000)
            ydata.append(value)
        if(add_series):
            chart.add_serie(name=loc.name, y=ydata, x=xdata, extra=extra_series)

    chart.buildhtml()

    html_string = chart.jschart + '\n'
    
    data = {
        'chart_html' : mark_safe(html_string),
        'query_data' : query_data
    }
    
    return render(request,'utilities/all_data.html', dictionary=data)
    #data = {'something_here': 'content'}
    #return render(request, 'utilities/index.html', dictionary=data)
