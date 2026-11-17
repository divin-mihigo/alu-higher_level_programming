#!/usr/bin/python3
"""Module that defines a function checking the inheritance of an object."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An object that is exactly an instance of a_class returns False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
