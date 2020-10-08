from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import blogger,blogcontent,blogcomment
# Create your views here.

# home page management
def index(request):
    data = blogcontent.objects.all()
    dict = {"data":data}
    return render(request,'blogApp/home.html',dict)

# signup, login and logout management

def handelsignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email,password)
        user.save()
        messages.success(request,"Successfully account is created!")
        login(request, user)
        messages.success(request, "Successfully logged IN!")
        return redirect('/')

def handellogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged IN!")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentils, Please try again!")
            return HttpResponse("404-Not Found")


def handellogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')

# Contact form
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']
        user = blogger(name=name,email=email,msg=msg)
        user.save()
    return render(request,"blogApp/index.html")#index

# Handle Post blog
def postblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        slug = request.POST['slug']
        blog = blogcontent(blog_title=title,blog_content=content,slug=slug)
        blog.save()
        messages.success(request,'''Your blog successfully posted!Sooner display on the home page''')
    return render(request,"blogApp/post.html")

#Handle Search box
def search(request):
    query = request.GET['search']
    if len(query)>80:
         blo = []
    else:
        title = blogcontent.objects.filter(blog_title__icontains=query)
        content = blogcontent.objects.filter(blog_content__icontains=query)
        blo = title.union(content)
    para = {"blog": blo, "query":query}
    return render(request, 'blogApp/search.html',para)

def blogpage(request,slug):
    post = blogcontent.objects.filter(slug=slug)
    comments = blogcomment.objects.filter(post=post.first())
    content={"data":post,"comment":comments}
    return render(request,"blogApp/blog.html",content)

def comment_post(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postno = str(request.POST.get("parentSno"))
        cSno = str(request.POST.get("cSno"))
        post = blogcontent.objects.get(blog_s_no=postno)
        if cSno == "":
            com = blogcomment(comment=comment,user=user,post=post)
            com.save()
            messages.success(request, "Your comment has been posted successfully!")
        else:
            parent = blogcomment.objects.get(s_no=cSno)
            com = blogcomment(comment=comment, user=user, post=post, parent=parent)
            com.save()
            messages.success(request,"Your replay has been posted successfully!")
        return redirect(f"/blog/{post.slug}")