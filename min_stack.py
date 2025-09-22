def __init__(self):
        self.stack=[]
        self.Minstack=[]
def push(self, val):
        self.stack.append(val)
        if (len(self.Minstack)==0 or val<=self.Minstack[-1]):
             self.Minstack.append(val)
def pop(self):
        if len (self.stack)==0:
            return 'st is empty'
        else:
            topel = self.stack.pop()
        if topel == self.Minstack[-1]:
            return self.Minstack.pop()       
def top(self):
        if len(self.stack)!=0:
            return self.stack[-1]
def getMin(self):
        return self.Minstack[-1]