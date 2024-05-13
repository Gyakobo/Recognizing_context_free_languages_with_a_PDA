# Language Recognition with a PDA(Pushdown Automaton)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Introduction
The following project should define a PDA that in its turn would recognize a specific context-free language.

## Let's have a look at Language A
* A, in simple terms, is a language that defines all arithmetic floating point numbers and valid operations on said decimal or whole numbers. 

* A select string of language A is of the form: 
$$
ab^kaEab^ka, 
$$
$$
k>=0
$$

* Here is an example string: $abba(1.2*(1.-2.+3.1))abba$

> Note: Language A is not a regular language, however, it's a context-free language

### Context Free Grammar for A

Language A can be defined by a 4-tuple context-free grammar $G = (V, \Sigma, R, S)$, where:

* V = {S, T, C, H, Y, N} (set of variables, or non-terminals)



<img src="assets/PDF_img.png" style="float: left; margin-bottom: 1rem;">