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
        self.resultCompound = True
    def also(self, condition):
        self.resultCompound = self.resultCompound and condition
        return condition
    def result(self):
        return self.resultCompound

def action1():
    print("action 1")

def action2():
    print("action 2")

def action3():
    print("action 3")

def main():

    accumulatorLogicalAnd = AccumulatorLogicalAnd()
    also = accumulatorLogicalAnd.also
    all = accumulatorLogicalAnd.result

    condition1 = True
    condition2 = False
    condition3 = True

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

if __name__ == '__main__':
    main()