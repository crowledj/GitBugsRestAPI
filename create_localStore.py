from flask import Flask
import polling
import requests
import json
import time
import os
app = Flask(__name__)

## code to create and append to the local Data store of requests to githiub..


print(" \n \n **************************************************************************************************")
print(" \n    *********      Filling local store @ ./dict_data.txt with 'bug' github commits....       *********")
print(" \n \n **************************************************************************************************")



@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

shaDict={}

#keep polling the sife for a success response |(and an update -'new commits')
poll_count=0
while(True):
  
  poll_result=polling.poll(
    lambda: requests.get('https://api.github.com/search/commits?q=message:bug',headers={"Accept":"application/vnd.github.cloak-preview"}
                         ).status_code == 200,
    step=60,
    poll_forever=True)
 
  #file location of local store    
  my_dict_data_file = open('./dict_data.txt', 'a')
  if poll_result == True: 
    
    return_req=requests.get('https://api.github.com/search/commits?q=message:bug',headers={"Accept":"application/vnd.github.cloak-preview"}) 
    
    poll_count+=1
    print('polling the githib API  =  ' + str(poll_count) + " - th time ...")
    
    #after ten polls to API - API hit rate is exceeded and must wait another minute..
    #if (poll_count % 10) == 0:
    #  time.sleep(60)

    ## try track all unique entrie by storing dict with all sha's as keys..:
    ret_json=return_req.json()
    
    if 'items' not in ret_json:
      break
    
    for counter,items in enumerate(ret_json['items']):
      
      ## ensure each unique github commit with 'bug' in message is unique in the localstore...
      if items['sha'] not in shaDict:
        
        #print(ret_json)
      
        shaDict[items['sha']] = counter
        
        my_dict_data_file.write(str(str(ret_json['items'][counter]).encode('utf-8').strip()))
        my_dict_data_file.write("\n")
        
  #try running the rest API server in the background now a localStore has been built up,
  #if poll_count == 3:
    
    #print('poll_count =  ' + str(poll_count) + "  - runing the Rest APi server and the display on localhost..... \n ")
  
    
    ##and run the web page coomin store ...    
    #os.system("python ./easyWebPg_2.py & ")
    
    #os.system("./app.py &")
        
  my_dict_data_file.close()  
  




