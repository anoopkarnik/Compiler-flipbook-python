# flipbook_compiler

## Files Description 

1) fc - bash file which first compiles our code file in our language using main.py file into out.py file and then runs the out.py file to generate video.

2) main.py - It just takes input from lex.py(our token generator), parser.py (our parser) and emit.py (our code generator) to compile our language file into python format.

3) lex.py = File taking care of token generation and recognition

4) parser.py = File taking care of parsing our tokens

5) emit.py = File taking care of code conversion from our language to python

6) *.flip = Files containing sample codes in our language

## Example Run: 

1) We first make our bash file executable - "chmod +x fc"

2) We then run the bash file with two arguments our sample code and output file name - "./fc trial.flip output.mp4"

