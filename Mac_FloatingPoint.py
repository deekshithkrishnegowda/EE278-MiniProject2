import pandas as pd
import numpy as np

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
output_80 = ReLU_result

# the nueron activation point is the converted into appropriate format. In this case it is floating point number with half precision.

int16bits_80 = np.asarray(output_80, dtype=np.float16).view(np.int16).item()
# print("this is value of int16bits: %d " %int16bits)
#print('{:016b}'.format(int16bits_80))

# the addition product or multiplication product is converted into half precision floating point using the numpy package. 
# the result is in integer format. this is later converted into string because int cannot be indexed in python  

y_80=bin(int16bits_80)
sbox_80=''
k_80=list(y_80)
x_80=k_80[2:]
l_80=len(x_80)
noOfZeroes_80=16-l_80
for i in range(noOfZeroes_80):
    sbox_80=sbox_80+'0'
for j in x_80:
    sbox_80=sbox_80+j
print("This is the 16bit binary value: %s " %sbox_80)


#print (sbox_80,len(sbox_80)) 

#sign_bit_80=(sbox_80[0])
exp_part_80=(sbox_80[1:6])
man_part_80=(sbox_80[6:]) 

# the mantissa and exponent part are given to exp_part_80 and man_part_80. This is displayed later.    

# this portion calculated the sign of the addition or multiplication operation 
# During multiplication , if both the signs are same, then sign of product is positive. Else it is negative. 
# During addition , the sign of the largest integer is given to the product. 



# this portion displays the mantissa and the exponent portions of the product along with the number of bits    
print("ANSWER IN HALF PRECISION FLOATING POINT")     
print("Mantissa is {} and number of bits is {}".format((man_part_80),len(man_part_80)))
print("Exponent is {} and number of bits is {}".format((exp_part_80),len(exp_part_80)))
print("Sign is {} and number of bit is 1".format(final_sign))
