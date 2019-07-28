// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// sum = 0;
// for(let i=0; i<M[1]; i+0){
//	sum += M[0];
//  }
//  M[2] = sum;
//




@sum
M=0   //  sum = 0
@i
M=0   //  i = 0

(loop)
	@i
	D=M
	@R1
	D=D-M
	@loop
	D;JLT    //  if (i<M[1]): GOTO loop

	@sum
	D=M
	@R0
	D=D+M    //  sum += M[0]
	@loop
	0;JMP      // GOTO loop

	@sum
	D=M
	@R2
	M=D      //  M[@] = sum