from vsc.model.expr_literal_model import ExprLiteralModel

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.



'''
Created on Jul 28, 2019

@author: ballance
'''
from vsc.model.expr_model import ExprModel

class ExprPartselectModel(ExprModel):
    
    def __init__(self, lhs, upper, lower=None):
        self.lhs = lhs
        self.upper = upper 
        self.lower = lower 
    
    def build(self, btor):
        upper = self.upper
        lower = self.lower if self.lower is not None else self.upper 
        return btor.Slice(
            self.lhs.build(btor),
            lower.val(), 
            upper.val())
        
    def width(self):
        upper = self.upper
        lower = self.lower if self.lower is not None else self.upper 
        return (upper.val() - lower.val()) + 1
    
    def is_signed(self):
        return False
    
    def accept(self, visitor):
        visitor.visit_expr_partselect(self)
    
