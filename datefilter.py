import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-02
#append all json strings to new file called output.txt
dateCount = {}
output=[]
f2=open('output.txt','w')
f2.write('\n')
f2.close()

f2=open('output.txt','a')
for root,dirs, files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        #print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            #print(payload['received'])
            k = payload['received'].split('T')[0]
            #print (k)
            if k>='2019-01-01' and k<='2019-01-02':
            #k.split('-')[0]=='2019':
                #if k.split('-')[1]=='01':
                    #if k.split('-')[2]=='01' or k.split('-')[2]=='02':
                        #print (k)                        
                        #string+=line+'\n'                        
                        f2.write(line+'\n')                        
                        print (line)
f2.close()          
