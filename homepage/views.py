from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from.models import todo
from.forms import todoform, saveurlform

# Create your views here.
def homepage(request):
    todo_list = todo.objects.order_by('id')

    form = todoform()

    from bs4 import BeautifulSoup
    import requests
   

    arrayofticks =['DJIA','SP500','NASDAQ','RUT','Vix']
    arrayofothers = ['CL.1','GC00']
    arrayofyield = ['TMUBMUSD10Y']
    
    
    quote_change=[]
    quote_changePer=[]
    quote_value=[]
    
    for x in arrayofticks:
        newwebpage='https://quotes.wsj.com/index/'
        index= newwebpage.find('https://quotes.wsj.com/index/')
        newpage=newwebpage[index:] + x

        v = requests.get(newpage)
        b =v.text

        soup = BeautifulSoup(b, 'html.parser')

        quote_value.append(soup.find(id="quote_val").get_text())
        quote_change.append(soup.find(id="quote_change").get_text())
        quote_changePer.append(soup.find(id="quote_changePer").get_text())

    DJIA=quote_changePer[0]
    DJIA1=DJIA[:-1]
    DJIA2=float(DJIA1)
    SP500=quote_changePer[1]
    SP5001=SP500[:-1]
    SP5002=float(SP5001)
    NASDAQ=quote_changePer[2]
    NASDAQ1=NASDAQ[:-1]
    NASDAQ2=float(NASDAQ1)
    RUSSELL=quote_changePer[3]
    RUSSELL1=RUSSELL[:-1]
    RUSSELL2=float(RUSSELL1)
    VIX=quote_changePer[4]
    VIX1=VIX[:-1]
    VIX2=float(VIX1)


    quote_changePerfuture=[]

    for x in arrayofothers:
        newwebpage='https://quotes.wsj.com/futures/'
        index= newwebpage.find('https://quotes.wsj.com/futures/')
        newpage=newwebpage[index:] + x
        #  print(newpage)

        v = requests.get(newpage)
        b =v.text

        soup = BeautifulSoup(b, 'html.parser')

        
        quote_changePerfuture.append(soup.find(id="quote_changePer").get_text())

    OIL=quote_changePerfuture[0]
    OIL1=OIL[:-1]
    OIL2=float(OIL1)

    GOLD=quote_changePerfuture[1]
    GOLD1=GOLD[:-1]
    GOLD2=float(GOLD1)
            
    quote_changePeryield=[]

    for x in arrayofyield:
        newwebpage='https://quotes.wsj.com/bond/BX/'
        index= newwebpage.find('https://quotes.wsj.com/bond/BX/')
        newpage=newwebpage[index:] + x
       

        v = requests.get(newpage)
        b =v.text

        soup = BeautifulSoup(b, 'html.parser')

            
        quote_changePeryield.append(soup.find(id="quote_val").get_text())

    TEN=quote_changePeryield[0]

    #next steps take article
    v = requests.get('https://www.wsj.com/news/markets')
    b =v.text

    soup = BeautifulSoup(b, 'html.parser')

    quote_all=soup.find_all("a" , {"class":"wsj-headline-link"})


    marketart=[]
    link=[]
    both=[]
    marketarticle1=""
    marketarticle2=""
    marketarticle3=""
    marketarticle4=""
    marketarticle5=""
    marketarticle6=""
    marketarticle7=""
    marketarticle8=""
    marketarticle9=""
    marketarticle10=""
    marketarticle11=""
    marketarticle12=""

    for a in soup.find_all('a',{"class":"wsj-headline-link"} ,href=True):
        if a.text:
            marketart.append(a['href'])


    for x in range(3):
        link+=quote_all[x]

    for x in range(3):
        both.append(link[x])
        both.append(marketart[x])

    marketarticle1=both[0]
    marketarticle2=both[2]
    marketarticle3=both[4]
    marketarticle4=both[1]
    marketarticle5=both[3]
    marketarticle6=both[5]

    v = requests.get('https://www.wsj.com/news/technology')
    b =v.text

    soup = BeautifulSoup(b, 'html.parser')

    quote_tech=soup.find_all("a" , {"class":"wsj-headline-link"})

    markettech=[]
    linktech=[]
    bothtech=[]


    for a in soup.find_all('a',{"class":"wsj-headline-link"} ,href=True):
        if a.text:
            markettech.append(a['href'])


    for x in range(3):
        linktech+=quote_tech[x]

    for x in range(3):
        bothtech.append(linktech[x])
        bothtech.append(markettech[x])

    marketarticle7=bothtech[0]
    marketarticle8=bothtech[2]
    marketarticle9=bothtech[4]
    marketarticle10=bothtech[1]
    marketarticle11=bothtech[3]
    marketarticle12=bothtech[5]

    context = {'todo_list' : todo_list, 'form' : form, 'a' : DJIA2,'b':SP5002,'c':NASDAQ2,'d':RUSSELL2,'e':OIL2,'f':GOLD2,'g':TEN,'h':VIX2,
    'i': marketarticle1,'j': marketarticle2,'k': marketarticle3,'l': marketarticle4,'m': marketarticle5,'n': marketarticle6,'o': marketarticle7,'p': marketarticle8,'q': marketarticle9,
    'r': marketarticle10,'s': marketarticle11,'t': marketarticle12 }

    return render(request, 'homepage.html',context)
  

@require_POST



def addtodo(request):
    form = todoform(request.POST)

    print(request.POST['text'])

    if form.is_valid():
        new_todo = todo(text=request.POST['text'])
        new_todo.save()


    return redirect('homepage')
    

def completetodo(request, todo_id):
    Todo = todo.objects.get(pk=todo_id)
    Todo.complete = True
    Todo.save()

    return redirect('homepage')

def deletecomplete(request):
    todo.objects.filter(complete__exact=True).delete()

    return redirect('homepage')

def todaydate(request):
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y  %H:%M")


def saveurl(request):
    form2 = saveurlform()

    return render(request, 'homepage.html' , {'form':form2})

def posturl(request):
    form2 = saveurlform(request.POST)
    if form2.is_valid():
        url_name = form2.cleaned_data['url_name']
        url_link = form2.cleaned_date['url_link']
        url_name.save()
        url_link.save()
        form2 = saveurlform()
        return redirect('homepage')

    args = {'form': form2, 'url_name': url_name, 'url_link': url_link}

    return render(request, 'homepage.html' , args)