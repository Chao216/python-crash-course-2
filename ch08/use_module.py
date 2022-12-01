#import the whole module

import module_example

module_example.greeting("Chao Jiang")
module_example.format_name("valadimir", 'PUTIN')

# import specific function

from module_example import greeting

greeting("Apurva Potdar")

from module_example import format_name

format_name("LARRY", 'page')

# use as to alias a module

import module_example as handy

handy.greeting("Jiang Zemin")
handy.format_name("david", "TAO")

# import all functions from a module

from module_example import *

greeting("Donald trump")
format_name("BERLINER", "PLATZ")
