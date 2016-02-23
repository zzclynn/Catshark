# Convert csv to json
import re
def convert():
    result='['
    f = open('./csv_file/train.csv', 'r')
    title= getattributes(f.readline())
    i=0
    while True:
        line=csv2array2( f.readline(),len(title) )
        if line!=None:
            if i==0:
                result+=formatJSON(title,line)[1:]
                i=1
            else:
                result+=formatJSON(title,line)
            # print result
        else:
            break
    fw=open('./json_file/train.json','w')
    fw.write(result+'\n]')

def getattributes(s):
    s=re.findall(r'".*"',s)
    s=s[0].split('"')
    l=[]
    for i in s:
        if i!=',' and i!='':
            l.append(i)
    return l

def csv2array2(s,l):
    r=[i for i in range(l)]
    scomma=s.split(',')
    if len(scomma)!=l:

        m=s.split('"')
        # print '->'+str(len(m))
        if len(m)==5:
            r[0]=m[0].split(',')[0]
            r[1]=m[0].split(',')[1]
            # print m[1]
            r[2]='"{0}"'.format(m[1])
            r[3]= '"{0}"'.format(m[3])
            r[4]= m[-1][1:]
            # print r
            return r
        else:
            return
        # if len(m)==2:
        #     print 1
        #     r[2]=m[0]
        #     r[3]=m[1]
        #     r[0],r[1]=scomma[0],scomma[1]
        #     r[4]=scomma[-1]
        #     return r
        # elif len(m)==1 and scomma[-2][-1]=='"':
        #     print 2
        #     r[2]=''
        #     squote=s.split('"')[0]
        #     scomma2=squote.split(',')
        #     for  x in scomma2[2:]:
        #         r[2]+=x+','
        #     r[2]=r[2][:len(r[2])-1]
        #     r[3]=m[0]
        #     r[0],r[1]=scomma[0],scomma[1]
        #     r[4]=scomma[-1]
        #     return r

    else:
        # print 3
        s=s.split(',')

        if len(s)==l:
            s[-1]=s[-1][:len(s[-1])-1]
            # print s
        elif len(s)>l:
            # print len(s),s
            r=[]
            for i in xrange(2):
                r.append(s[i])
            t3=''
            for i in xrange(2,len(s)-2):
                t3+=s[i]+','
            r.append(t3[:len(t3)-1])
            # print t3[:len(t3)-1]
            for i in xrange(len(s)-2,len(s)):
                r.append(s[i])
            s=r


        for i in xrange(len(s)):
            try:
                float(s[i])
            except:
                if s[i]!='' and s[i][0]!='"':
                    s[i]='"{0}"'.format(s[i])

    return s

def formatJSON(title,s):
    # print title
    # print s
    result=',\n {\n'
    for i in xrange(len(title)):
        if i==len(title)-1:
            r='"{0}":{1}'.format(title[i],s[i])
        else:
            # print title
            # print s
            r='"{0}":{1},'.format(title[i],s[i])
        # print r
        result+='\t'+r+'\n'
    return result+' }'


convert()
