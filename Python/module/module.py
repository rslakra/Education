#
# Author: Rohtash Lakra
#

# Reloading a Module
# For reasons of efficiency, a module is only loaded once per interpreter session.
# That is fine for function and class definitions, which typically make up the bulk of a module’s contents.
# But a module can contain executable statements as well, usually for initialization.
# Be aware that these statements will only be executed the first time a module is imported.
# If you make a change to a module and need to reload it, you need to either restart the interpreter or use a function
# called ```reload()``` from module importlib:


# Modules are often designed with the capability to run as a standalone script for purposes of testing the
# functionality that is contained within the module. This is referred to as unit testing.
# For example, suppose you have created a module ```module.py``` containing a factorial function, as follows:
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
# However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.
# Using this fact, you can discern which is the case at run-time and alter behavior accordingly:
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))

# But it can also be run as a standalone by passing an integer argument on the command-line for testing:
# python module.py 6


# In summary, __all__ is used by both packages and modules to control what is imported when import * is specified.
# But the default behavior differs:
# For a package, when ```__all__``` is not defined, import * does not import anything.
# For a module, when ```__all__``` is not defined, import * imports everything (except—you guessed it—names starting with an underscore).


# Subpackages
# Packages can contain nested subpackages to arbitrary depth.
# In addition, a module in one subpackage can reference objects in a sibling subpackage (in the event that the sibling
# contains some functionality that you need).
# Or you can use a relative import, where '..' refers to the package one level up.
# .. evaluates to the parent package (pkg), and
# ..sub_pkg1 evaluates to subpackage sub_pkg1 of the parent package.




