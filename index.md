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

## Updates

* *The class and its waitlist are completely full.* Please check back later in
the semester to see if enrollment will have become available. Visitors are permitted
to audit only if there is enough space in the room. Please do leave available
seats to enrolled students.

## Assingments 

Assignments will be posted on
[Piazza](https://piazza.com/berkeley/spring2018/ee227c/home). If you haven't
already, [sign up here](https://piazza.com/berkeley/spring2018/ee227c).
Homeworks will be assigned roughly every two weeks, and 2--3 problems will be selected for grading (we will not tell you which ones in advance). Assignments should be submitted through [GradeScope](https://gradescope.com); the course is listed as EE227C, which you may join with entry code 9P5NDV. *All homeworks should be latexed.* Students will be permitted two unexcused late assignments (up to a week late). Students requesting additional extensions should email Max.

## Grading

Grading policy: 50% homeworks, 10% scribing, 20% midterm exam, 20% final exam. 


## Course notes

Course notes will be publicly available. Participants will
collaboratively create and maintain notes over the course of the semester
using git. See [this
repository](https://github.com/ee227c/ee227c.github.io/tree/master/notes) for
source files. Most lectures will have an accompanying Jupyter notebook
containing plots and illustrative examples.

### [Sign up for scribing here](https://docs.google.com/spreadsheets/d/1OSW_Yznt80k40Zmf6MVRvz3wT-An0XFbNkEEWNbEjNE/edit?usp=sharing)

All three scribes should collaborate to prove a *single* tex file. Moritz will have a skeleton of notes available [here](https://github.com/ee227c/ee227c.github.io/tree/master/notes), which students will fill in, following [these instructions](https://github.com/ee227c/ee227c.github.io/blob/master/notes/instructions.pdf). 

We suggest that each scribe takes down notes, and then all three meet after class to consolidate. 

### [All available lecture notes (pdf)](notes/ee227c-notes.pdf)

See individual lectures below.

## Schedule


| # | Date  | Topic  | pdf | ipynb  |
|-|-|-|-|-|
| 1 | 1/16 | Convexity  | [pdf](notes/ee227c-lecture1.pdf) | [ipynb](http://nbviewer.jupyter.org/urls/ee227c.github.io/notes/lecture1.ipynb)
| 2 | 1/18 | Gradient method (non-smooth and smooth) | [pdf](notes/ee227c-lecture2.pdf)  | ---  |
| 3 | 1/23 | Gradient method (strongly convex) |   |   |
| 4 | 1/25 | Gradient method (some applications) | ---  | [ipynb](code/lecture4.html)  |
| 5 | 1/30 | Conditional gradient (Frank-Wolfe algorithm) |   |   |
| 6 | 2/1 |  Momentum and acceleration|   |   |
| 7 | 2/6 |Nesterov's method  |   |   |
| 8 | 2/8 |  Lower bounds|   |   |
| 9 | 2/13 |  Robustness acceleration trade-offs |   |   |
| 10 | 2/15 | Stochastc optimization |   |   |
| 11 | 2/20 | Learning, regularization, and generalization |   |   |
| 12 | 2/22 | Coordinate Descent |   |   |
| 13 | 2/27 | Proximal Methods  |   |   |
| 14 | 3/1 | Duality theory|   |   |
| 15 | 3/6 | Algorithms using duality |   |   |
| 18 | 3/8 | Distributed Optimization |   |   |
| 16 | 3/13 | Backpropagation and adjoints |   |   |
| 17 | 3/15 | Some implementation aspects |   |   |
| 19 | 3/20 | Quasi-convex problems |   |   |
| 20 | 3/22 | Alternating minimization |   |   |
| -- | 3/27 | No class (Spring break) |   |   |
| -- | 3/29 | No class (Spring break) |   |   |
| 21 | 4/3  | Guest lecture by Ludwig Schmidt on non-convex constraints | | |
| 22 | 4/5  | Guest lecture by Ludwig Schmidt on non-convex constraints | | |
| 23 | 4/10 | Newton method |   |   |
| 24 | 4/12 | Ellipsoid method |   |   |
| 25 | 4/17 | Sampling from convex sets |   |   |
| 25 | 4/19 | TBD |   |   |
| 26 | 4/24 | Sum of squares |   |   |
| 27 | 4/26 | Last lecture |   |   |
| 28 | 5/1 | Reading, review, recitation |   |   |
| 29 | 5/3 | Reading, review, recitation |   |   |

## Background

The prerequisites are previous coursework in linear algebra, multivariate
calculus, probability and statistics. 
Coursework or background in optimization theory as covered in
EE227BT is highly recommended.  The class will involve some basic programming.
Students are encouraged to use either [Julia](https://julialang.org) or Python.
We discourage the use of MATLAB.

## Material

### Textbooks

* Numerical Optimization. J. Nocedal and S. J. Wright, Springer Series in Operations Research, Springer-Verlag, New York, 2006 (2nd edition).
* Convex Optimization. S. Boyd and L. Vandenberghe. Cambridge University Press,
Cambridge, 2003. [PDF available here](http://www.stanford.edu/~boyd/cvxbook/)
* Introductory Lectures on Convex Optimization: A Basic Course. Y. Nesterov. Kluwer, 2004.
* Convex Optimization: Algorithms and Complexity. S. Bubeck. [PDF available here](https://arxiv.org/abs/1405.4980)
* Nonlinear Programming D. P. Bertsekas. Athena Scientific, Belmont, Massachusetts. (2nd edition). 1999. 
*  Participants will furthermore have access to a yet unpublished optimization text
called *Nonlinear Optimization for Machine Learning: New Shit Has Come to
Light*.

### Lecture notes

* Efficient Methods in Convex Programming. A. Nemirovski. Lecture Notes as
[PDF available here](http://www2.isye.gatech.edu/~nemirovs/Lect_EMCO.pdf).

### Blog posts

* [The Zen of Gradient Descent](http://blog.mrtz.org/2013/09/07/the-zen-of-gradient-descent.html) Moritz Hardt
* [Why Momentum Really Works](https://distill.pub/2017/momentum/) Gabriel Goh.
* [Robustness versus Acceleration](http://blog.mrtz.org/2014/08/18/robustness-versus-acceleration.html) Moritz Hardt
