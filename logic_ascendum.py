input_num = 6
alph = ["A","B","C","D","E","F"]

output = []
some = ''

for x in range(0,input_num):
    if len(output)!=input_num:
        some = some+alph[x]
        output.append(some)
        
    else:
        break

dup_output = output[::-1]

fin_out = output+dup_output[1:len(dup_output)]

fin_output_11 = []
for ff in fin_out:
    if len(ff)==1:
        print ((input_num-1)*" "+ff)
    else:
        x = list(ff)
        if len(x)-input_num==-1:
            print (" "+" ".join(x))
        elif len(x)-input_num==-2:
            print ("  "+" ".join(x))
        elif len(x)-input_num == -3:
            print ("   "+" ".join(x))
        elif len(x)-input_num == -4:
            print ("    "+" ".join(x))
        else:
            print(" ".join(x))
    
    
    
