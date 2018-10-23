import pandas as pd


file=pd.read_excel("testcases.xlsx",sheetname="Sheet3")
i = 0
THETHA = []
A = []
A_sign = []
THETHA_sign=[]
while (i<4):
    THETHA.append(file["THETHA"][i])
    A.append(file["A_SCALED"][i])
    A_sign.append(file["A_SIGN"][i])
    THETHA_sign.append(file["THETHA_SIGN"][i])
    i = i+1
# the input activation point and the thetha values are entered in the excel sheet. The excel sheet is read from 
# using the panda package. The scaled values of input activation point and thetha are then put inside a list

i = 0
activation_sum = 0

# weighted multiplication operation is done on input activation point and thetha.
def activation(i,THETHA,A):
    activation_sum_1 = THETHA[0]*A[0]
    activation_sum_2 = THETHA[1]*A[1]
    activation_sum_3 = THETHA[2]*A[2]
    activation_sum_4 = THETHA[3]*A[3]
    if ((A_sign[0]==0) and (THETHA_sign[0]==0)):
        sign_1 = 0
    elif((A_sign[0]==0) and (THETHA_sign[0]==1)):
        sign_1 = 1
    elif((A_sign[0]==1) and (THETHA_sign[0]==0)):
        sign_1 = 1
    elif((A_sign[0]==1) and (THETHA_sign[0]==1)):
        sign_1 = 0

    if ((A_sign[1]==0) and (THETHA_sign[1]==0)):
        sign_2 = 0
    elif((A_sign[1]==0) and (THETHA_sign[1]==1)):
        sign_2 = 1
    elif((A_sign[1]==1) and (THETHA_sign[1]==0)):
        sign_2 = 1
    elif((A_sign[1]==1) and (THETHA_sign[1]==1)):
        sign_2 = 0

    if ((A_sign[2]==0) and (THETHA_sign[2]==0)):
        sign_3 = 0
    elif((A_sign[2]==0) and (THETHA_sign[2]==1)):
        sign_3 = 1
    elif((A_sign[2]==1) and (THETHA_sign[2]==0)):
        sign_3 = 1
    elif((A_sign[2]==1) and (THETHA_sign[2]==1)):
        sign_3 = 0

    if ((A_sign[3]==0) and (THETHA_sign[3]==0)):
        sign_4 = 0
    elif((A_sign[3]==0) and (THETHA_sign[3]==1)):
        sign_4 = 1
    elif((A_sign[3]==1) and (THETHA_sign[3]==0)):
        sign_4 = 1
    elif((A_sign[3]==1) and (THETHA_sign[3]==1)):
        sign_4 = 0            

    if ((sign_1 ==1) or (sign_2==1)):
        if (activation_sum_1>activation_sum_2):
            temp_sum_1 = activation_sum_1 - activation_sum_2
            temp_sign_1 = sign_1
        else:
            temp_sum_1 = activation_sum_2 - activation_sum_1
            temp_sign_1 = sign_2     
    else:
        temp_sum_1 = activation_sum_1 + activation_sum_2
        temp_sign_1 = 0

    if ((sign_3 ==1) or (sign_4==1)):
        if (activation_sum_3>activation_sum_4):
            temp_sum_2 = activation_sum_3 - activation_sum_4
            temp_sign_2 = sign_3
        else:
            temp_sum_2 = activation_sum_4 - activation_sum_3
            temp_sign_2 = sign_4 
    else:
        temp_sum_2 = activation_sum_3 + activation_sum_4
        temp_sign_2 = 0

    if ((temp_sign_1==1) or (temp_sign_2==1)):
        if (temp_sum_1>temp_sum_2):
            activation_sum = temp_sum_1 - temp_sum_2
            sign = temp_sign_1
        else:
            activation_sum = temp_sum_2 - temp_sum_1             
            sign = temp_sign_2
    else:
        activation_sum = temp_sum_1 + temp_sum_2
        sign = 0

    return activation_sum,sign

def ReLU (value,sign):
    if (sign ==1):
        final_result = 0
    else:
        final_result = value 
    
    return final_result
# the neuron activation number is then passed through ReLu function. If the neuron activation point is negative, the the 
# the output if ReLU function is zero. 

ReLU_input,final_sign = activation(i,THETHA,A)
ReLU_result = ReLU(ReLU_input,final_sign)

# the nueron activation point is the converted into appropriate format. In this case it is Mu-Law.

if final_sign == 1:
    final_sign_Mu = 0
else:
    final_sign_Mu = 1    

list1_80 = [0,0,0,0,0,0,0,1]
list2_80 = [0,0,0,0,0,0,1]
list3_80 = [0,0,0,0,0,1]
list4_80 = [0,0,0,0,1]
list5_80 = [0,0,0,1]
list6_80 = [0,0,1]
list7_80 = [0,1]
list8_80 = [1]

# the above list is used as the encoding table

list1_1_80 = [0,0,0]
list2_1_80 = [0,0,1]
list3_1_80 = [0,1,0]
list4_1_80 = [0,1,1]
list5_1_80 = [1,0,0]
list6_1_80 = [1,0,1]
list7_1_80 = [1,1,0]
list8_1_80 = [1,1,1]

# this list is concatinated with some value later.
# this function is used to covert the fractional part which is in decimal into binary. 
# This is done because python does not has binary format datatype.

def dec_int_conv(d_80):
    temp_80=2*d_80
    
    if(temp_80>=1):
        ret_bit_80 = 1
        ret_sub_80 = temp_80-1
        return ret_bit_80,ret_sub_80
    else:
        ret_bit_80 = 0
        ret_sub_80 = temp_80
        return ret_bit_80,ret_sub_80 

dec_list_80 = []
n_80 = 0
dec_precision = 13

d_80 = ReLU_result    
dec_int_conv(d_80)   

while n_80<=dec_precision:
    b_80,a_80=dec_int_conv(d_80)
    d_80=a_80  
    dec_list_80.insert(n_80,b_80) 
    n_80=n_80+1

 
#print (dec_list_80,type(dec_list_80[0])) 

dec_list_updated_80 = []
for i_80 in dec_list_80:
    if(i_80==0):
        dec_list_updated_80.append(i_80)
    else:
        break

if (d_80<1):
    dec_list_updated_80.append(1)


final_list_80 = []

if (dec_list_80[0:1] == dec_list_updated_80):
    final_list_80 = list8_1_80 + dec_list_80[1:5] 
    final_list_80.insert(0, final_sign_Mu)
    
elif (dec_list_80[0:2] == dec_list_updated_80):
    final_list_80 = list7_1_80 + dec_list_80[2:6]
    final_list_80.insert(0, final_sign_Mu)     
    
elif (dec_list_80[0:3] == dec_list_updated_80):
    final_list_80 = list6_1_80 + dec_list_80[3:7]
    final_list_80.insert(0, final_sign_Mu) 

elif (dec_list_80[0:4] == dec_list_updated_80):
    final_list_80 = list5_1_80 + dec_list_80[4:8]
    final_list_80.insert(0, final_sign_Mu)
 
elif (dec_list_80[0:5] == dec_list_updated_80):
    final_list_80 = list4_1_80 + dec_list_80[5:9]
    final_list_80.insert(0, final_sign_Mu)

elif (dec_list_80[0:6] == dec_list_updated_80):
    final_list_80 = list3_1_80 + dec_list_80[6:10]
    final_list_80.insert(0, final_sign_Mu)
    
elif (dec_list_80[0:7] == dec_list_updated_80):
    final_list_80 = list2_1_80 + dec_list_80[7:11]
    final_list_80.insert(0, final_sign_Mu)

elif (dec_list_80[0:8] == dec_list_updated_80):
    final_list_80 = list1_1_80 + dec_list_80[8:12]
    final_list_80.insert(0, final_sign_Mu)        

# the results are displayed in the following section.
# After dividing the inputs by 8192, if the results is  not comparable with the encoding table, then the number cannot be represented 
# using mu-law encoding.

else:
    print ("cannot display in mu-law ")
                    
print ("Mu-law encoded value is {}".format(final_list_80))             

