'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title> Git 'Buggy' commits list : </title>
</head>
<body>

<ol>
'''

import time

## File to create the running web page diplay  of bug 'commits' info.  pulled down from github :

def main():
    #while(1):
        #rerecall and display the results on brwoser every 5 secs
        #time.sleep(5)
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
        
    try :
    
        # TODO : get 100  (or less) latest lines from file - poss. reverse list func tion on localStore file (dict_data.txt)
        input_file =open('./dict_data.txt',"r")
        locatStore_contnts=input_file.readlines()
        
        #locatStore_contnts.reverse()
                
        #str(locatStore_contnts)
        str_list=[contents]
        
        if len(locatStore_contnts) >= 100:
            size=100
            
        else:
            size=len(locatStore_contnts)
        
        ## Construct the html string from content above using the local store of git hub data..
        for j in range(0,size):

            contents_1=str_list[-1] + '\n <li> '
            contents_2=contents_1
            
            indx=locatStore_contnts[j].find("'message':") 
            
            indx_end_posn = locatStore_contnts[j][indx:].find(",")
        
            str_list.append(locatStore_contnts[j][indx:indx+indx_end_posn])              
                      
            #link to git commit         
            url_indx=  locatStore_contnts[j].find("'url':")
            
            url_indx_end_posn = locatStore_contnts[j][url_indx:].find(",")
                
            contents_3= '  ,  ' +  locatStore_contnts[j][url_indx:url_indx+url_indx_end_posn-1]
            str_list.append(contents_3)            
                               
            githubName_indx=locatStore_contnts[j].find("'name':")
 
            githubName_indx_end_posn = locatStore_contnts[j][githubName_indx:].find(",")
            contents_4= '  ,  ' +  locatStore_contnts[j][githubName_indx:githubName_indx+githubName_indx_end_posn]    
            str_list.append(contents_4)             
            
            #Date n time :
            dateTime_indx=locatStore_contnts[j].find("'date':")
            
            #Date n time :
            dateTime_indx=locatStore_contnts[j].find("date")
            dateTime_indx_end_posn = locatStore_contnts[j][dateTime_indx:].find(",")
            contents_6= '  ,  ' +  locatStore_contnts[j][dateTime_indx:dateTime_indx+dateTime_indx_end_posn]    
        
            str_list.append(contents_6)                      
            
            str_list.append(' <li>  \n')
            #str_list.append(str_list[-1] + ' <li>  \n')
            
        #final_contnts = str_list[-1] + "\n </ol>  \n \n </body> \n </html> \n ''' "
        str_list.append("\n </ol>  \n \n </body> \n </html> \n ''' ")
        
        final_contnts =  ' '.join(str_list)
        #zfinal_contnts = str_list  #+ "\n </ol>  \n \n </body> \n </html> \n ''' "
    
    except Exception as inst:

        print("Error...")
    
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)
           
    output.write(final_contnts)
    output.close()
    input_file.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac


main()