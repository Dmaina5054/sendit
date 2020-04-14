from django.shortcuts import render
import africastalking
import os

def procmess(request):
    #this funtion sends a message and returns a response obj
   
    mess_dir = '/cv001_19502.txt' #corpora
    contact_list = ['+254724111111',]

    user_name = 'sandbox'
    api_key = os.environ['ATK_KEY'] #use python-dotenv
    africastalking.initialize(user_name,api_key)
    sms = africastalking.SMS
    
    
    with open(mess_dir,'r') as f:

        resp = sms.send(f.read(),contact_list)
        
       

        # key_p = resp.get('SMSMessageData')
        # recipient_list = key_p['Recipients']

        resp = resp
    return render(request,'mtext/index.html',{'context':resp})



            




    
