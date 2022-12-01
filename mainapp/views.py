from django.shortcuts import render, redirect
from .models import Sertificate

# Create your views here.
def home_page(request):
    # model = Sertificate.objects.all().get(nomer="00122001")
    # print(model.ism_familiya)
    if request.method == 'POST':
        aaaaa = request.POST.get('nomer')
        print(aaaaa)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return redirect("success_page", pk=str(aaaaa))
        # try:
        #     model = Sertificate.objects.get(nomer=aaaaa)
        #     return redirect("success_page", pk=aaaaa)
        # except:
        #     return redirect('failed_page')
        

    return render(request, "index.html")

def success_page(request, pk):
    print(pk, type(pk), "aaaaaaaaaaaaaaaa")
    print("nomer")
    # model = "a"
    # test = pk
    # model = Sertificate.objects.get(nomer=pk)
    # print(model)
    nomerlar = Sertificate.objects.all()
    print(nomerlar)
    print(list(nomerlar))


    try:
        model = Sertificate.objects.get(nomer=pk)
        print(model)
    except:
        print("error")
        return redirect('failed_page')
    # model = "a"
    return render(request, "success.html", {'model': model})



def failed_page(request):
    print(request)
    return render(request, "failed.html")