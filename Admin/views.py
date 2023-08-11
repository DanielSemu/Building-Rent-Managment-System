from django.shortcuts import render,redirect
from .models import Block_Location,Block,Room,Role
from django.contrib.auth.hashers import make_password
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    #create default user!
    
    form=LoginForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
           
            if user is not None:
                #role=user.Role
                role=str(user.Role)
                if role  == "Student_Dean":
                    request.session['username'] = username
                    login(request, user)
                    return redirect('studentdeanhome')
                elif role=='Admin':
                    request.session['username'] = username
                    login(request, user)
                    return redirect('Adminhome')
                else:
                    messages.error(request,"You have no Role In this System...")
            else:
                messages.error(request,"Invalid credientials...")
                return redirect('home')
    return render(request,"homepagetest.html",{"form":form})
def Adminhome(request):
    return render(request,"Admin/Adminhome.html")
def Add_Block(request):
    form=AddBlockForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            block=request.POST['Block_name']
            if Block.objects.filter(Block_name=block).exists() :
                messages.error(request, "This Block is already Registerd")
                return redirect('addblock')
            else:
                form.save()
                messages.success(request,"Block Registered Succesfully")
                return redirect('addblock')
    return render(request,"Admin/AddBlock.html",{"form":form})

def Add_Room(request):
    form=AddRoomForm(request.POST or None)
    if request.method=='POST':
        room=request.POST['Room_name']
        block=request.POST['Block']
        if Room.objects.filter(Room_name=room ,Block =block).exists():
            messages.error(request,"This Room is Already Registered")
            return redirect("addroom")
        else:
            if form.is_valid():
                form.save()
                messages.error(request,"The Room Registereed Successfully")
                return redirect("addroom")
            
    return render(request,"Admin/AddRoom.html",{"form":form})
def Add_Role(request):
    form=AddBlockForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            block=request.POST['Block_name']
            if Block.objects.filter(Block_name=block).exists() :
                messages.error(request, "This Block is already Registerd")
                return redirect('addblock')
            else:
                form.save()
                messages.success(request,"Block Registered Succesfully")
                return redirect('addblock')
    return render(request,"Admin/AddRole.html",{"form":form})
def Add_Block_Location(request):
    form=AddBlockLocationForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            block_location=request.POST['Block_Location']
            if Block_Location.objects.filter(Block_Location=block_location).exists() :
                messages.error(request, "This Block is already Registerd")
                return redirect('addblocklocation')
            else:
                form.save()
                messages.success(request,"Block Registered Succesfully")
                return redirect('addblocklocation')
            
    return render(request,"Admin/AddBlockLocation.html",{"form":form})

def view_block(request):
    result=Block.objects.all()
    return render(request,"Admin/viewblock.html",{'result':result})
def view_room(request,pk):
    result=Room.objects.filter(Block_id=pk)
    return render(request,"Admin/viewroom.html",{"result":result})
def edit_block(request,pk):
    result=Block.objects.get(id=pk)
    form=AddBlockForm(request.POST or None,instance=result)
    context = {'form':form} 
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return redirect("viewblock")
    return render(request,"Admin/edit_block.html",context)

def edit_room(request,pk):
    result=Room.objects.get(id=pk)
    val=Block.objects.get(id=result.Block_id)
    form=AddRoomForm(request.POST or None,instance=result)
    context = {'form':form} 
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return redirect("viewroom",val.id)
    return render(request,"Admin/edit_room.html",context)

def delete_room(request,pk):
    result=Room.objects.get(id=pk)
    val=Block.objects.get(id=result.Block_id)
    result.delete()
    messages.error(request,"Room Removed!")
    return redirect('viewroom',val.id)

def delete_block(request,pk):
    result=Block.objects.get(id=pk)
    result.delete()
    messages.error(request,"Block Removed!")
    return redirect('viewblock')


#User Management

def registerUser(request):
    form=RegisrationForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user=User()
            firstname=form.cleaned_data.get("first_name")
            lastname=form.cleaned_data.get("last_name")
            username=form.cleaned_data.get("username")
            role=form.cleaned_data.get("Role")
            password1=form.cleaned_data.get("password")
            password2=make_password(password1)
            user.first_name=firstname
            user.last_name=lastname
            user.username=username
            r=Role.objects.get(Role_name=role)
            user.Role=r
            user.password=password2
            user.save()
            return redirect("registerUser")
        else:
            messages.error(request,'Invalid Form')
            
    return render(request,"Admin/registeruser.html",{"form":form})

def view_user(request):
    username=request.session.get('username')
    # print(username)
    result=User.objects.exclude(username=username)
    return render(request,'Admin/viewuser.html',{'result':result})
def edit_user(request,pk):
    username=request.session.get('username')
    result=User.objects.get(id=pk)
    val=User.objects.exclude(username=username)
    form=UpdateUserForm(request.POST or None,instance=result)
    context = {'form':form}
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return redirect("viewuser")

    return render(request, 'Admin/edit_user.html',context)

def roomstatus(request):
    room=Room.objects.all()
    
    return render(request,"Admin/roomstatus.html",{"result":room})

# @login_required(login_url='login_view')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('home')