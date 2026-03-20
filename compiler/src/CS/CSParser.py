# Generated from /workspace/src/grammar/CS.g4 by ANTLR 4.13.2
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
        4,1,12,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,2,1,
        2,3,2,29,8,2,1,3,1,3,1,3,3,3,34,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,54,8,6,10,6,12,6,
        57,9,6,1,7,1,7,3,7,61,8,7,1,7,0,1,12,8,0,2,4,6,8,10,12,14,0,0,59,
        0,19,1,0,0,0,2,24,1,0,0,0,4,28,1,0,0,0,6,30,1,0,0,0,8,39,1,0,0,0,
        10,45,1,0,0,0,12,47,1,0,0,0,14,60,1,0,0,0,16,18,3,4,2,0,17,16,1,
        0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,
        19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,2,0,0,25,3,1,0,0,0,
        26,29,3,6,3,0,27,29,3,8,4,0,28,26,1,0,0,0,28,27,1,0,0,0,29,5,1,0,
        0,0,30,31,5,1,0,0,31,33,5,8,0,0,32,34,3,2,1,0,33,32,1,0,0,0,33,34,
        1,0,0,0,34,35,1,0,0,0,35,36,5,4,0,0,36,37,3,12,6,0,37,38,5,7,0,0,
        38,7,1,0,0,0,39,40,5,8,0,0,40,41,5,5,0,0,41,42,3,12,6,0,42,43,5,
        6,0,0,43,44,5,7,0,0,44,9,1,0,0,0,45,46,5,9,0,0,46,11,1,0,0,0,47,
        48,6,6,-1,0,48,49,3,14,7,0,49,55,1,0,0,0,50,51,10,2,0,0,51,52,5,
        3,0,0,52,54,3,14,7,0,53,50,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,
        56,1,0,0,0,56,13,1,0,0,0,57,55,1,0,0,0,58,61,3,10,5,0,59,61,5,8,
        0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,15,1,0,0,0,5,19,28,33,55,60
    ]

class CSParser ( Parser ):

    grammarFileName = "CS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'const'", "'int'", "'+'", "'='", "'('", 
                     "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "CONST", "INT", "PLUS", "ASSIGN", "LRB", 
                      "RRB", "SEMICOLON", "ID", "INT_LIT", "SINGLE_COMMENT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_type_system = 1
    RULE_statement = 2
    RULE_const_stmt = 3
    RULE_call_stmt = 4
    RULE_literal = 5
    RULE_expression = 6
    RULE_expression1 = 7

    ruleNames =  [ "program", "type_system", "statement", "const_stmt", 
                   "call_stmt", "literal", "expression", "expression1" ]

    EOF = Token.EOF
    CONST=1
    INT=2
    PLUS=3
    ASSIGN=4
    LRB=5
    RRB=6
    SEMICOLON=7
    ID=8
    INT_LIT=9
    SINGLE_COMMENT=10
    WS=11
    ERROR_CHAR=12

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

        def EOF(self):
            return self.getToken(CSParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==8:
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(CSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_systemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSParser.INT, 0)

        def getRuleIndex(self):
            return CSParser.RULE_type_system

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_system" ):
                return visitor.visitType_system(self)
            else:
                return visitor.visitChildren(self)




    def type_system(self):

        localctx = CSParser.Type_systemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type_system)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(CSParser.INT)
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

        def const_stmt(self):
            return self.getTypedRuleContext(CSParser.Const_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(CSParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.const_stmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.call_stmt()
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


    class Const_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSParser.CONST, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSParser.SEMICOLON, 0)

        def type_system(self):
            return self.getTypedRuleContext(CSParser.Type_systemContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_const_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_stmt" ):
                return visitor.visitConst_stmt(self)
            else:
                return visitor.visitChildren(self)




    def const_stmt(self):

        localctx = CSParser.Const_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CSParser.CONST)
            self.state = 31
            self.match(CSParser.ID)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 32
                self.type_system()


            self.state = 35
            self.match(CSParser.ASSIGN)
            self.state = 36
            self.expression(0)
            self.state = 37
            self.match(CSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def LRB(self):
            return self.getToken(CSParser.LRB, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def RRB(self):
            return self.getToken(CSParser.RRB, 0)

        def SEMICOLON(self):
            return self.getToken(CSParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = CSParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CSParser.ID)
            self.state = 40
            self.match(CSParser.LRB)
            self.state = 41
            self.expression(0)
            self.state = 42
            self.match(CSParser.RRB)
            self.state = 43
            self.match(CSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSParser.INT_LIT, 0)

        def getRuleIndex(self):
            return CSParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(CSParser.INT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(CSParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(CSParser.PLUS, 0)

        def getRuleIndex(self):
            return CSParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.expression1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 50
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 51
                    self.match(CSParser.PLUS)
                    self.state = 52
                    self.expression1() 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CSParser.LiteralContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = CSParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression1)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.literal()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(CSParser.ID)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




