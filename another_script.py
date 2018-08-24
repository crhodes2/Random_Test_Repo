# !/usr/bin/env python3
# -*- mode: python -*-
###############################################################
'''
                         About program

'''
####################### List of modules #######################

import script                  # importing a script
from script import outside     # importing a script variable

#######################    Variables    #######################

''' none at the moment '''

#######################    Functions    #######################

def a_new_function(par):
    print('a new function with an {0} variable'. format(par))

def main():
    function = script.function()
    inside = "inside"

    print(function)
    print(a_new_function(inside))       # calling a function with a local variable
    print(a_new_function(outside))      # calling a function with an outside variable from another script



#######################       Main      #######################

if __name__ == "__main__":
    main()