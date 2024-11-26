# Generated from grammarTraductor.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,1,1,1,4,1,40,8,1,
        11,1,12,1,41,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,4,3,4,67,8,4,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,76,8,6,4,6,78,8,6,11,6,12,6,79,1,7,
        1,7,1,7,1,7,3,7,86,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,95,8,9,1,
        10,1,10,1,10,5,10,100,8,10,10,10,12,10,103,9,10,1,11,1,11,1,11,5,
        11,108,8,11,10,11,12,11,111,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,120,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,130,
        8,14,10,14,12,14,133,9,14,1,14,3,14,136,8,14,1,14,0,0,15,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,0,2,1,0,5,6,1,0,7,8,141,0,34,1,0,
        0,0,2,44,1,0,0,0,4,46,1,0,0,0,6,50,1,0,0,0,8,66,1,0,0,0,10,68,1,
        0,0,0,12,77,1,0,0,0,14,85,1,0,0,0,16,87,1,0,0,0,18,91,1,0,0,0,20,
        96,1,0,0,0,22,104,1,0,0,0,24,119,1,0,0,0,26,121,1,0,0,0,28,135,1,
        0,0,0,30,33,3,2,1,0,31,33,3,4,2,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,1,1,0,0,0,36,34,1,0,0,
        0,37,39,3,14,7,0,38,40,5,16,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,
        1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,45,3,14,7,0,44,37,1,0,0,0,
        44,43,1,0,0,0,45,3,1,0,0,0,46,47,3,6,3,0,47,48,5,16,0,0,48,49,3,
        12,6,0,49,5,1,0,0,0,50,51,5,1,0,0,51,52,5,3,0,0,52,53,5,10,0,0,53,
        54,3,8,4,0,54,55,5,11,0,0,55,56,5,12,0,0,56,7,1,0,0,0,57,62,3,10,
        5,0,58,59,5,13,0,0,59,61,3,10,5,0,60,58,1,0,0,0,61,64,1,0,0,0,62,
        60,1,0,0,0,62,63,1,0,0,0,63,67,1,0,0,0,64,62,1,0,0,0,65,67,1,0,0,
        0,66,57,1,0,0,0,66,65,1,0,0,0,67,9,1,0,0,0,68,69,5,3,0,0,69,11,1,
        0,0,0,70,75,5,15,0,0,71,72,3,14,7,0,72,73,5,16,0,0,73,76,1,0,0,0,
        74,76,3,14,7,0,75,71,1,0,0,0,75,74,1,0,0,0,76,78,1,0,0,0,77,70,1,
        0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,13,1,0,0,0,81,
        86,3,16,8,0,82,86,3,18,9,0,83,86,3,26,13,0,84,86,3,20,10,0,85,81,
        1,0,0,0,85,82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,15,1,0,0,0,
        87,88,5,3,0,0,88,89,5,9,0,0,89,90,3,20,10,0,90,17,1,0,0,0,91,94,
        5,2,0,0,92,95,3,20,10,0,93,95,5,3,0,0,94,92,1,0,0,0,94,93,1,0,0,
        0,95,19,1,0,0,0,96,101,3,22,11,0,97,98,7,0,0,0,98,100,3,22,11,0,
        99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,
        21,1,0,0,0,103,101,1,0,0,0,104,109,3,24,12,0,105,106,7,1,0,0,106,
        108,3,24,12,0,107,105,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,
        110,1,0,0,0,110,23,1,0,0,0,111,109,1,0,0,0,112,120,5,4,0,0,113,120,
        3,26,13,0,114,115,5,10,0,0,115,116,3,20,10,0,116,117,5,11,0,0,117,
        120,1,0,0,0,118,120,5,3,0,0,119,112,1,0,0,0,119,113,1,0,0,0,119,
        114,1,0,0,0,119,118,1,0,0,0,120,25,1,0,0,0,121,122,5,3,0,0,122,123,
        5,10,0,0,123,124,3,28,14,0,124,125,5,11,0,0,125,27,1,0,0,0,126,131,
        3,20,10,0,127,128,5,13,0,0,128,130,3,20,10,0,129,127,1,0,0,0,130,
        133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,136,1,0,0,0,133,
        131,1,0,0,0,134,136,1,0,0,0,135,126,1,0,0,0,135,134,1,0,0,0,136,
        29,1,0,0,0,15,32,34,41,44,62,66,75,79,85,94,101,109,119,131,135
    ]

class grammarTraductorParser ( Parser ):

    grammarFileName = "grammarTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'('", "')'", "':'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "ID", "CONT", "PLUS", 
                      "MINUS", "MULT", "DIVI", "EQUALS", "LPAREN", "RPAREN", 
                      "COLON", "COMMA", "WS", "INDENT", "NEWLINE", "COMMENT" ]

    RULE_program = 0
    RULE_statement_root = 1
    RULE_function = 2
    RULE_function_declaration = 3
    RULE_param_list = 4
    RULE_param = 5
    RULE_code_block = 6
    RULE_statement = 7
    RULE_assignment = 8
    RULE_return_statement = 9
    RULE_expr = 10
    RULE_term = 11
    RULE_factor = 12
    RULE_function_call = 13
    RULE_arg_list = 14

    ruleNames =  [ "program", "statement_root", "function", "function_declaration", 
                   "param_list", "param", "code_block", "statement", "assignment", 
                   "return_statement", "expr", "term", "factor", "function_call", 
                   "arg_list" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    ID=3
    CONT=4
    PLUS=5
    MINUS=6
    MULT=7
    DIVI=8
    EQUALS=9
    LPAREN=10
    RPAREN=11
    COLON=12
    COMMA=13
    WS=14
    INDENT=15
    NEWLINE=16
    COMMENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_root(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.Statement_rootContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.Statement_rootContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.FunctionContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.FunctionContext,i)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarTraductorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1054) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4, 10]:
                    self.state = 30
                    self.statement_root()
                    pass
                elif token in [1]:
                    self.state = 31
                    self.function()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_rootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(grammarTraductorParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.NEWLINE)
            else:
                return self.getToken(grammarTraductorParser.NEWLINE, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_statement_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_root" ):
                listener.enterStatement_root(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_root" ):
                listener.exitStatement_root(self)




    def statement_root(self):

        localctx = grammarTraductorParser.Statement_rootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_root)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 38
                    self.match(grammarTraductorParser.NEWLINE)
                    self.state = 41 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==16):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(grammarTraductorParser.Function_declarationContext,0)


        def NEWLINE(self):
            return self.getToken(grammarTraductorParser.NEWLINE, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarTraductorParser.Code_blockContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = grammarTraductorParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.function_declaration()
            self.state = 47
            self.match(grammarTraductorParser.NEWLINE)
            self.state = 48
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarTraductorParser.DEF, 0)

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(grammarTraductorParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(grammarTraductorParser.COLON, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)




    def function_declaration(self):

        localctx = grammarTraductorParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(grammarTraductorParser.DEF)
            self.state = 51
            self.match(grammarTraductorParser.ID)
            self.state = 52
            self.match(grammarTraductorParser.LPAREN)
            self.state = 53
            self.param_list()
            self.state = 54
            self.match(grammarTraductorParser.RPAREN)
            self.state = 55
            self.match(grammarTraductorParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.ParamContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.COMMA)
            else:
                return self.getToken(grammarTraductorParser.COMMA, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = grammarTraductorParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.param()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 58
                    self.match(grammarTraductorParser.COMMA)
                    self.state = 59
                    self.param()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = grammarTraductorParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(grammarTraductorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.INDENT)
            else:
                return self.getToken(grammarTraductorParser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.NEWLINE)
            else:
                return self.getToken(grammarTraductorParser.NEWLINE, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = grammarTraductorParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.match(grammarTraductorParser.INDENT)
                self.state = 75
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.statement()
                    self.state = 72
                    self.match(grammarTraductorParser.NEWLINE)
                    pass

                elif la_ == 2:
                    self.state = 74
                    self.statement()
                    pass


                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(grammarTraductorParser.AssignmentContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(grammarTraductorParser.Return_statementContext,0)


        def function_call(self):
            return self.getTypedRuleContext(grammarTraductorParser.Function_callContext,0)


        def expr(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExprContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarTraductorParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.return_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def EQUALS(self):
            return self.getToken(grammarTraductorParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExprContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = grammarTraductorParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(grammarTraductorParser.ID)
            self.state = 88
            self.match(grammarTraductorParser.EQUALS)
            self.state = 89
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(grammarTraductorParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExprContext,0)


        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = grammarTraductorParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(grammarTraductorParser.RETURN)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 92
                self.expr()
                pass

            elif la_ == 2:
                self.state = 93
                self.match(grammarTraductorParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.TermContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.PLUS)
            else:
                return self.getToken(grammarTraductorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.MINUS)
            else:
                return self.getToken(grammarTraductorParser.MINUS, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = grammarTraductorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.term()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 97
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 98
                self.term()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.FactorContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.MULT)
            else:
                return self.getToken(grammarTraductorParser.MULT, i)

        def DIVI(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.DIVI)
            else:
                return self.getToken(grammarTraductorParser.DIVI, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = grammarTraductorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.factor()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.factor()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(grammarTraductorParser.CONT, 0)

        def function_call(self):
            return self.getTypedRuleContext(grammarTraductorParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = grammarTraductorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(grammarTraductorParser.CONT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.function_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(grammarTraductorParser.LPAREN)
                self.state = 115
                self.expr()
                self.state = 116
                self.match(grammarTraductorParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(grammarTraductorParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(grammarTraductorParser.Arg_listContext,0)


        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = grammarTraductorParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(grammarTraductorParser.ID)
            self.state = 122
            self.match(grammarTraductorParser.LPAREN)
            self.state = 123
            self.arg_list()
            self.state = 124
            self.match(grammarTraductorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.COMMA)
            else:
                return self.getToken(grammarTraductorParser.COMMA, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = grammarTraductorParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.expr()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 127
                    self.match(grammarTraductorParser.COMMA)
                    self.state = 128
                    self.expr()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





