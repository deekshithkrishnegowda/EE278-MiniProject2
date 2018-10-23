import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="MAC-FixedPoint represenatation")
parser.add_argument("-m","--dec_precision",type = int,required=True,metavar="",help="Precision of fraction part")
args = parser.parse_args()
# the input is passed through the commandline argument. I have used argparse package. 
# the input parameter is the fixed point parameter 

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

# the nueron activation point is the converted into appropriate format. In this case it is fixed point number.
# A parameter should be passed to fixed point.

d_80 = ReLU_result 

def dec_int_conv(d_80):
    temp=2*d_80
    
    if(temp>=1):
        ret_bit = 1
        ret_sub = temp-1
        return ret_bit,ret_sub
    else:
        ret_bit = 0
        ret_sub = temp
        return ret_bit,ret_sub 

dec_list_80 = []
n_80 = 0

while n_80<=args.dec_precision:
    b_80,a_80=dec_int_conv(d_80)
    d_80=a_80  
    dec_list_80.insert(n_80,b_80) 
    n_80=n_80+1

del dec_list_80[-1] 

# The final result in fixed point format is displayed.
if(ReLU_result>0):
    print("the final result is {} and sign is {}".format(ReLU_result,final_sign))
    print("the fixed point represenatation is {}".format(dec_list_80))
else: 
    print ("number quantized to 0 after ReLU function") 
 
