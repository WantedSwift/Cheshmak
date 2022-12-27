from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import JsonResponse
from api.models import users ,actions,Chat
from operator import itemgetter

import json
import uuid
# Create your views here.

@csrf_exempt
def get_chat(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        reciver_id = request.POST['reciver_id']
        list_chat1 = Chat.objects.filter(sender_id=user.id,reciver_id=reciver_id).values('id','sender_id','reciver_id','created_at','message')
        list_chat2 = Chat.objects.filter(sender_id=reciver_id,reciver_id=user.id).values('id','sender_id','reciver_id','created_at','message')
        list_chat1 = list(list_chat1)
        list_chat2 = list(list_chat2)
        main_list = list_chat1 + list_chat2
        main_list = list(main_list)
        i = 0

        

        #main_list = main_list.sort(key=itemgetter('id'), reverse=True)
        

        for item in main_list:
            main_list[i]['created_at'] = str(main_list[i]['created_at'])
            i = i + 1

        return JsonResponse({
            'status': True,
            'data':main_list
        }, encoder=json.JSONEncoder)

@csrf_exempt
def get_matchs(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        list1 = actions.objects.filter(user1=user.id,action=1).values('user1','user2','action')
        list1 = list(list1)
        sorted = list1
        for item in list1:
            user2 = item['user2']
            try:
                action2 = actions.objects.get(user1=user2,user2=user.id,action=1)

            except Exception as exc:
                sorted.remove(item)

        i = 0
        for item in sorted:
            user2 = users.objects.get(id=item['user2'])
            user2 = model_to_dict(user2)
            user2['image'] = str(user2['image'])
            sorted[i]['reciver'] = user2

            i = i + 1

        sorted.reverse()

        chat_list = sorted
      
        main_list = list(chat_list)
        

        for item in chat_list:
            user1 = user.id
            user2 = item['user2']
            Chatdd = Chat.objects.filter(sender_id=user1,reciver_id=user2).values('id','sender_id','reciver_id')
            Chatdd = list(Chatdd)
            
            if Chatdd == []:
                Chatdd2 = Chat.objects.filter(sender_id=user2,reciver_id=user1).values('id','sender_id','reciver_id')
                Chatdd2 = list(Chatdd2)
                print('Chatdd =>',Chatdd2)
                if Chatdd2 == []:
                    print('print1 =>',sorted)
                    main_list.remove(item)
                    
                    

        print('print1 =>',sorted)
        print('print2 =>',list(main_list))

        return JsonResponse({
            'status': True,
            'match': sorted,
            'chat':main_list
        }, encoder=json.JSONEncoder)





@csrf_exempt
def send_message(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        reciver_id = request.POST['reciver_id']
        message = request.POST['message']
        Chat.objects.create(sender_id=user.id,reciver_id=reciver_id,message=message)


        return JsonResponse({
            'status': True
        }, encoder=json.JSONEncoder)

@csrf_exempt
def delete_profile(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        user.is_active = 0
        user.save()


        return JsonResponse({
            'status': True
        }, encoder=json.JSONEncoder)


@csrf_exempt
def get_profile(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        user = model_to_dict(user)
        user['image'] = str(user['image'])


        return JsonResponse({
            'status': True,
            'data': user
        }, encoder=json.JSONEncoder)



@csrf_exempt
def actions_set(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        user2 =  request.POST['user2']
        action = request.POST['action']

        try:
            old = actions.objects.get(user1=user.id,user2=user2)
            old.action = action
            old.save()

            try:
                old2 = actions.objects.get(user1=user2,user2=user.id)
                if old2.action == 1:
                    if old.action == 1:
                        data_user = users.objects.get(id=user2)
                        data_user = model_to_dict(data_user)
                        data_user['image'] = str(data_user['image'])
                        return JsonResponse({
                            'status': True,
                            'is_match': True,
                            'user2':data_user
                        }, encoder=json.JSONEncoder)
                    else:
                        return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)
                else:
                    return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)

            except Exception as exc:
                return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)

        except Exception as exc:
            old = actions.objects.create(user1=user.id,user2=user2,action=action)
            try:
                old2 = actions.objects.get(user1=user2,user2=user.id)
                if old2.action == 1:
                    if old.action == 1:
                        data_user = users.objects.get(id=user2)
                        data_user = model_to_dict(data_user)
                        data_user['image'] = str(data_user['image'])
                        return JsonResponse({
                            'status': True,
                            'is_match': True,
                            'user2':data_user
                        }, encoder=json.JSONEncoder)
                    else:
                        return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)
                else:
                    return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)

            except Exception as exc:
                return JsonResponse({
                            'status': True,
                            'is_match': False,
                            'user2':''
                        }, encoder=json.JSONEncoder)



@csrf_exempt
def get_home(request):
  #  try:
        token = request.headers.get('Authorization')
        user = users.objects.get(token=token)
        gender = user.gender
        gender1 = 1
        if gender == 0:
            gender1 = 1
        elif gender == 1:
            gender1 = 0
        else:
            gender1 = 2
        all = users.objects.filter(is_active=1,gender=gender1).values('id','name','gender','image')
        all_list = list(all)
        all_list_final = list(all_list)
        all_actions = actions.objects.filter(user1=user.id).values('user1','user2','action')
    
        for item in all_list:
            for item2 in all_actions:
                print('item22222',item2['user2'])
                print('id2222222',item['id'])
                if item2['user2'] == item['id']:
                    all_list_final.remove(item)
                


        return JsonResponse({
            'status': True,
            'data': all_list_final
        }, encoder=json.JSONEncoder)


@csrf_exempt
def upload_image_user(request):
  #  try:
        image = request.FILES.get('image')
        gender =  request.POST['gender']
        name =  request.POST['name']
        token = request.headers.get('Authorization')
        
        user = users.objects.get(token=token)
        user.gender = gender
        user.name = name
        user.image = image
        user.is_active = 1
        user.save()
		
        user_model = model_to_dict(user)
        user_model['image'] = str(user_model['image'])

       
  
        return JsonResponse({
            'status': True,
            'data': user_model,
        }, encoder=json.JSONEncoder)


@csrf_exempt
def login_register(request):
    try:
        email = request.POST["email"]
    except Exception as exc:
        return  JsonResponse({
            'status' : False,
            'message' : "please insert email"
         } , encoder=json.JSONEncoder)

    try:
        object_user = users.objects.get(email=email)
        ll = model_to_dict(object_user)
        ll['image'] = str(ll['image'])

        return JsonResponse({
            'status': True,
            'data': ll
        }, encoder=json.JSONEncoder)

    except Exception as exc:
        token =  uuid.uuid4().hex
        object_user = users.objects.create(token=token ,email=email)
        ll = model_to_dict(object_user)
        ll['image'] = str(ll['image'])
        
        return JsonResponse({
            'status': True,
            'data': ll
        }, encoder=json.JSONEncoder)

