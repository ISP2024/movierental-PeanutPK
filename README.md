## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.

## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1)
for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources)
in the assignment description.

## Rationale

2.1 what refactoring signs (code smells) suggest this refactoring?

<span style='color: #A8E6CF'>Ans.</span> Inappropriate Intimacy.

2.2 what design principle suggests this refactoring? Why?

<span style='color: #A8E6CF'>Ans.</span> Single Responsibility Principle (SRP),
because SRP wants a class to only take a responsible for itself only. Having
a `price_code` attribute which only used by Rental class means that Movie class
handles both information about price_code for itself and for Rental class
method which violates SRP.