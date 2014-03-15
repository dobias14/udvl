
class Formula:
    def __init__(self, subformulas):
        self.subforms = subformulas
    
    def toString(self):
        pass
    
    def eval(self, i):
        pass
    
    def subf(self):
        return self.subforms
    
class Variable(Formula):
    def __init__(self, m_name):
        Formula.__init__(self, [])
        self.m_name = m_name
    
    def toString(self):
        return self.m_name
    
    def eval(self, i):
        return i[self.m_name]
    
    def subf(self):
        return []
    
    def name(self):
        return self.m_name
    

class Negation(Formula):
    def __init__(self, orig):
        Formula.__init__(self, [orig])
    
    def toString(self):
        return "-" + self.originalFormula().toString()
    
    def originalFormula(self):
        return self.subf()[0]
    
    def eval(self, i):
        return not self.originalFormula().eval(i)
    
    
class Conjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, subformulas)

## Problem s tymto je ten, ze mi dava & aj vedla negacie
##     Spravne (a&-b) ZLE (a&-&b)
##
##    def toString(self):
##        z = "("
##        s=""
##        k="}"
##        for f in self.subf():
##            s += f.toString()
##        z += "&".join(s) + k
##        return z
    
    def toString(self):
        s = "("
        for x in self.subf():
            s += x.toString()
            s += "&"
        return s[0:-1] + ")"
    
    def eval(self, i):
        for x in self.subf():
            if not x.eval(i):
                return False
        return True


class Disjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, subformulas)
        
    def toString(self):
        s = "("
        for x in self.subf():
            s += x.toString()
            s += "|"
        return s[0:-1] + ")"

    def eval(self , i):
        for x in self.subf():
            if x.eval(i):
                return True
        return False
    
    
class Implication(Formula):
    def __init__(self, left, right):
        Formula.__init__(self, [left, right])
        
    def left(self):
        return self.subf()[0]

    def right(self):
        return self.subf()[1]
        
    def toString(self):
        return "(" + self.left().toString() + "=>" + self.right().toString() + ")"
    
    def eval(self, i):
        return (not self.left().eval(i)) or (self.right().eval(i))
    

class Equivalence(Formula):
    def __init__(self, left, right):
        Formula.__init__(self, [left, right])

    def left(self):
        return self.subf()[0]

    def right(self):
        return self.subf()[1]
    
    def toString(self):
        return "(" + self.left().toString() + "<=>" + self.right().toString() + ")"
    
    def eval(self, i):
        return (self.left().eval(i) == self.right().eval(i))
    
