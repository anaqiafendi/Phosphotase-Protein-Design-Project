

import requests
import xml.etree.ElementTree as ET
import pandas as pd
import numpy
import os, os.path
import pickle
# import winsound
import time


from sys import platform
if os.name == 'nt' or platform == 'win32':
    os.chdir(os.path.dirname(__file__))
file_name="./test_1.xlsx"
xl_file = pd.ExcelFile(file_name)
dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}


count_x=0
GI_seq_dict=dict([])
bad_GI_list=[]

'''
for df_name in dfs.keys():
    count_x+=1
    if count_x>=5:
        try:
            GI_Num= dfs[df_name]["GI #"][0]
            if type(GI_Num)==numpy.float64:
                GI_Num=str(int(GI_Num))

            print(GI_Num)
            # We can use GI # as the UID so lets fetch the data from it 
            Base_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
            Utility_Name = 'efetch.fcgi?'
            Parameters = 'db=protein&id=' + str(GI_Num) + '&retmode=xml'
            URL_request = Base_URL + Utility_Name + Parameters
            URL_request = URL_request.replace(' ','+') # Need to replace all spaces within URL for query 
            print(URL_request)
            response = requests.get(URL_request) # Stores response of URL request
            #print(response)
            # Convert bytes of response.content of string to import to xml 
            bytes_string = str(response.content, 'utf-8')
            root = ET.fromstring(bytes_string)
            protein_sequence = root.find('GBSeq').find('GBSeq_sequence').text 
            print(protein_sequence)
            GI_seq_dict[GI_Num]=protein_sequence
            time.sleep(2)
        except Exception:
            print("Error: ", GI_Num)
            bad_GI_list.append(GI_Num)


pickle.dump( GI_seq_dict, open( "GI_seq_dict.p", "wb" ) )
pickle.dump( bad_GI_list, open( "bad_GI_list.p", "wb" ) )
'''

pickle_in1=open("./GI_seq_dict.p","rb")
GI_seq_dict=pickle.load(pickle_in1)
pickle_in1.close()
for i in GI_seq_dict.keys():
    print(i, GI_seq_dict[i]) 

pickle_in1=open("./bad_GI_list.p","rb")
bad_GI_list=pickle.load(pickle_in1)
pickle_in1.close()
for i in bad_GI_list:
    print(i) 