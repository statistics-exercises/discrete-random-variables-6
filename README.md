# Plotting Binomial random variables

Now that you know how to generate binomial random variables lets make a scatter plot showing 100 random variables that are sampled from this distribution.

To complete this exercise you will need to:

- Write a function called `binomial` that takes `n` (the number of trials to perform) and `p` (the probability of success) as arguments using what you learned in the previous exercise.

- Use this function and what you know about loops and lists to generate a list called `random_variables` that contains 100 binomial random variables all of which have the n parameter set equal to the global variable `num` and the p parameter set to the global variable `prob`.

I have included code in the cell on the left that will plot your list of random variables.  To get this code to work, however, you will need to write a second list called `indices` that contains a numerical index for each of these random variables.  The first of these indices should be equal to one, the second should be equal to two, the third should be three and so on.  
