numstr = '9876543210'
summ=200
signs = ['-','+',' ']

def string_to_summ(str_val):
    sum=0
    list_val=str_val.split('+')
    for i in range(len(list_val)):
        if (list_val[i].find('-') != -1):
            minus_list=list_val[i].split('-')
            for k in range(len(minus_list)):
                if (k == 0):
                    sum=sum+int(minus_list[k])
                else:
                    sum=sum-int(minus_list[k])
        else:
            sum=sum+int(list_val[i])
    return sum

for i1 in range(len(signs)):
    for i2 in range(len(signs)):
        for i3 in range(len(signs)):
            for i4 in range(len(signs)):
                for i5 in range(len(signs)):
                    for i6 in range(len(signs)):
                        for i7 in range(len(signs)):
                            for i8 in range(len(signs)):
                                for i9 in range(len(signs)):
                                    el = [numstr[0],signs[i1],numstr[1],signs[i2],numstr[2],signs[i3],numstr[3],signs[i4],numstr[4],signs[i5],numstr[5],signs[i6],numstr[6],signs[i7],numstr[7],signs[i8],numstr[8],signs[i9],numstr[9]]
                                    el2 = ''.join(el).replace(" ", "")
                                    if (string_to_summ(el2) == summ):
                                        print('{0}={1}'.format(el2, string_to_summ(el2)))


            

