from django.shortcuts import render
from .models import Company
from django.http import HttpResponseRedirect

def one(request):
    return render(request,'myapp/one.html')
def two(request):
    return render(request,'myapp/two.html')
def tre(request):
    return render(request,'myapp/tre.html')
def man(request):
    return render(request,'myapp/man.html')

def post(request):
    '''
    count = Company.objects.count()
    
    posts=[]
    name = [Company.objects.get(id = i).companyName for i in range(count - 2, count + 1)]
    nomer = [Company.objects.get(id = i).companyNumber for i in range(count - 2, count + 1)]
    post = [Company.objects.get(id = i).companyPost for i in range(count - 2, count + 1)]
    for i in range(2,-1,-1):
        posts.append([name[i],nomer[i],post[i]])
    
    print(posts,'-'*20)
    posts = [[Company.objects.get(id=i)] for i in range(count,count-3,-1)]
    '''
    posts = Company.objects.order_by('-id')[:3]
    print(posts)
    data = {
        'posts': posts
    }
    return render(request,'myapp/post.html', data)


def form(request):
    if request.method == 'POST':
        

        form = dict(request.POST)
        print(int(form['company_index'][0]),form['company_name'],'-'*500)

        Company(companyName=str(form['company_name'][0]),companyNumber=int(form['company_index'][0]), companyPost=str(form['company_post'][0]),).save()

        return HttpResponseRedirect('man')
    if request.method == 'GET':
        return render(request,'myapp/form.html')

