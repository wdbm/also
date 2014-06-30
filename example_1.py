################################################################################
#                                                                              #
# also                                                                         #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is an implementation of the branch logic "if also" in Python.   #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

class AccumulatorLogicalAnd(object):
    def __init__(self):
        self.attribute_all = True
        self.attribute_any = False
        self.attribute_none = None
        self.attribute_numberTotal = 0
        self.attribute_numberPassed = 0
        self.attribute_numberFailed = 0
    def also(self, condition):
        self.attribute_all = self.attribute_all and condition
        self.attribute_any = self.attribute_any or condition
        self.attribute_none = not condition and (self.attribute_none is None or self.attribute_none)
        self.attribute_numberTotal += 1
        if condition:
            self.attribute_numberPassed += 1
        else:
            self.attribute_numberFailed += 1
        return condition
    def all(self):
        return self.attribute_all
    def any(self):
        return self.attribute_any
    def none(self):
        return self.attribute_none
    def total(self):
        return self.attribute_numberTotal
    def passed(self):
        return self.attribute_numberPassed
    def failed(self):
        return self.attribute_numberFailed

def action1():
    print("action 1")

def action2():
    print("action 2")

def action3():
    print("action 3")

def main():

    accumulatorLogicalAnd = AccumulatorLogicalAnd()
    also = accumulatorLogicalAnd.also
    all = accumulatorLogicalAnd.all
    any = accumulatorLogicalAnd.any
    none = accumulatorLogicalAnd.none
    total = accumulatorLogicalAnd.total
    passed = accumulatorLogicalAnd.passed
    failed = accumulatorLogicalAnd.failed

    condition1 = True
    condition2 = False
    condition3 = True

    print

    if also(condition1):
        action1()
    if also(condition2):
        action2()
    if also(condition3):
        action3()
    if all():
        print("all conditions passed")
    else:
        print("some conditions failed")

    print
    print("Did all pass?\t\t{result}".format(result = str(all())))
    print("Did any pass?\t\t{result}".format(result = str(any())))
    print("Did none pass?\t\t{result}".format(result = str(none())))
    print("How many in total?\t{result}".format(result = str(total())))
    print("How many passed?\t{result}".format(result = str(passed())))
    print("How many failed?\t{result}".format(result = str(failed())))
    print

if __name__ == '__main__':
    main()