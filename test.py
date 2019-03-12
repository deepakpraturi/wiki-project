import sys, getopt
import json
from apiclient.discovery import build

def translate(q):  # Function converts the given segments into target language using google api
    query = q
    target_language = 'te'
    service = build('translate', 'v2', developerKey='AIzaSyDKzYeLBqWqGBxs06qU8L48t8iW8cBZDEQ')
    collection = service.translations()
    request = collection.list(q=query, target=target_language)
    response = request.execute()
    response_json = json.dumps(response)
    
    ascii_translation = ((response['translations'][0])['translatedText']).encode('utf-8').decode('ascii', 'ignore')
    
    utf_translation = ((response['translations'][0])['translatedText']).encode('utf-8')
    print (response)
    print(response["translations"][0]["translatedText"])
    print("***************************************************")
    return response["translations"][0]["translatedText"]

print(str(sys.argv))
f = open(sys.argv[1], "r")  #opens the input text file in reading mode
k = open(sys.argv[3],"a")   #open/creates the output file(translated text file) in appending mode
s=f.read()
if sys.argv[2] == 's':   # s indicates the spliting of the file into sentences
    s1=s.split(".")
    for i in s1:
        t=translate(i)
        k.write(t)
        k.write("\n")
elif sys.argv[2] == 'p':  # p indicates the spliting of the file into para's
    s2=s.split("\n")
    for i in s2:
        t=translate(i)
        k.write(t)
        k.write("\n")
else:                   # d indicates the whole file
    t=translate(s)
    k.write(t)
    k.write("\n")


# The command to run this file is : python3 test.py samp1.txt s transout.txt
# Before running this file we should install google api python client : pip install --upgrade google-api-python-client
# test.py is our script file
# The first argument(samp1.txt) is the input file which consists original content.
# The second argument(s or p or d) indicates the type of spliting of original file as sentences, para's and whole text respectively.
# The third argument(transout.txt) is the output file which stores the translated text.





