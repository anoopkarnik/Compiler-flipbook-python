import sys
from lex import *

class Parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.symbols = set()
        self.files = set()
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def checkToken(self, kind):
        return kind == self.curToken.kind

    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.

    def abort(self, message):
        sys.exit("Error. " + message)

        # Production rules.

    # program ::= {statement}
    # program ::= {statement}
    def program(self):
        # Since some newlines are required in our grammar, need to skip the excess.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            self.statement()

    def statement(self):
        if self.checkToken(TokenType.PRINT):
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                self.emitter.emitLine("print(\"" + self.curToken.text + "\")")
                self.nextToken()

            elif self.checkToken(TokenType.LIST):
                self.emitter.emitLine("print(" + self.curToken.text+")")
                self.nextToken()
            else:
                self.emitter.emit("print(\"{}\".format(float)(")
                self.expression()
                self.emitter.emitLine("))")
        # "IF" comparison "THEN" block "ENDIF"
        elif self.checkToken(TokenType.IF):
            self.nextToken()
            self.emitter.emit("if(")
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()
            self.emitter.emitLine("):")

            # Zero or more statements in the body.
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)

        # "WHILE" comparison "REPEAT" block "ENDWHILE"
        elif self.checkToken(TokenType.WHILE):
            self.nextToken()
            self.emitter.emit("while(")
            self.comparison()

            self.match(TokenType.REPEAT)
            self.nl()
            self.emitter.emitLine("):")

            # Zero or more statements in the loop body.
            while not self.checkToken(TokenType.ENDWHILE):
                self.emitter.emitTab("")
                self.statement()

            self.match(TokenType.ENDWHILE)
        # "LABEL" ident

        # "LET" ident = expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()

            #  Check if ident exists in symbol table. If not, declare it.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

            self.emitter.emit(self.curToken.text + " = ")
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)

            self.expression()
            self.emitter.emit("\n")
        elif self.checkToken(TokenType.INTINPUT):
            self.nextToken()

            # If variable doesn't already exist, declare it.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
            # Emit scanf but also validate the input. If invalid, set the variable to 0 and clear the input.
            self.emitter.emitLine(self.curToken.text + "= int(input())")
            self.match(TokenType.IDENT)
        elif self.checkToken(TokenType.STRINPUT):
            self.nextToken()
            # If variable doesn't already exist, declare it.
            if self.curToken.text not in self.files:
                self.files.add(self.curToken.text)
            self.emitter.emitLine(self.curToken.text + "= input()")
            self.match(TokenType.IDENT)
        elif self.checkToken(TokenType.LIST):
            self.nextToken()
            self.emitter.emitLine(self.curToken.text + " = []")
            self.nextToken()
        elif self.checkToken(TokenType.LISTINPUT):
            self.nextToken()
            self.emitter.emitLine(self.curToken.text +".append(input())" )
            self.nextToken()
        elif self.checkToken(TokenType.CREATE):
            self.nextToken()
            if self.curToken.text == 'FOLDER':
                self.nextToken()
                self.emitter.headerLine("import cv2")
                self.emitter.headerLine("import glob")
                self.emitter.headerLine("import sys")
                self.emitter.emitLine("img_array = []")
                self.emitter.emitLine("img_loc = []")
                self.emitter.emitLine("img_types = [\'*JPG\',\'*jpg\',\'*png\',\'*PNG\',\'*JPEG\',\'*jpeg\',\'*gif\',\'*GIF\']")
                self.emitter.emitLine("for t in img_types:")
                self.emitter.emitTab("")
                self.emitter.emitLine("img_loc.extend(glob.glob("+self.curToken.text+"+\"/\"+t))")
                self.emitter.emitLine("for file in img_loc:")
                self.emitter.emitTab("")
                self.emitter.emitLine("img = cv2.imread(file)")
                self.emitter.emitTab("")
                self.emitter.emitLine("height, width, layers = img.shape")
                self.emitter.emitTab("")
                self.emitter.emitLine("size = (width,height)")
                self.emitter.emitTab("")
                self.emitter.emitLine("img_array.append(img)")
                self.emitter.emitLine("print(\"Type frames per second of the video :\")")
                self.emitter.emitLine("fps = int(input())")
                self.emitter.emitLine("out = cv2.VideoWriter(sys.argv[1],cv2.VideoWriter_fourcc(*\'DIVX\'), fps, size)")
                self.emitter.emitLine("for i in range(len(img_array)):")
                self.emitter.emitTab("")
                self.emitter.emitLine("out.write(img_array[i])")
                self.emitter.emitLine("out.release()")
            elif self.curToken.text == 'FILE':
                self.nextToken()
                self.emitter.headerLine("import cv2")
                self.emitter.headerLine("import glob")
                self.emitter.headerLine("import sys")
                self.emitter.emitLine("img_array = []")
                self.emitter.emitLine("for file in range(int("+self.curToken.text+")):")
                self.emitter.emitTab("")
                self.emitter.emitLine("file_path,  rep = input().split()")
                self.emitter.emitTab("")
                self.emitter.emitLine("for _ in range(int(rep)):")
                self.emitter.emitTab("")
                self.emitter.emitTab("")
                self.emitter.emitLine("img = cv2.imread(file_path)")
                self.emitter.emitTab("")
                self.emitter.emitTab("")
                self.emitter.emitLine("height, width, layers = img.shape")
                self.emitter.emitTab("")
                self.emitter.emitTab("")
                self.emitter.emitLine("size = (width,height)")
                self.emitter.emitTab("")
                self.emitter.emitTab("")
                self.emitter.emitLine("img_array.append(img)")
                self.emitter.emitLine("print(\"Type frames per second of the video :\")")
                self.emitter.emitLine("fps = int(input())")
                self.emitter.emitLine("out = cv2.VideoWriter(sys.argv[1],cv2.VideoWriter_fourcc(*\'DIVX\'), fps, size)")
                self.emitter.emitLine("for i in range(len(img_array)):")
                self.emitter.emitTab("")
                self.emitter.emitLine("out.write(img_array[i])")
                self.emitter.emitLine("out.release()")
            self.nextToken()
        else:
            self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")

        # Newline.
        self.nl()

        # nl ::= '\n'+
    def nl(self):

        # Require at least one newline.
        self.match(TokenType.NEWLINE)
        # But we will allow extra newlines too, of course.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

    # comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
    def comparison(self):
        self.expression()
        # Must be at least one comparison operator and another expression.
        if self.isComparisonOperator():
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.expression()
        # Can have 0 or more comparison operator and expressions.
        while self.isComparisonOperator():
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.expression()

      # Return true if the current token is a comparison operator.
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

     # expression ::= term {( "-" | "+" ) term}
    def expression(self):
        self.term()
        # Can have 0 or more +/- and expressions.
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.term()


    # term ::= unary {( "/" | "*" ) unary}
    def term(self):
        self.unary()
        # Can have 0 or more *// and expressions.
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.unary()

    def unary(self):
        # Optional unary +/-
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
        self.primary()

    def primary(self):
        if self.checkToken(TokenType.NUMBER):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            # Ensure the variable already exists.
            if self.curToken.text not in self.symbols:
                self.abort("Referencing variable before assignment: " + self.curToken.text)

            self.emitter.emit(self.curToken.text)
            self.nextToken()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)


