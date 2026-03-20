# Generated from /workspace/src/grammar/CS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSParser import CSParser
else:
    from CSParser import CSParser

# This class defines a complete generic visitor for a parse tree produced by CSParser.

class CSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSParser#program.
    def visitProgram(self, ctx:CSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#type_system.
    def visitType_system(self, ctx:CSParser.Type_systemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#statement.
    def visitStatement(self, ctx:CSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#const_stmt.
    def visitConst_stmt(self, ctx:CSParser.Const_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#call_stmt.
    def visitCall_stmt(self, ctx:CSParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#literal.
    def visitLiteral(self, ctx:CSParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression.
    def visitExpression(self, ctx:CSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression1.
    def visitExpression1(self, ctx:CSParser.Expression1Context):
        return self.visitChildren(ctx)



del CSParser