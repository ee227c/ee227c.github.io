---
layout: default
---

# EE 227C (Spring 2018)<br /> Convex Optimization and Approximation

University of California, Berkeley  

Time: **TuTh 12:30PM - 1:59PM**, Location: **Etcheverry 3106**  
Instructor: [Moritz Hardt](http://mrtz.org) (Email: hardt+ee227c@berk...edu)   
Graduate Instructor: [Max Simchowitz](https://people.eecs.berkeley.edu/~msimchow/index.html) (Email: msimchow@berk...edu).  
Office hours: Max on Mon 3-4pm, Soda 310 (starting 1/29), Moritz on Fri 9--9:50a, SDH 722 

## Summary

This course will explore theory and algorithms for nonlinear optimization. We
will focus on problems that arise in machine learning and modern data analysis,
paying attention to concerns about complexity, robustness, and implementation in
these domains. We will also see how tools from convex optimization can help
tackle non-convex optimization problems common in practice.


## Course notes

Course notes will be publicly available. Participants will
collaboratively create and maintain notes over the course of the semester
using git. See [this
repository](https://github.com/ee227c/ee227c.github.io/tree/master/notes) for
source files. 

### [All available lecture notes (pdf)](notes/ee227c-notes.pdf)

See individual lectures below. These notes likely contain several mistakes. If
you spot any please send an email or pull request.

## Schedule


| # | Date  | Topic  | pdf | ipynb  |
|-|-|-|-|-|
| | | **Part I: Basic gradient methods** | | |
| 1 | 1/16 | Convexity  | [pdf](notes/ee227c-lecture1.pdf) | [ipynb](http://nbviewer.jupyter.org/urls/ee227c.github.io/notes/lecture1.ipynb)
| 2 | 1/18 | Gradient method (non-smooth and smooth) | [pdf](notes/ee227c-lecture2.pdf)  | ---  |
| 3 | 1/23 | Gradient method (strongly convex) | [pdf](notes/ee227c-lecture3.pdf)  | --- |
| 4 | 1/25 | Some applications of gradient methods | [pdf](notes/ee227c-lecture4.pdf)  | [ipynb](code/lecture4.html)  |
| 5 | 1/30 | Conditional gradient (Frank-Wolfe algorithm) | [pdf](notes/ee227c-lecture5.pdf)  | [ipynb](code/lecture5.html)  |
| | | **Part II: Krylov methods and acceleration** | | |
| 6 | 2/1 |  Discovering acceleration with Chebyshev polynomials | [pdf](notes/ee227c-lecture6.pdf)  | [ipynb](code/lecture6.html)  |
| 7 | 2/6 | Nesterov's accelerated gradient descent  | [pdf](notes/ee227c-lecture7.pdf)  | ---  |
| 8 | 2/8 | Eigenvalue intermezzo | [pdf](notes/ee227c-lecture8.pdf)  | ---  |
| 9 | 2/13 | Lower bounds, robustness vs acceleration | [pdf](notes/ee227c-lecture9.pdf)  | [py](code/lecture9.py) |
| | | **Part III: Stochastic optimization** | | |
| 10 | 2/15 | Stochastc optimization | [pdf](notes/ee227c-lecture10.pdf)  | ---  |
| 11 | 2/20 | Learning, regularization, and generalization | [pdf](notes/ee227c-lecture11.pdf)   | ---  |
| 12 | 2/22 | Coordinate Descent (guest lecture by Max Simchowitz) | [pdf](notes/ee227c-lecture12.pdf)  | ---  |
| | | **Part IV: Dual methods** | | |
| 13 | 2/27 | Duality theory  | [pdf](notes/ee227c-lecture13.pdf) | --- |
| 14 | 3/1 | Dual decomposition, method of multipliers | [pdf](notes/ee227c-lecture14.pdf) | ---  |
| 15 | 3/6 | Stochastic Dual Coordinate Ascent | [pdf](notes/ee227c-lecture15.pdf)  | ---  |
| 16 | 3/8 | Backpropagation and adjoints | [pdf](notes/ee227c-lecture16.pdf) | --- |
| | | **Part V: Non-convex problems** | | |
| 17 | 3/13 | Non-convex problems | [pdf](notes/ee227c-lecture17.pdf)  | ---  |
| 18 | 3/15 | Saddle points | [pdf](notes/ee227c-lecture18.pdf)  |   |
| 19 | 3/20 | Alternating minimization and expectaction maximization | ---  | [ipynb](code/lecture19.html) |
| 20 | 3/22 | Derivative-free optimization, policy gradient, controls | --- | [ipynb](code/lecture20.html) |
| 21 | 4/3  | Non-convex constraints I (guest lecture by Ludwig Schmidt) | [pdf](notes/ee227c-lecture21.pdf) | |
| 22 | 4/5  | Non-convex constraints II (guest lecture by Ludwig Schmidt) | | [ipynb](code/lecture22.html) |
| | | **Part VI: Higher-order and interior point methods** | | |
| 23 | 4/10 | Newton's method | [pdf](notes/ee227c-lecture23.pdf)  | --- |
| 24 | 4/12 | Experimenting with second-order methods | ---  | [ipynb](code/lecture24.html)  |
| 25 | 4/17 | Enter interior point methods | [pdf](notes/ee227c-lecture25.pdf) | ---  |
| 26 | 4/19 | Primal-dual interior point methods |   |   |
| 27 | 4/24 | Ellipsoid method |   |   |
| 28 | 4/26 | Submodular functions, Lovasz extension |   |   |
| 29 | 5/1 | Reading, review, recitation |   |   |
| 30 | 5/3 | Reading, review, recitation |   |   |

### [Sign up for scribing here](https://docs.google.com/spreadsheets/d/1OSW_Yznt80k40Zmf6MVRvz3wT-An0XFbNkEEWNbEjNE/edit?usp=sharing)

All three scribes should collaborate to provide a *single* tex file as seen
[here](https://github.com/ee227c/ee227c.github.io/tree/master/notes).
Students are required to closely follow [these instructions](https://github.com/ee227c/ee227c.github.io/blob/master/notes/instructions.pdf). 

We suggest that each scribe takes down notes, and then all three meet after class to consolidate. 

## Assignments 

Assignments will be posted on
[Piazza](https://piazza.com/berkeley/spring2018/ee227c/home). If you haven't
already, [sign up here](https://piazza.com/berkeley/spring2018/ee227c).
Homeworks will be assigned roughly every two weeks, and 2--3 problems will be selected for grading (we will not tell you which ones in advance). Assignments should be submitted through [GradeScope](https://gradescope.com); the course is listed as EE227C, which you may join with entry code 9P5NDV. *All homeworks should be latexed.* Students will be permitted two unexcused late assignments (up to a week late). Students requesting additional extensions should email Max.

## Grading

Grading policy: 50% homeworks, 10% scribing, 20% midterm exam, 20% final exam. 



## Background

The prerequisites are previous coursework in linear algebra, multivariate
calculus, probability and statistics.  Coursework or background in optimization
theory as covered in EE227BT is highly recommended.  The class will involve some
basic programming.  Students are encouraged to use either
[Julia](https://julialang.org) or Python.  We discourage the use of MATLAB.

## Material

* Nonlinear Programming (3rd edition). D. Bertsekas, Athena Scientific.
* Numerical Optimization. J. Nocedal and S. J. Wright, Springer Series in Operations Research, Springer-Verlag, New York, 2006 (2nd edition).
* Convex Optimization. S. Boyd and L. Vandenberghe. Cambridge University Press,
Cambridge, 2003. [PDF available here](http://www.stanford.edu/~boyd/cvxbook/)
* Introductory Lectures on Convex Optimization: A Basic Course. Y. Nesterov. Kluwer, 2004.
* Convex Optimization: Algorithms and Complexity. S. Bubeck. [PDF available here](https://arxiv.org/abs/1405.4980)
* Nonlinear Programming D. P. Bertsekas. Athena Scientific, Belmont, Massachusetts. (2nd edition). 1999. 
* Efficient Methods in Convex Programming. A. Nemirovski. Lecture Notes as
[PDF available here](http://www2.isye.gatech.edu/~nemirovs/Lect_EMCO.pdf).

