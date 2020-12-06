# flipbook_compiler 
(still working on exception catches and other functionalities already put in the programming language but not using it for our purposes)

## Base Creation

1) Please download files from below link with input images, submission video containing description of our programming language and demo and output flip videos we got - https://drive.google.com/drive/folders/1jqtHhJrx6IAH9Z1uT3svjtPDW2BHl2SV?usp=sharing
2) Download python 3.6, create an environment and activate it.
3) pip install -r requirements.txt

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

     i) ./fc 1.flip 1.mp4   

     ii) flipbook1 (images folder location which we can get from above google drive link)
     
     iii) 5 (example value to give when asked for frame rate per second)

- File name method (If you want to individually specify each imagepath and number of frames it occupies in our video) 

2b) We then run the bash file with two arguments our sample code and output file name - "./fc 1.flip output.mp4" which then asks us for number of files, then we mention each file name and the frames it occupies in each line, after we are asked to give frame rate per second of the video then a video file is generated.

      i) ./fc 2.flip 2.mp4   

     ii) 12 (example value to give when asked for number of files from flipbook2 folder we got from google drive link)
     
     iii) flipbook2/1.jpg 5 (example values to give for the 1st image and frames it occupies)
     
     iv) flipbook2/2.jpg 15 (example values to give for the 2nd image and frames it occupies)
     
      v) flipbook2/3.jpg 10 (example values to give for the 3rd image and frames it occupies)
      
     vi) flipbook2/4.jpg 6 (example values to give for the 4th image and frames it occupies)
     
     vii) flipbook2/5.jpg 2 (example values to give for the 5th image and frames it occupies)
     
     Viii) flipbook2/6.jpg 5 (example values to give for the 6th image and frames it occupies)
     
     ix) flipbook2/7.jpg 15 (example values to give for the 7th image and frames it occupies)
     
      x) flipbook2/8.jpg 10 (example values to give for the 8th image and frames it occupies)
      
     xi) flipbook2/9.jpg 6 (example values to give for the 9th image and frames it occupies)
     
     xii) flipbook2/10.jpg 2 (example values to give for the 10th image and frames it occupies)
     
     xiii) flipbook2/11.jpg 6 (example values to give for the 11th image and frames it occupies)
     
     xiv) flipbook2/12.jpg 2 (example values to give for the 12th image and frames it occupies)
     
     viii) 1 (example value to give when asked for frame rate per second)


