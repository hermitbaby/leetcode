from string import Template
import xml.sax
import pprint
import re
import sys
import collections


class NestedStrReplace():

    def __init__(self):
        self.vars = {}
        self.resolved_vars = {}
        self.resolved_vars_norm = {}

    def test(self):
        d = {'who': '${tim}', 'tim': 'aaa', 'me': 'lchen'}
        self.vars = d
        print self.strReplace("give ${who} 100, and ${me} 200")
        #print Template('Give ${who} 100').substitute(d)

    def isValid(self, str):
        if '$' in str and '{' in str and '}' in str:
            stack = []
            i=0
            while i < len(str):
                if str[i] =='$' and str[i+1] == '{':
                    stack.append("${")
                    i+=2
                if str[i] == '}':
                    stack.pop()
                i+=1
            return not stack # stack.isEmpty()
        return False

    def strReplace(self, str):
        strBuffer = list(str)
        while self.isValid(strBuffer):
            start = strBuffer.index("$")
            end = strBuffer.index("}")
            key = strBuffer[start+2 : end]
            # print key
            strKey = "".join(key)
            if strKey in self.vars:
                strBuffer[start:end+1] = self.vars[strKey]
            else:
                break
            print strBuffer
        return "".join(strBuffer)

    def getResult(self):
        for k in self.vars.keys():
            resolved_value = self.strReplace(self.vars[k])
            self.resolved_vars.update({k: resolved_value})
            self.resolved_vars_norm.update({self.normalizeVarName(k): resolved_value})
            #print k + "   |   " + self.normalizeVarName(k) + "   |   " + resolved_value
        return self.resolved_vars

    def normalizeVarName(self, str):
        strBuffer = []
        for char in str:
            if re.match('[a-zA-Z0-9_]', char):
                strBuffer.append(char)
            else:
                strBuffer.append('_')
        return "".join(strBuffer)

nsr = NestedStrReplace()
nsr.test()