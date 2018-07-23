# 8-Queen-Hill-Climbing---Thilan

My program uses a hill climbing approach to solve the 8-Queen Problem.

The program chooses the next best move randomly from a list of best moves. In this way, local or global maximum can be achieved depending on the path the program takes.

I have included two versions of my program.

The first version is the basic program which gets stuck at local maximums, or reaches the global maximum depending on its path.

In the second version, the program has been slightly edited, such that it always reaches a global maximum. It does this by reinitializing the board to its initial queen positions, if the result lands at a local maximum. The program loops until the path reaches a global maximum, which provides the solution that we are expecting. In this way, the final solution provided will always be a global maximum.

I have included the results from the console for the two versions of the code.


