(the input of the following program should be a brainfuck program
followed by an exclamation point (!) followed by the input to the
interpreted program)
   
   The BF interpreter in BF (when filtered through a comment remover)
   looks like:

>>>,[->+>+<<]>>[-<<+>>]>++++[<++++++++>-]<+<[->>+>>+<<<<]>>>>[-<<<<+>>
>>]<<<[->>+>+<<<]>>>[-<<<+>>>]<<[>[->+<]<[-]]>[-]>[[-]<<<<->-<[->>+>>+
<<<<]>>>>[-<<<<+>>>>]<<<[->>+>+<<<]>>>[-<<<+>>>]<<[>[->+<]<[-]]>[-]>]<
<<<[->>+<<]>[->+<]>[[-]<<<[->+>+<<]>>[-<<+>>]>++++++[<+++++++>-]<+<[->
>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<
[-]>>[[-]<<<<->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>
>>]<[<[->>+<<]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<+>>>
>[-]]<<<[->+>+<<]>>[-<<+>>]>+++++[<+++++++++>-]<<[->>>+>+<<<<]>>>>[-<<
<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>[[-]<<<<->-<[
->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]
]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<++>>>>[-]]<<<[->+>+<<]
>>[-<<+>>]>++++++[<++++++++++>-]<<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+
>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>[[-]<<<<->-<[->>>+>+<<<<]>>>
>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>]<<<<[->
>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<+++>>>>[-]]<<<[->+>+<<]>>[-<<+>>]>+++
+++[<++++++++++>-]<++<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-
<<<+>>>]<[<[->>+<<]>[-]]<[-]>>[[-]<<<<->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>
]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>
+<<]>+>[<->[-]]<[<<<<++++>>>>[-]]<<<[->+>+<<]>>[-<<+>>]>+++++[<+++++++
++>-]<+<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->
>+<<]>[-]]<[-]>>[[-]<<<<->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<
]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]
]<[<<<<+++++>>>>[-]]<<<[->+>+<<]>>[-<<+>>]>++++[<+++++++++++>-]<<[->>>
+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-
]>>[[-]<<<<->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>
]<[<[->>+<<]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<++++++
>>>>[-]]<<<[->+>+<<]>>[-<<+>>]>+++++++[<+++++++++++++>-]<<[->>>+>+<<<<
]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>[[-]
<<<<->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->
>+<<]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<+++++++>>>>[-
]]<<<[->+>+<<]>>[-<<+>>]>+++++++[<+++++++++++++>-]<++<[->>>+>+<<<<]>>>
>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<]>[-]]<[-]>>[[-]<<<<
->-<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<<[->+>>+<<<]>>>[-<<<+>>>]<[<[->>+<<
]>[-]]<[-]>>]<<<<[->>>+<<<]>[->>+<<]>+>[<->[-]]<[<<<<++++++++>>>>[-]]<
<<<[->>+>+<<<]>>>[-<<<+>>>]<[<<<[->>>>>>>>>+<+<<<<<<<<]>>>>>>>>[-<<<<<
<<<+>>>>>>>>]<<<<<<<[->>>>>>>>>+<<+<<<<<<<]>>>>>>>[-<<<<<<<+>>>>>>>]>[
<[->>>>>+<<<<<]>[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>+>-]>>[-]<[->+<]<<[[-<
<<<<+>>>>>]<<<<<-]<<<<<<<<+>[-]>>[-]]<,[->+>+<<]>>[-<<+>>]>++++[<+++++
+++>-]<+<[->>+>>+<<<<]>>>>[-<<<<+>>>>]<<<[->>+>+<<<]>>>[-<<<+>>>]<<[>[
->+<]<[-]]>[-]>[[-]<<<<->-<[->>+>>+<<<<]>>>>[-<<<<+>>>>]<<<[->>+>+<<<]
>>>[-<<<+>>>]<<[>[->+<]<[-]]>[-]>]<<<<[->>+<<]>[->+<]>]<<<<<[-][->>>>>
>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>
+>-]>>[[-<+<+>>]<<[->>+<<]>[-<+>[<->[-]]]<[[-]<[->+>+<<]>>[-<<+>>]<<[[
-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[-]>>>>>>>>>[-<<<<<<<<<+>>
>>>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<<<<<<<<<]>>>>>>>>>[-<<<<<<<<<+>>>>>>
>>>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-]>>>+<<<<[[-<<<<<+>>>>>]<<<
<<-]<<<<<<<<+[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<
]>[->>>>>+<<<<<]>>>>+>-][-]]>>[-<+<+>>]<<[->>+<<]>[-[-<+>[<->[-]]]]<[[
-]<[->+>+<<]>>[-<<+>>]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<
[-]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<<<<<<<<<]>
>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-]
>>>-<<<<[[-<<<<<+>>>>>]<<<<<-]<<<<<<<<+[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<
+>>>]>>>>>>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-][-]]>>[-<+<+>>]<<[->
>+<<]>[-[-[-<+>[<->[-]]]]]<[[-]<[->+>+<<]>>[-<<+>>]<<[[-<<<<<+>>>>>]>[
-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[-]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]<<<<<<<
<<<->+[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<]>[->>>
>>+<<<<<]>>>>+>-][-]]>>[-<+<+>>]<<[->>+<<]>[-[-[-[-<+>[<->[-]]]]]]<[[-
]<[->+>+<<]>>[-<<+>>]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[
-]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]<<<<<<<<<<+>+[->>>>>>>>>+<<<<<<+<<<]>
>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-][-]]>>[-<+<+>
>]<<[->>+<<]>[-[-[-[-[-<+>[<->[-]]]]]]]<[[-]<[->+>+<<]>>[-<<+>>]<<[[-<
<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[-]>>>>>>>>>[-<<<<<<<<<+>>>>
>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<<<<<<<<<]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>
>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-]>>>.<<<<[[-<<<<<+>>>>>]<<<<<
-]<<<<<<<<+[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<]>
[->>>>>+<<<<<]>>>>+>-][-]]>>[-<+<+>>]<<[->>+<<]>[-[-[-[-[-[-<+>[<->[-]
]]]]]]]<[[-]<[->+>+<<]>>[-<<+>>]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<
-]<<<<<<<<[-]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<
<<<<<<<<]>>>>>>>>>[-<<<<<<<<<+>>>>>>>>>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<
<]>>>>+>-]>>>,<<<<[[-<<<<<+>>>>>]<<<<<-]<<<<<<<<+[->>>>>>>>>+<<<<<<+<<
<]>>>[-<<<+>>>]>>>>>>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-][-]]>>[-<+
<+>>]<<[->>+<<]>[-[-[-[-[-[-[-<+>[<->[-]]]]]]]]]<[[-]<[->+>+<<]>>[-<<+
>>]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[-]>>>>>>>>>[-<<<<<
<<<<+>>>>>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<<<<<<<<<]>>>>>>>>>[-<<<<<<<<<
+>>>>>>>>>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-]>>>[-<<<+>+>>]<<[->
>+<<]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]>[-<<<<<<+>>>>>>]>+<<<<<<
<[>>>>>>>-<<<<<<<[-]]<<<[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>[<[-
>>>>>+<<<<<]>[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>+>-]>[[-]<+[<[->>>>>+<<<<
<]>[->>>>>+<<<<<]>>>>+>>>[->>+<<<+>]<[->+<]>>>[-[-[-[-[-[-[-<<<+>>>[<<
<->>>[-]]]]]]]]]<<<[<+>[-]]>[->>+<<<+>]<[->+<]>>>[-[-[-[-[-[-[-[-<<<+>
>>[<<<->>>[-]]]]]]]]]]<<<[<->[-]]<]>[-]]<<[->>>>>+<<<<<]>>>>>+>[-]]>>[
-<+<+>>]<<[->>+<<]>[-[-[-[-[-[-[-[-<+>[<->[-]]]]]]]]]]<[[-][-]<[->+>+<
<]>>[-<<+>>]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]<<<<<<<<[-]>>>>>>>
>>[-<<<<<<<<<+>>>>>>>>>]<<<<<<<<<<[->>>>>>>>>>+<+<<<<<<<<<]>>>>>>>>>[-
<<<<<<<<<+>>>>>>>>>]>[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>>+>-]>>>[-<<<+>
+>>]<<[->>+<<]<<[[-<<<<<+>>>>>]>[-<<<<<+>>>>>]<<<<<<-]>[-<<<<<<+>>>>>>
]<<<<<<[->>>>>>>+<<<<<<<]<<<[->>>>>>>>>+<<<<<<+<<<]>>>[-<<<+>>>]>>>>>>
[<[->>>>>+<<<<<]>[->>>>>+<<<<<]>[->>>>>+<<<<<]>>>+>-]>[[-]<+[<[-<<<<<+
>>>>>]>[-<<<<<+>>>>>]<<<<<<->>>[->>+<<<+>]<[->+<]>>>[-[-[-[-[-[-[-<<<+
>>>[<<<->>>[-]]]]]]]]]<<<[<->[-]]>[->>+<<<+>]<[->+<]>>>[-[-[-[-[-[-[-[
-<<<+>>>[<<<->>>[-]]]]]]]]]]<<<[<+>[-]]<]>[-]]<<[->>>>>+<<<<<]>>>>>+>[
-]]>>]

