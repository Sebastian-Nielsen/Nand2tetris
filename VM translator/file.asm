////////////////////
// function SimpleFunction.test 2
(file.SimpleFunction.test)
@0 
D=A
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
@0 
D=A
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
////////////////////
//push local 0
@LCL
D=M   // baseAddr of local
@0                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//push local 1
@LCL
D=M   // baseAddr of local
@1                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//add
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A+D
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
////////////////////
//not
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
D=!D
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
////////////////////
//push argument 0
@ARG
D=M   // baseAddr of argument
@0                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//add
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A+D
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
////////////////////
//push argument 1
@ARG
D=M   // baseAddr of argument
@1                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//sub
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@SP        
A=M        
M=D //*SP=D
@SP          
M=M+1  //SP++
@LCL
D=M
@R13
M=D
@R13
D=M
@5
D=D-A
A=D
D=M
@R14
M=D
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@ARG
A=M
M=D
@1
D=A
@ARG
D=A-D
@SP
M=D
@R13
D=A
@1
D=D-A
A=D
A=M
D=M
@THAT
M=D
@R13
D=A
@2
D=D-A
A=D
A=M
D=M
@THAT
M=D
@R13
D=A
@3
D=D-A
A=D
A=M
D=M
@THAT
M=D
@R13
D=A
@4
D=D-A
A=D
A=M
D=M
@THAT
M=D
@R14
