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
//pop pointer 1 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@3
D=A   // baseAddr of pointer
@1
D=D+A   //D=address of pointer 1
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
////////////////////
//push constant 0
@0                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 0  
@SP          
M=M+1  //SP++
////////////////////
//pop that 0 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@THAT
D=M   // baseAddr of that
@0
D=D+A   //D=address of that 0
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
////////////////////
//push constant 1
@1                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 1  
@SP          
M=M+1  //SP++
////////////////////
//pop that 1 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@THAT
D=M   // baseAddr of that
@1
D=D+A   //D=address of that 1
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
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
//push constant 2
@2                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 2  
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
////////////////////
//pop argument 0 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@ARG
D=M   // baseAddr of argument
@0
D=D+A   //D=address of argument 0
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
////////////////////
// label MAIN_LOOP_START
(MAIN_LOOP_START)
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
// if-goto COMPUTE_ELEMENT    
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@COMPUTE_ELEMENT
D;JNE       
////////////////////
// goto END_PROGRAM
@END_PROGRAM
0;JMP
////////////////////
// label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
////////////////////
//push that 0
@THAT
D=M   // baseAddr of that
@0                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//push that 1
@THAT
D=M   // baseAddr of that
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
//pop that 2 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@THAT
D=M   // baseAddr of that
@2
D=D+A   //D=address of that 2
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
////////////////////
//push pointer 1
@3
D=A   // baseAddr of pointer
@1                
A=D+A //D=segment+i 
D=M                 
                    
@SP                 
A=M                 
M=D    // *SP = D   
@SP          
M=M+1  //SP++
////////////////////
//push constant 1
@1                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 1  
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
//pop pointer 1 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@3
D=A   // baseAddr of pointer
@1
D=D+A   //D=address of pointer 1
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
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
//push constant 1
@1                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 1  
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
////////////////////
//pop argument 0 
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@R13
M=D 
@ARG
D=M   // baseAddr of argument
@0
D=D+A   //D=address of argument 0
@R14
M=D 
@R13
D=M 
@R14
A=M 
M=D 
////////////////////
// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
////////////////////
// label END_PROGRAM
(END_PROGRAM)
