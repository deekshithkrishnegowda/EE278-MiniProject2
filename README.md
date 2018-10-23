------------------------
Project Description
------------------------
In this mini project, I have made used of previously developed bit accurate model for addition and multiplication of floating point, fixed point and mu-law numbers. 
The input activation point is weighed summed with theta point which are the trained neuron weights in actual model to obtain neuron activation point. 
The weighted sum in then passed through a function, in this case ReLU function, to obtain final activation point.  

The input activation point and thetha values are given to the code through a an excel file. The code reads the excel file and then performs weighted sum operation on it. 
The code then passes the results through an ReLU function to get final activation point. Previously developed fixed point number representation model is used here to display 
the activation point of each neuron in fixed point format. 