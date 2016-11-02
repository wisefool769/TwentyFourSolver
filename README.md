# TwentyFourSolver

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/wisefool769/twentyfoursolver)


Suppose we have $s = (x_1, x_2, x_3, ... x_n)$ with $x_i \in \mathcal{N}$

Every possible number expressible with these and the 4 basic operations (subtraction, addition, multiplication, and division) can be expressed as follows:  

    Pick a number without replacement, call it a.  
    
    While s is not empty:  
    
        Pick a number without replacement, call it b.  
        
        Pick an operation, call it #  
        
        Choose one of a # b and b # a. Call the result a  
        
    Return a
    
Click the pink button above to use the solver. Click demo.ipynb. You can edit the input numbers and click the play button at top.
