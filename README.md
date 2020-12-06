# flipbook_compiler 

##( Work in Progress - video, examples flips, programming language documentations and more functionalities still pending)

## Files Description 

1) fc - bash file which first compiles our code file in our language using main.py file into out.py file and then runs the out.py file to generate video.

2) main.py - It just takes input from lex.py(our token generator), parser.py (our parser) and emit.py (our code generator) to compile our language file into python format.

3) lex.py = File taking care of token generation and recognition

4) parser.py = File taking care of parsing our tokens

5) emit.py = File taking care of code conversion from our language to python

6) *.flip = Files containing sample codes in our language

## Example Run: 

1) We first make our bash file executable - "chmod +x fc"

- Folder name method(If you have folder location and want to use all the images in it as just one frame)

2a) We then run the bash file with two arguments our sample code and output file name which then asks us for folder names in which our image files, after we are asked to give frame rate per second of the vidoe then a video file is generated.

ex - i) ./fc 1.flip 1.mp4   

     ii) images (example value to give when asked for folder name)
     
     iii) 5 (example value to give when asked for frame rate per second)

- File name method (If you want to individually specify each imagepath and number of frames it occupies in our video) 

2b) We then run the bash file with two arguments our sample code and output file name - "./fc 1.flip output.mp4" which then asks us for number of files, then we mention each file name and the frames it occupies in each line, after we are asked to give frame rate per second of the video then a video file is generated.

ex - i) ./fc 2.flip 2.mp4   

     ii) 5 (example value to give when asked for number of files)
     
     iii) images/1.jpg 5 (example values to give for the 1st image and frames it occupies)
     
     iv) images/2.jpg 15 (example values to give for the 2nd image and frames it occupies)
     
      v) images/3.jpg 10 (example values to give for the 3rd image and frames it occupies)
      
     vi) images/4.jpg 6 (example values to give for the 4th image and frames it occupies)
     
     vii) images/5.jpg 2 (example values to give for the 5th image and frames it occupies)
     
     viii) 10 (example value to give when asked for frame rate per second)


