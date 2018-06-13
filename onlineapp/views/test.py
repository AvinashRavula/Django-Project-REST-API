from django.shortcuts import render, redirect


def session_view(request):
    request.session.setdefault('counter',0)
    request.session['counter'] += 1
    #request.session['counter'] = call_count + 1
    return render(request, 'Error_page.html', {'error': "Count = "+str(request.session['counter'])})


def raise_python_error(request):
    raise ValueError("Value error")


def redirect_page(request):
    return redirect("https://www.google.com")