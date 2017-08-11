from django.http import HttpResponse


def index(request):
    return HttpResponse("""
        Rango says hey there LeeDark! <br/>
        <a href='/rango/about'>About here</a>""")


def about(request):
    return HttpResponse("""
        Rango says here is about page. <br/>
        <a href='/rango'>Index here</a>""")