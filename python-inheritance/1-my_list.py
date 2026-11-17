#!/usr/bin/python3
"""Module that defines the class MyList, a list that can print sorted."""


class MyList(list):
    """Class that inherits from list and can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
