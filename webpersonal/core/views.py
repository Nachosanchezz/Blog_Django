from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
    </ul>
        """


def home(request):
 return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Nacho y me encanta Django!</p>
 """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portfolio</h2>
        <p>Algunos de mis proyectos:</p>
        <ul>
            <li><a href="https://github.com/DeNexus-Project/DeNexus_CSV-Analysis">DeNexus CSV Analysis</a></li>
         </ul>
    """)
   
def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí os dejo mi mail y mis redes sociales:</p>
        <ul>
            <li><a href="mailto:isanccal@myuax.com">Gmail</a></li>
            <li><a href="https://github.com/Nachosanchezz">Github</a></li>
            <li><a href="https://linkedin.com/in/ignacio-sanchez-calabrese">LinkedIn</a></li>
 </ul>
 """)



         

