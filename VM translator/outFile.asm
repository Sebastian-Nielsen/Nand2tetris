////////////////////
//push constant 7
@7                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 7  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 8
@8                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 8  
             
@SP          
M=M+1  //SP++
             
////////////////////
// neg
@SP          
M=M-1  //SP--
@SP         
A=M         
D=M  //D=*SP
D=-D    
@SP     
A=M     
M=D     
             
@SP          
M=M+1  //SP++
             
