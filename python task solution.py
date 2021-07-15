di1={'A':'Hello','B':'World','C':'Buddy'}
di2={'A':'Hello','C':'Buddy','D':'Welcome'}
inp1="A and B"
inp2="A and C"
inp3="D or B"
inp4="A or B"
inp5="A and B and C"
inp6="A and (B or C)"
inp7="A and (C or D)"
inp8="A and (B or C) and D"

def split(st):      
    li=[]
    li2= st.split(" ")
    #print(li2)
    for i in range(len(li2)):
        if(len(li2[i])==1):
            li.append(li2[i])
        elif(li2[i][0]=="("):
            li.append("(")
            li.append(li2[i][1])
        elif(li2[i][1]==")"):
            li.append(li2[i][0])
            li.append(")")
        else:
            li.append(li2[i])
       
    return li
def parse(st,di):
   
    li=split(st)
    #print(li)
    res=""
    i=0
    f=1
    while i < len(li):
        if(li[i]=="or"):
            if(f==0):
                i=i+1
                res= res+ di[li[i]]
            while(i<len(li) and li[i]!=")"):
                i=i+1
        elif(li[i]=="and"):
            pass
        elif(li[i]=="("):
            pass
        else:
            if(li[i] in di.keys()):
                res = res + di[li[i]]
            else:
                f=0
        i=i+1
         
    print(res)  

parse(inp1,di1)
parse(inp2,di1)
parse(inp3,di1)
parse(inp4,di1)
parse(inp5,di1)
parse(inp6,di1)
parse(inp7,di1)
parse(inp8,di2)