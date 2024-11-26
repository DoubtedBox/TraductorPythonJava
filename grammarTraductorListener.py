# Generated from grammarTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarTraductorParser import grammarTraductorParser
else:
    from grammarTraductorParser import grammarTraductorParser

# This class defines a complete listener for a parse tree produced by grammarTraductorParser.
class grammarTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by grammarTraductorParser#program.
    def enterProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#program.
    def exitProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#statement_root.
    def enterStatement_root(self, ctx:grammarTraductorParser.Statement_rootContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statement_root.
    def exitStatement_root(self, ctx:grammarTraductorParser.Statement_rootContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#function.
    def enterFunction(self, ctx:grammarTraductorParser.FunctionContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#function.
    def exitFunction(self, ctx:grammarTraductorParser.FunctionContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#function_declaration.
    def enterFunction_declaration(self, ctx:grammarTraductorParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#function_declaration.
    def exitFunction_declaration(self, ctx:grammarTraductorParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#param_list.
    def enterParam_list(self, ctx:grammarTraductorParser.Param_listContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#param_list.
    def exitParam_list(self, ctx:grammarTraductorParser.Param_listContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#param.
    def enterParam(self, ctx:grammarTraductorParser.ParamContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#param.
    def exitParam(self, ctx:grammarTraductorParser.ParamContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#code_block.
    def enterCode_block(self, ctx:grammarTraductorParser.Code_blockContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#code_block.
    def exitCode_block(self, ctx:grammarTraductorParser.Code_blockContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#statement.
    def enterStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statement.
    def exitStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#assignment.
    def enterAssignment(self, ctx:grammarTraductorParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#assignment.
    def exitAssignment(self, ctx:grammarTraductorParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#return_statement.
    def enterReturn_statement(self, ctx:grammarTraductorParser.Return_statementContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#return_statement.
    def exitReturn_statement(self, ctx:grammarTraductorParser.Return_statementContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#expr.
    def enterExpr(self, ctx:grammarTraductorParser.ExprContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#expr.
    def exitExpr(self, ctx:grammarTraductorParser.ExprContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#term.
    def enterTerm(self, ctx:grammarTraductorParser.TermContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#term.
    def exitTerm(self, ctx:grammarTraductorParser.TermContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#factor.
    def enterFactor(self, ctx:grammarTraductorParser.FactorContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#factor.
    def exitFactor(self, ctx:grammarTraductorParser.FactorContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#function_call.
    def enterFunction_call(self, ctx:grammarTraductorParser.Function_callContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#function_call.
    def exitFunction_call(self, ctx:grammarTraductorParser.Function_callContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#arg_list.
    def enterArg_list(self, ctx:grammarTraductorParser.Arg_listContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#arg_list.
    def exitArg_list(self, ctx:grammarTraductorParser.Arg_listContext):
        pass



del grammarTraductorParser