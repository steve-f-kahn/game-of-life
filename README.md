# Conway's Game of Life

## Introduction

Conway's game of life, also known by Life is a zero player game. How the game progresses is determined by its initial state. 

## Game Rules

1. Any cell with fewer then 2 live neighbours dies
2. Any cell with two or three neighbours lives on to the next generation
3. Any cell that has more then 3 neighbours dies
4. Any dead cell that has exactly 3 neighbours becomes a live cell

A neighbour is a cell that is next to a cell either horizontally, diagonally or vertically

## User Storues
```
As a person
So that I can have a big board
I'd like to adjust the size of the board
```
```
As a person
So I can find new patterns
I'd like to be able to randomly generate a board state
```
```
As a person
So I can change how cluttered the board is 
I'd like to change the chance of life in the randomly generated board
```
```
As a person
So I can investigate a specific pattern 
I'd like to be able to set an initial board state
```
```
As a live cell
So I can represent underpopulation
I'd like to die if I have fewer then 2 neighbours
```
```
As a live cell
So I can represent stable population
I'd like to stay the same if I have 2 or 3 neighbours
```
```
As a live cell
So I can represent overpopulation
I'd like to die if I have more then 3 neighbours
```
```
As a dead cell
So I can represent reproduction
I'd like to be a live cell if I have 3 live neighbours
```