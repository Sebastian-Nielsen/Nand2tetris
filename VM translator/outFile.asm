////////////////////
//push constant 17
@17                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 17  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 17
@17                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 17  
             
@SP          
M=M+1  //SP++
             
////////////////////
//eq
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_0_TRUE
D;JEQ
D=0             
@Bool_0_FALSE 
0;JMP           
(Bool_0_TRUE) 
D=-1            
(Bool_0_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 17
@17                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 17  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 16
@16                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 16  
             
@SP          
M=M+1  //SP++
             
////////////////////
//eq
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_1_TRUE
D;JEQ
D=0             
@Bool_1_FALSE 
0;JMP           
(Bool_1_TRUE) 
D=-1            
(Bool_1_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 16
@16                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 16  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 17
@17                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 17  
             
@SP          
M=M+1  //SP++
             
////////////////////
//eq
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_2_TRUE
D;JEQ
D=0             
@Bool_2_FALSE 
0;JMP           
(Bool_2_TRUE) 
D=-1            
(Bool_2_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 892
@892                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 892  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 891
@891                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 891  
             
@SP          
M=M+1  //SP++
             
////////////////////
//lt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_3_TRUE
D;JLT
D=0             
@Bool_3_FALSE 
0;JMP           
(Bool_3_TRUE) 
D=-1            
(Bool_3_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 891
@891                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 891  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 892
@892                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 892  
             
@SP          
M=M+1  //SP++
             
////////////////////
//lt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_4_TRUE
D;JLT
D=0             
@Bool_4_FALSE 
0;JMP           
(Bool_4_TRUE) 
D=-1            
(Bool_4_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 891
@891                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 891  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 891
@891                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 891  
             
@SP          
M=M+1  //SP++
             
////////////////////
//lt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_5_TRUE
D;JLT
D=0             
@Bool_5_FALSE 
0;JMP           
(Bool_5_TRUE) 
D=-1            
(Bool_5_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32767
@32767                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32767  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32766
@32766                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32766  
             
@SP          
M=M+1  //SP++
             
////////////////////
//gt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_6_TRUE
D;JGT
D=0             
@Bool_6_FALSE 
0;JMP           
(Bool_6_TRUE) 
D=-1            
(Bool_6_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32766
@32766                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32766  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32767
@32767                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32767  
             
@SP          
M=M+1  //SP++
             
////////////////////
//gt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_7_TRUE
D;JGT
D=0             
@Bool_7_FALSE 
0;JMP           
(Bool_7_TRUE) 
D=-1            
(Bool_7_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32766
@32766                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32766  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 32766
@32766                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 32766  
             
@SP          
M=M+1  //SP++
             
////////////////////
//gt
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A-D
@Bool_8_TRUE
D;JGT
D=0             
@Bool_8_FALSE 
0;JMP           
(Bool_8_TRUE) 
D=-1            
(Bool_8_FALSE)
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 57
@57                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 57  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 31
@31                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 31  
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 53
@53                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 53  
             
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
//push constant 112
@112                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 112  
             
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
//neg
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
D=-D
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//and
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A&D
@SP        
A=M        
M=D //*SP=D
             
@SP          
M=M+1  //SP++
             
////////////////////
//push constant 82
@82                
D=A                 
@SP                 
A=M                 
M=D   // *SP = 82  
             
@SP          
M=M+1  //SP++
             
////////////////////
//or
@SP          
M=M-1  //SP--
A=M         
D=M  //D=*SP
@SP          
M=M-1  //SP--
A=M         
A=M  //A=*SP
D=A|D
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
             
