@256//0
D=A//1
@SP//2
M=D//3
////////////////////
// call Sys.init 0
@None.RET_0//4
D=A//5
@SP        //6
A=M        //7
M=D //*SP=D//8
@SP          //9
M=M+1  //SP++//10
@LCL//11
D=M//12
@SP        //13
A=M        //14
M=D //*SP=D//15
@SP          //16
M=M+1  //SP++//17
@ARG//18
D=M//19
@SP        //20
A=M        //21
M=D //*SP=D//22
@SP          //23
M=M+1  //SP++//24
@THIS//25
D=M//26
@SP        //27
A=M        //28
M=D //*SP=D//29
@SP          //30
M=M+1  //SP++//31
@THAT//32
D=M//33
@SP        //34
A=M        //35
M=D //*SP=D//36
@SP          //37
M=M+1  //SP++//38
@SP       //39
D=M       //40
@5        //41
D=D-A     //42
@0//43
D=D-A     //44
@ARG      //45
M=D       //46
@SP //47
D=M //48
@LCL//49
M=D //50
////////////////////
// goto Sys.init
@Sys.init//51
0;JMP//52
(None.RET_0)//53
/////////////////////////////////////////////
// FILE: Class1                          
////////////////////
// function Class1.set 0
(Class1.set)//53
////////////////////
//push argument 0
@ARG//53
D=M   // baseAddr of argument//54
@0                //55
A=D+A //A=segment+i //56
D=M                 //57
@SP        //58
A=M        //59
M=D //*SP=D//60
@SP          //61
M=M+1  //SP++//62
////////////////////
//pop static 0 
@SP          //63
M=M-1  //SP--//64
A=M         //65
D=M  //D=*SP//66
@R13//67
M=D //68
@16//69
D=A   // baseAddr of static//70
@0//71
D=D+A   //D=address of static 0//72
@R6//73
M=D //74
@R13//75
D=M //76
@R6//77
A=M //78
M=D //79
////////////////////
//push argument 1
@ARG//80
D=M   // baseAddr of argument//81
@1                //82
A=D+A //A=segment+i //83
D=M                 //84
@SP        //85
A=M        //86
M=D //*SP=D//87
@SP          //88
M=M+1  //SP++//89
////////////////////
//pop static 1 
@SP          //90
M=M-1  //SP--//91
A=M         //92
D=M  //D=*SP//93
@R13//94
M=D //95
@16//96
D=A   // baseAddr of static//97
@1//98
D=D+A   //D=address of static 1//99
@R6//100
M=D //101
@R13//102
D=M //103
@R6//104
A=M //105
M=D //106
////////////////////
//push constant 0
@0//107
D=A //108
@SP        //109
A=M        //110
M=D //*SP=D//111
@SP          //112
M=M+1  //SP++//113
////////////////////
// return
@LCL//114
D=M//115
@R13//116
M=D//117
@R13//118
D=M//119
@5//120
A=D-A//121
D=M//122
@R14//123
M=D//124
@SP          //125
M=M-1  //SP--//126
A=M         //127
D=M  //D=*SP//128
@ARG//129
A=M//130
M=D//131
D=1//132
@ARG//133
D=M+D//134
@SP//135
M=D//136
@R13//137
D=M//138
@1//139
D=D-A//140
A=D//141
D=M//142
@THAT//143
M=D//144
@R13//145
D=M//146
@2//147
D=D-A//148
A=D//149
D=M//150
@THIS//151
M=D//152
@R13//153
D=M//154
@3//155
D=D-A//156
A=D//157
D=M//158
@ARG//159
M=D//160
@R13//161
D=M//162
@4//163
D=D-A//164
A=D//165
D=M//166
@LCL//167
M=D//168
@R14//169
A=M//170
0;JMP//171
////////////////////
// function Class1.get 0
(Class1.get)//172
////////////////////
//push static 0
@16//172
D=A   // baseAddr of static//173
@0                //174
A=D+A //A=segment+i //175
D=M                 //176
@SP        //177
A=M        //178
M=D //*SP=D//179
@SP          //180
M=M+1  //SP++//181
////////////////////
//push static 1
@16//182
D=A   // baseAddr of static//183
@1                //184
A=D+A //A=segment+i //185
D=M                 //186
@SP        //187
A=M        //188
M=D //*SP=D//189
@SP          //190
M=M+1  //SP++//191
////////////////////
//sub
@SP          //192
M=M-1  //SP--//193
A=M         //194
D=M  //D=*SP//195
@SP          //196
M=M-1  //SP--//197
A=M         //198
A=M  //A=*SP//199
D=A-D//200
@SP        //201
A=M        //202
M=D //*SP=D//203
@SP          //204
M=M+1  //SP++//205
////////////////////
// return
@LCL//206
D=M//207
@R13//208
M=D//209
@R13//210
D=M//211
@5//212
A=D-A//213
D=M//214
@R14//215
M=D//216
@SP          //217
M=M-1  //SP--//218
A=M         //219
D=M  //D=*SP//220
@ARG//221
A=M//222
M=D//223
D=1//224
@ARG//225
D=M+D//226
@SP//227
M=D//228
@R13//229
D=M//230
@1//231
D=D-A//232
A=D//233
D=M//234
@THAT//235
M=D//236
@R13//237
D=M//238
@2//239
D=D-A//240
A=D//241
D=M//242
@THIS//243
M=D//244
@R13//245
D=M//246
@3//247
D=D-A//248
A=D//249
D=M//250
@ARG//251
M=D//252
@R13//253
D=M//254
@4//255
D=D-A//256
A=D//257
D=M//258
@LCL//259
M=D//260
@R14//261
A=M//262
0;JMP//263
/////////////////////////////////////////////
// FILE: Class2                          
////////////////////
// function Class2.set 0
(Class2.set)//264
////////////////////
//push argument 0
@ARG//264
D=M   // baseAddr of argument//265
@0                //266
A=D+A //A=segment+i //267
D=M                 //268
@SP        //269
A=M        //270
M=D //*SP=D//271
@SP          //272
M=M+1  //SP++//273
////////////////////
//pop static 0 
@SP          //274
M=M-1  //SP--//275
A=M         //276
D=M  //D=*SP//277
@R13//278
M=D //279
@16//280
D=A   // baseAddr of static//281
@0//282
D=D+A   //D=address of static 0//283
@R6//284
M=D //285
@R13//286
D=M //287
@R6//288
A=M //289
M=D //290
////////////////////
//push argument 1
@ARG//291
D=M   // baseAddr of argument//292
@1                //293
A=D+A //A=segment+i //294
D=M                 //295
@SP        //296
A=M        //297
M=D //*SP=D//298
@SP          //299
M=M+1  //SP++//300
////////////////////
//pop static 1 
@SP          //301
M=M-1  //SP--//302
A=M         //303
D=M  //D=*SP//304
@R13//305
M=D //306
@16//307
D=A   // baseAddr of static//308
@1//309
D=D+A   //D=address of static 1//310
@R6//311
M=D //312
@R13//313
D=M //314
@R6//315
A=M //316
M=D //317
////////////////////
//push constant 0
@0//318
D=A //319
@SP        //320
A=M        //321
M=D //*SP=D//322
@SP          //323
M=M+1  //SP++//324
////////////////////
// return
@LCL//325
D=M//326
@R13//327
M=D//328
@R13//329
D=M//330
@5//331
A=D-A//332
D=M//333
@R14//334
M=D//335
@SP          //336
M=M-1  //SP--//337
A=M         //338
D=M  //D=*SP//339
@ARG//340
A=M//341
M=D//342
D=1//343
@ARG//344
D=M+D//345
@SP//346
M=D//347
@R13//348
D=M//349
@1//350
D=D-A//351
A=D//352
D=M//353
@THAT//354
M=D//355
@R13//356
D=M//357
@2//358
D=D-A//359
A=D//360
D=M//361
@THIS//362
M=D//363
@R13//364
D=M//365
@3//366
D=D-A//367
A=D//368
D=M//369
@ARG//370
M=D//371
@R13//372
D=M//373
@4//374
D=D-A//375
A=D//376
D=M//377
@LCL//378
M=D//379
@R14//380
A=M//381
0;JMP//382
////////////////////
// function Class2.get 0
(Class2.get)//383
////////////////////
//push static 0
@16//383
D=A   // baseAddr of static//384
@0                //385
A=D+A //A=segment+i //386
D=M                 //387
@SP        //388
A=M        //389
M=D //*SP=D//390
@SP          //391
M=M+1  //SP++//392
////////////////////
//push static 1
@16//393
D=A   // baseAddr of static//394
@1                //395
A=D+A //A=segment+i //396
D=M                 //397
@SP        //398
A=M        //399
M=D //*SP=D//400
@SP          //401
M=M+1  //SP++//402
////////////////////
//sub
@SP          //403
M=M-1  //SP--//404
A=M         //405
D=M  //D=*SP//406
@SP          //407
M=M-1  //SP--//408
A=M         //409
A=M  //A=*SP//410
D=A-D//411
@SP        //412
A=M        //413
M=D //*SP=D//414
@SP          //415
M=M+1  //SP++//416
////////////////////
// return
@LCL//417
D=M//418
@R13//419
M=D//420
@R13//421
D=M//422
@5//423
A=D-A//424
D=M//425
@R14//426
M=D//427
@SP          //428
M=M-1  //SP--//429
A=M         //430
D=M  //D=*SP//431
@ARG//432
A=M//433
M=D//434
D=1//435
@ARG//436
D=M+D//437
@SP//438
M=D//439
@R13//440
D=M//441
@1//442
D=D-A//443
A=D//444
D=M//445
@THAT//446
M=D//447
@R13//448
D=M//449
@2//450
D=D-A//451
A=D//452
D=M//453
@THIS//454
M=D//455
@R13//456
D=M//457
@3//458
D=D-A//459
A=D//460
D=M//461
@ARG//462
M=D//463
@R13//464
D=M//465
@4//466
D=D-A//467
A=D//468
D=M//469
@LCL//470
M=D//471
@R14//472
A=M//473
0;JMP//474
/////////////////////////////////////////////
// FILE: Sys                          
////////////////////
// function Sys.init 0
(Sys.init)//475
////////////////////
//push constant 6
@6//475
D=A //476
@SP        //477
A=M        //478
M=D //*SP=D//479
@SP          //480
M=M+1  //SP++//481
////////////////////
//push constant 8
@8//482
D=A //483
@SP        //484
A=M        //485
M=D //*SP=D//486
@SP          //487
M=M+1  //SP++//488
////////////////////
// call Class1.set 2
@Sys.RET_1//489
D=A//490
@SP        //491
A=M        //492
M=D //*SP=D//493
@SP          //494
M=M+1  //SP++//495
@LCL//496
D=M//497
@SP        //498
A=M        //499
M=D //*SP=D//500
@SP          //501
M=M+1  //SP++//502
@ARG//503
D=M//504
@SP        //505
A=M        //506
M=D //*SP=D//507
@SP          //508
M=M+1  //SP++//509
@THIS//510
D=M//511
@SP        //512
A=M        //513
M=D //*SP=D//514
@SP          //515
M=M+1  //SP++//516
@THAT//517
D=M//518
@SP        //519
A=M        //520
M=D //*SP=D//521
@SP          //522
M=M+1  //SP++//523
@SP       //524
D=M       //525
@5        //526
D=D-A     //527
@2//528
D=D-A     //529
@ARG      //530
M=D       //531
@SP //532
D=M //533
@LCL//534
M=D //535
////////////////////
// goto Class1.set
@Class1.set//536
0;JMP//537
(Sys.RET_1)//538
////////////////////
//pop temp 0 
@0//538
@0//539
@0//540
@0//541
@0//542
@0//543
@0//544
@0//545
@SP          //546
M=M-1  //SP--//547
A=M         //548
D=M  //D=*SP//549
@R13//550
M=D //551
@5//552
D=A   // baseAddr of temp//553
@0//554
D=D+A   //D=address of temp 0//555
@R6//556
M=D //557
@R13//558
D=M //559
@R6//560
A=M //561
M=D //562
@1//563
@1//564
@1//565
@1//566
@1//567
@1//568
@1//569
@1//570
@1//571
@1//572
@1//573
////////////////////
//push constant 23
@23//574
D=A //575
@SP        //576
A=M        //577
M=D //*SP=D//578
@SP          //579
M=M+1  //SP++//580
////////////////////
//push constant 15
@15//581
D=A //582
@SP        //583
A=M        //584
M=D //*SP=D//585
@SP          //586
M=M+1  //SP++//587
////////////////////
// call Class2.set 2
@Sys.RET_2//588
D=A//589
@SP        //590
A=M        //591
M=D //*SP=D//592
@SP          //593
M=M+1  //SP++//594
@LCL//595
D=M//596
@SP        //597
A=M        //598
M=D //*SP=D//599
@SP          //600
M=M+1  //SP++//601
@ARG//602
D=M//603
@SP        //604
A=M        //605
M=D //*SP=D//606
@SP          //607
M=M+1  //SP++//608
@THIS//609
D=M//610
@SP        //611
A=M        //612
M=D //*SP=D//613
@SP          //614
M=M+1  //SP++//615
@THAT//616
D=M//617
@SP        //618
A=M        //619
M=D //*SP=D//620
@SP          //621
M=M+1  //SP++//622
@SP       //623
D=M       //624
@5        //625
D=D-A     //626
@2//627
D=D-A     //628
@ARG      //629
M=D       //630
@SP //631
D=M //632
@LCL//633
M=D //634
////////////////////
// goto Class2.set
@Class2.set//635
0;JMP//636
(Sys.RET_2)//637
////////////////////
//pop temp 0 
@0//637
@0//638
@0//639
@0//640
@0//641
@0//642
@0//643
@0//644
@SP          //645
M=M-1  //SP--//646
A=M         //647
D=M  //D=*SP//648
@R13//649
M=D //650
@5//651
D=A   // baseAddr of temp//652
@0//653
D=D+A   //D=address of temp 0//654
@R6//655
M=D //656
@R13//657
D=M //658
@R6//659
A=M //660
M=D //661
@1//662
@1//663
@1//664
@1//665
@1//666
@1//667
@1//668
@1//669
@1//670
@1//671
@1//672
////////////////////
// call Class1.get 0
@Sys.RET_3//673
D=A//674
@SP        //675
A=M        //676
M=D //*SP=D//677
@SP          //678
M=M+1  //SP++//679
@LCL//680
D=M//681
@SP        //682
A=M        //683
M=D //*SP=D//684
@SP          //685
M=M+1  //SP++//686
@ARG//687
D=M//688
@SP        //689
A=M        //690
M=D //*SP=D//691
@SP          //692
M=M+1  //SP++//693
@THIS//694
D=M//695
@SP        //696
A=M        //697
M=D //*SP=D//698
@SP          //699
M=M+1  //SP++//700
@THAT//701
D=M//702
@SP        //703
A=M        //704
M=D //*SP=D//705
@SP          //706
M=M+1  //SP++//707
@SP       //708
D=M       //709
@5        //710
D=D-A     //711
@0//712
D=D-A     //713
@ARG      //714
M=D       //715
@SP //716
D=M //717
@LCL//718
M=D //719
////////////////////
// goto Class1.get
@Class1.get//720
0;JMP//721
(Sys.RET_3)//722
////////////////////
// call Class2.get 0
@Sys.RET_4//722
D=A//723
@SP        //724
A=M        //725
M=D //*SP=D//726
@SP          //727
M=M+1  //SP++//728
@LCL//729
D=M//730
@SP        //731
A=M        //732
M=D //*SP=D//733
@SP          //734
M=M+1  //SP++//735
@ARG//736
D=M//737
@SP        //738
A=M        //739
M=D //*SP=D//740
@SP          //741
M=M+1  //SP++//742
@THIS//743
D=M//744
@SP        //745
A=M        //746
M=D //*SP=D//747
@SP          //748
M=M+1  //SP++//749
@THAT//750
D=M//751
@SP        //752
A=M        //753
M=D //*SP=D//754
@SP          //755
M=M+1  //SP++//756
@SP       //757
D=M       //758
@5        //759
D=D-A     //760
@0//761
D=D-A     //762
@ARG      //763
M=D       //764
@SP //765
D=M //766
@LCL//767
M=D //768
////////////////////
// goto Class2.get
@Class2.get//769
0;JMP//770
(Sys.RET_4)//771
////////////////////
// label WHILE
(WHILE)//771
////////////////////
// goto WHILE
@WHILE//771
0;JMP//772