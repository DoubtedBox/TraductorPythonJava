# Generated from grammarTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,102,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,3,4,3,55,
        8,3,11,3,12,3,56,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,11,1,11,1,12,1,12,1,13,4,13,78,8,13,11,13,12,13,79,1,
        13,1,13,1,14,4,14,85,8,14,11,14,12,14,86,1,15,4,15,90,8,15,11,15,
        12,15,91,1,16,1,16,5,16,96,8,16,10,16,12,16,99,9,16,1,16,1,16,0,
        0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,1,0,6,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,1,0,48,57,1,0,32,32,1,0,9,9,2,0,10,10,13,13,107,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,
        1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,
        1,0,0,0,0,33,1,0,0,0,1,35,1,0,0,0,3,39,1,0,0,0,5,46,1,0,0,0,7,54,
        1,0,0,0,9,58,1,0,0,0,11,60,1,0,0,0,13,62,1,0,0,0,15,64,1,0,0,0,17,
        66,1,0,0,0,19,68,1,0,0,0,21,70,1,0,0,0,23,72,1,0,0,0,25,74,1,0,0,
        0,27,77,1,0,0,0,29,84,1,0,0,0,31,89,1,0,0,0,33,93,1,0,0,0,35,36,
        5,100,0,0,36,37,5,101,0,0,37,38,5,102,0,0,38,2,1,0,0,0,39,40,5,114,
        0,0,40,41,5,101,0,0,41,42,5,116,0,0,42,43,5,117,0,0,43,44,5,114,
        0,0,44,45,5,110,0,0,45,4,1,0,0,0,46,50,7,0,0,0,47,49,7,1,0,0,48,
        47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,6,1,0,0,
        0,52,50,1,0,0,0,53,55,7,2,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,8,1,0,0,0,58,59,5,43,0,0,59,10,1,0,0,0,
        60,61,5,45,0,0,61,12,1,0,0,0,62,63,5,42,0,0,63,14,1,0,0,0,64,65,
        5,47,0,0,65,16,1,0,0,0,66,67,5,61,0,0,67,18,1,0,0,0,68,69,5,40,0,
        0,69,20,1,0,0,0,70,71,5,41,0,0,71,22,1,0,0,0,72,73,5,58,0,0,73,24,
        1,0,0,0,74,75,5,44,0,0,75,26,1,0,0,0,76,78,7,3,0,0,77,76,1,0,0,0,
        78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,6,
        13,0,0,82,28,1,0,0,0,83,85,7,4,0,0,84,83,1,0,0,0,85,86,1,0,0,0,86,
        84,1,0,0,0,86,87,1,0,0,0,87,30,1,0,0,0,88,90,7,5,0,0,89,88,1,0,0,
        0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,32,1,0,0,0,93,97,
        5,35,0,0,94,96,8,5,0,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,
        97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,6,16,0,0,101,
        34,1,0,0,0,7,0,50,56,79,86,91,97,1,6,0,0
    ]

class grammarTraductorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    ID = 3
    CONT = 4
    PLUS = 5
    MINUS = 6
    MULT = 7
    DIVI = 8
    EQUALS = 9
    LPAREN = 10
    RPAREN = 11
    COLON = 12
    COMMA = 13
    WS = 14
    INDENT = 15
    NEWLINE = 16
    COMMENT = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'+'", "'-'", "'*'", "'/'", "'='", "'('", 
            "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "ID", "CONT", "PLUS", "MINUS", "MULT", "DIVI", 
            "EQUALS", "LPAREN", "RPAREN", "COLON", "COMMA", "WS", "INDENT", 
            "NEWLINE", "COMMENT" ]

    ruleNames = [ "DEF", "RETURN", "ID", "CONT", "PLUS", "MINUS", "MULT", 
                  "DIVI", "EQUALS", "LPAREN", "RPAREN", "COLON", "COMMA", 
                  "WS", "INDENT", "NEWLINE", "COMMENT" ]

    grammarFileName = "grammarTraductor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

