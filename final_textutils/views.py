from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    txt = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc","off")
    fullcaps = request.GET.get("fullcaps","off")
    newline = request.GET.get("newline","off")
    spaceremove = request.GET.get("spaceremove","off")
    charactercount = request.GET.get("charactercount","off")
    if removepunc == "on":
        punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed += char
        params = {"purpose" : "Remove Punctuations","analyzed_text" : analyzed}
        return render(request,"analyze.html",params)

    elif fullcaps == "on":
        upper = ""
        for char in txt:
            upper = upper + char.upper()
            
        params = {"purpose" : "changed to upper case","uppercase" : upper}
        return render(request,"capfirst.html",params)

    elif newline == "on":
        new_line = ""
        for char in txt:
            if char !="\n":
                new_line = new_line + char
                

        params = {"purpose" : "remove newlines","lines" : new_line}
        return render(request,"newlineremove.html",params)

    elif spaceremove == "on":
        space_rm =""
        cs =""
        for char in txt:    
            if char == " ":
                if char == " " and cs == " ":
                    continue
                space_rm = space_rm + char

            else:
                space_rm = space_rm +char

            cs = char



        params = {"purpose" : "remove spaces","spacex" : space_rm}
        return render(request,"spacexremove.html",params)

    elif charactercount == "on":
        count = ""
        counter = 0
        for char in txt:
            count = count + char
            counter = counter + 1

        params = {"purpose" : "Character counter","counting" : counter}
        return render(request,"charactercount.html",params)


    else:
        return render(request,"error.html")