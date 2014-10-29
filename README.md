This is a collection of Python scripts to generate cellular automata
(currently, this only generates 2D automata following Conway's Game of Life rules)

Depends on numpy and matplotlib (pcolor) to generate graphics

(Developed on numpy 1.8.0, and matplotlib 1.3.0)

CellularAutomata.py contains the CellularAutomata2D object which holds the automaton
and the rules by which it evolves

GameOfLifePatterns.py contains a set of basic patterns to add to the automaton for
Game Of Life

playGameOfLife.py is a run script to generate automata

