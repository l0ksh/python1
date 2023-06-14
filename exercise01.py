#!/usr/bin/env python3
"""

In Python, the zip() function is used to combine two or more iterables (such as lists, tuples, or strings) into a single iterable object, returning an iterator of tuples. Each tuple contains elements from all the input iterables, corresponding to the same index position.

Basic syntax - zip(*iterables)

It's worth noting that zip() stops when the shortest input iterable is exhausted. If the input iterables are of different lengths, the resulting iterable will only contain tuples until the length of the shortest iterable.

"""
def main():
    """ Main entry point of the app """
    countries = ['India','America','United Kingdom','Russia','Spain']
    capital = ['Delhi','Washington DC','London','Moscow','Madrid']

    for f,b in zip(countries,capital):
        print(f'The capital of {f} is {b}')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
