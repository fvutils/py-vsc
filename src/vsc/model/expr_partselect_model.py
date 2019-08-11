'''
Created on Jul 28, 2019

@author: ballance
'''
from vsc.model.expr_model import ExprModel

class ExprPartselectModel(ExprModel):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs 
        self.rhs = rhs 
        pass
    
    def accept(self, visitor):
        visitor.visit_expr_partselect(self)
    