
import csv
import json
import re
filename='product_descriptions'
csvfile = open('./csv_file/'+filename+'.csv', 'r')
jsonfile = open('./json_file/'+filename+'_0'+'.json', 'w')
t=1
def getattributes(s):
    s=re.findall(r'".*"',s)
    s=s[0].split('"')
    l=[]
    for i in s:
        if i!=',' and i!='':
            l.append(i)
    return tuple(l)
fieldnames=getattributes(csvfile.readline())
print fieldnames
# title= csv2array(csvfile.readline())
# fieldnames=tuple(title)
#

reader = csv.DictReader(csvfile, fieldnames)
# print len(reader)
jsonfile.write('[')
i=0
for row in reader:
    if i!=0:
        if i==100000:
            jsonfile.write(']')
            jsonfile=open('./json_file/'+filename+'_'+str(t)+'.json', 'w')
            t+=1
            jsonfile.write('[')
            i=1
        else:
            jsonfile.write(',\n')
            i+=1
    else:
        i+=1
    json.dump(row, jsonfile)
#
jsonfile.write(']')