from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse, QueryDict
import requests
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def home(request):
    return render(request,'home.html')

@csrf_exempt 
def general_data(request):
    name  = request.GET.get('name', -1)
    r = requests.get('https://anapioficeandfire.com/api/books?name='+str(name))
    val = r.json()
    if val != []:
        data = {}
        data['status_code'] = 200
        data['status'] = "success"
        res = {}
        res["name"] = val[0]['name']
        res["isbn"] = val[0]['isbn']
        res["authors"] = val[0]['authors']
        res["number_of_pages"]= val[0]["numberOfPages"]
        res["publisher"]= val[0]["publisher"]
        res["country"]= val[0]["country"]
        res["release_date"]= val[0]["released"].split('T')[0]
        data['data'] = [res]
    else:
        data = {}
        data['status_code'] = 200
        data['status'] = "success"
        data['data'] = []
    return JsonResponse(data,safe=False)
        
    


@csrf_exempt 
def book_api(request):
    if request.method == 'POST':
        tok=items(isbn=request.POST.get('isbn'),name=request.POST.get('name'),country=request.POST.get('country'),number_of_pages=request.POST.get('number_of_pages'),publisher=request.POST.get('publisher'),year = int(str(request.POST.get('release_date').split('-')[0])),release_date=str(request.POST.get('release_date')))
        tok.save()
        auths = request.POST.getlist("authors")
        for a in auths:
            flag=author.objects.filter(name__exact=a).first()
            if flag:
                flag.books.add(tok)
                flag.save()
            else:
                auth=author(name=a)
                auth.save()
                auth.books.add(tok)
                auth.save()
        data = {}
        data['status_code'] = 200
        data['status'] = "success"
        res = {}
        res["name"] = tok.name
        res["isbn"] = tok.isbn
        res["authors"] = [i.name for i in tok.authors.all()]
        res["number_of_pages"]= tok.number_of_pages
        res["publisher"]= tok.publisher
        res["country"]= tok.country
        res["release_date"]= str(tok.release_date).split('T')[0]
        data['data'] = [res]
        return JsonResponse(data,safe=False)
    elif request.method == 'GET':
        name  = request.GET.get('name', -1)
        auth  = request.GET.get('author', -1)
        country  = request.GET.get('country', -1)
        publisher  = request.GET.get('publisher', -1)
        rdate  = request.GET.get('rdate', -1)
        books = items.objects.all()
        if auth != -1:
            au = author.objects.filter(name__exact=auth).first()
            if au:
                books = au.books.all()
            else:
                data =[]
                dummy = {}
                dummy["status_code"]= 200
                dummy["status"]= "success"
                dummy["data"]= []
                data.append(dummy)
                return JsonResponse(data,safe=False)
        if name != -1:
            books = [k for k in books if k.name == name]
        if country != -1:
            books = [k for k in books if k.country == country]
        if publisher != -1:
            books = [k for k in books if k.publisher == publisher]
        if rdate != -1:
            books = [k for k in books if k.year == rdate]
        
        data = []
        for b in books:
            dummy = {}
            dummy['status_code'] = 200
            dummy['status'] = "success"
            res = {}
            res["name"] = b.name
            res["isbn"] = b.isbn
            res["authors"] = [i.name for i in b.authors.all()]
            res["number_of_pages"]= b.number_of_pages
            res["publisher"]= b.publisher
            res["country"]= b.country
            res["release_date"]= str(b.release_date).split('T')[0].split(' ')[0]
            dummy['data'] = [res]
            data.append(dummy)
        if data == []:
            dummy = {}
            dummy["status_code"]= 200
            dummy["status"]= "success"
            dummy["data"]= []
            data.append(dummy)
        return JsonResponse(data,safe=False)
    else:
        return HttpResponse('not allowed')
    

  
@csrf_exempt 
def book_api_patch(request,id):
    if request.method == 'PATCH':
        payload = QueryDict(request.body)
        tok = get_object_or_404(items, id=id)
        tok.isbn=payload['isbn']
        tok.name=payload['name']
        tok.country=payload['country']
        tok.number_of_pages=payload['number_of_pages']
        tok.publisher=payload['publisher']
        dt = str(payload['release_date'])
        tok.release_date=dt
        tok.year=int(dt.split('-')[0])
        tok.save()
        orignal = [i.name for i in tok.authors.all()]
        removed_authors=list(set(orignal)-set(payload.getlist("authors")))
        added_authors=list(set(payload.getlist("authors"))-set(orignal))
        for word in removed_authors:
            flag=author.objects.filter(name__exact=word).first()
            flag.delete()
        for word in added_authors:
            flag=author.objects.filter(name__exact=word).first()
            if flag:
                flag.books.add(tok)
                flag.save()
            else:
                bake=author(name=word)
                bake.save()
                bake.books.add(tok)
                bake.save()
        data = {}
        data['status_code'] = 200
        data['status'] = "success"
        data['message'] = "The book "+payload['name']+" was updated successfully"
        res = {}
        res["id"] = id
        res["name"] = tok.name
        res["isbn"] = tok.isbn
        res["authors"] = [i.name for i in tok.authors.all()]
        res["number_of_pages"]= tok.number_of_pages
        res["publisher"]= tok.publisher
        res["country"]= tok.country
        res["release_date"]= str(tok.release_date).split('T')[0]
        data['data'] = [res]
        return JsonResponse(data,safe=False)
    elif request.method == 'DELETE':
        tok = get_object_or_404(items, id=id)
        msg = tok.name
        tok.delete()
        dummy = {}
        dummy["status_code"]= 200
        dummy["status"]= "success"
        dummy["message"] = "The book "+msg+" was deleted successfully"
        dummy["data"]= []
        return JsonResponse(dummy,safe=False)
    elif request.method == 'GET':
        book = get_object_or_404(items, id=id)
        dummy = {}
        dummy['status_code'] = 200
        dummy['status'] = "success"
        res = {}
        res["id"] = id
        res["name"] = book.name
        res["isbn"] = book.isbn
        res["authors"] =  [i.name for i in book.authors.all()]
        res["number_of_pages"]= book.number_of_pages
        res["publisher"]= book.publisher
        res["country"]= book.country
        res["release_date"]= str(book.release_date).split('T')[0].split(' ')[0]
        dummy['data'] = [res]
        return JsonResponse(dummy,safe=False)
    
    
