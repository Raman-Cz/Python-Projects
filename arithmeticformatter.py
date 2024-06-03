def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return 'Error: Too many problems.'
    # we will make 3 different lists to store the horizontal lines
    # 3rd will be for the answers when show_answers =True..

    list1=[]
    list2=[]
    list3=[]
    
    digits="0123456789"
    for each in problems:
        size=len(each) #length of each problem
        i=0
        l1=""
        while each[i] !=' ':
            if str(each[i]) not in digits:
                return 'Error: Numbers must only contain digits.'
            l1+=each[i]
            i+=1 
        if len(l1)>4:
            return 'Error: Numbers cannot be more than four digits.'
        list1.append(int(l1))
        i+=1
        if each[i]=='+':
            list2.append('+')
        elif each[i]=='-':
            list2.append('-')
        elif each[i]=='*' or each[i]=='/':
            return "Error: Operator must be '+' or '-'."
        
        i+=2
        l2=""
        while i<size:
            if str(each[i]) not in digits:
                return 'Error: Numbers must only contain digits.'
            l2+=each[i]
            i+=1 
        if len(l2)>4:
            return 'Error: Numbers cannot be more than four digits.'
        list3.append(int(l2))

    solution=""

    #line1................................

    for j in range(len(list1)):
        len1=len(str(list1[j]))
        len2=len(str(list3[j]))

        if len1<len2:
            solution+=" "*(abs(len1-len2)+2)+str(list1[j])
            if j <len(problems)-1:
                solution+="    "
        else:
            solution+="  "+str(list1[j])
            if j <len(problems)-1:
                solution+="    "
    solution+="\n"

    #line2.....................................
    for j in range(len(list1)):
        len1=len(str(list1[j]))
        len2=len(str(list3[j]))

        if len1<len2:
            solution+=list2[j]+" "+str(list3[j])
            if j <len(problems)-1:
                solution+="    "
        else:
            solution+=list2[j]+" "*((abs(len2-len1)+1))+str(list3[j])
            if j <len(problems)-1:
                solution+="    "
    
    #line3......................................
    solution+="\n"
    for j in range(len(list1)):
        len1=len(str(list1[j]))
        len2=len(str(list3[j]))
        x=max(len1,len2)
        solution+="-"*(x+2)
        if j <len(problems)-1:
                solution+="    "
    
    if show_answers==True:
        solution+="\n"
        for i in range(len(list1)):
            len1=len(str(list1[i]))
            len2=len(str(list3[i]))
            x=max(len1,len2)
            x=x+2
            y=""
            if list2[i]=="+":
                y=str(list1[i]+list3[i])
                solution+=" "*(x-len(y))+y
                if i <len(problems)-1:
                    solution+="    "
            else:
                y=str(list1[i]-list3[i])
                solution+=" "*(x-len(y))+y
                if i <len(problems)-1:
                    solution+="    "
    return solution
    

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))