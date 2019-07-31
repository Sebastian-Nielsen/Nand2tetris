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
//pop local 0 
             
@SP          
M=M-1  //SP--
             
@SP                 
A=M                 
D=M   // D=*SP      
@R13                
M=D   // M[13]=D    // store popped value temporarily in R13 
@LCL
D=M   // baseAddr of local          
@0                
D=D+A  //D = address of 'local 0'    
@R14                
M=D                 
@R13                
D=M                 
@R14                 
A=M                 
M=D                 
////////////////////
//pop local 2 
             
@SP          
M=M-1  //SP--
             
@SP                 
A=M                 
D=M   // D=*SP      
@R13                
M=D   // M[13]=D    // store popped value temporarily in R13 
@LCL
D=M   // baseAddr of local          
@2                
D=D+A  //D = address of 'local 2'    
@R14                
M=D                 
@R13                
D=M                 
@R14                 
A=M                 
M=D                 
