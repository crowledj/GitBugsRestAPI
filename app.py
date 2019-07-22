from flask import Flask, jsonify,request
app = Flask(__name__)   


print(" \n \n **************************************************************************************************")
print(" \n    *****      type :  python easyWebPg_2.py  to view latest localstore display in browser...    *****")
print(" \n    **************************************************************************************************")



print(" \n \n ***********************************************************************************************************************************")
print(" \n    *****    Use curl cmd with'num_results parameter ' to view latet 'n' localstore commits in JSON format in the terminal ...    *****")
print(" \n    ***********************************************************************************************************************************")




## rest AP{I section of assignbment .. ( 'curl' to test and run while this file is running...)}
def do_restQuerys(X):

    input_file =open('./dict_data.txt',"r")
    #length=2
    
    #rerad commit info from local Store of commit data in reverse - i.e latest X - files first 
    locatStore_contnts=  input_file.readlines()
    
    if len(locatStore_contnts) <= X:
        size=len(locatStore_contnts)
        
    else:
        size=X
                            
    str_list=[]
    ### Construct the html string from content above using the local store of guit hub data..
    for j in range(0,size):
        
        ##link to git commit         
        ##tasks=locatStore_contnts[j]
        
        indx=locatStore_contnts[j].find("'message':") 
        
        indx_end_posn = locatStore_contnts[j][indx:].find(",")
            
        str_list.append(locatStore_contnts[j][indx:indx+indx_end_posn]) 
        
        
        ##link to git commit         
        url_indx=locatStore_contnts[j].find("'url':")
        ##print('url_indx = ' + str(url_indx))
        
        url_indx_end_posn = locatStore_contnts[j][url_indx:].find(",")
    
        contents_3= locatStore_contnts[j][url_indx:url_indx+url_indx_end_posn-1]
        str_list.append(contents_3)
        
        githubName_indx=locatStore_contnts[j].find("'name':")

        githubName_indx_end_posn = locatStore_contnts[j][githubName_indx:].find(",")
        contents_4= locatStore_contnts[j][githubName_indx:githubName_indx+githubName_indx_end_posn]    
        
        str_list.append(contents_4)     
          
        #Date n time :
        dateTime_indx=locatStore_contnts[j].find("date")
        dateTime_indx_end_posn = locatStore_contnts[j][dateTime_indx:].find(",")
        contents_5= locatStore_contnts[j][dateTime_indx:dateTime_indx+dateTime_indx_end_posn]    
        
        str_list.append(contents_5)         
                  
    commits=str_list
    
    return commits



@app.route('/todo/api/v1.0/commits', methods=['GET']) #,paramaters=['i'])
def get_tasks():
    
    #grab 'num_results' paramter ,from the cmd line   
    num_results = request.args.get('num_results')
    
    commits=do_restQuerys(int(num_results)) 
    
    return jsonify({'commits': commits})

if __name__ == '__main__':
    app.run(debug=False,port=8080)
