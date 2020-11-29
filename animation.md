---
layout: default
title: Tom TKG's Homepage
use_math: true
---

## GIF Animation
### Ackley function:
$$
\begin{aligned}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{aligned}
$$
<a href="animation/AckleyGA.gif"><img src="animation/AckleyGA.gif"></a><a href="animation/AckleyEP.gif"><img src="animation/AckleyEP.gif"></a><a href="animation/AckleyPBIL.gif"><img src="animation/AckleyPBIL.gif"></a>

<a href="animation/AckleyDE.gif"><img src="animation/AckleyDE.gif"></a><a href="animation/AckleyPSO.gif"><img src="animation/AckleyPSO.gif"></a><a href="animation/AckleyAS.gif"><img src="animation/AckleyAS.gif"></a>

## Javascript Animation
### Weight Vector Generation Method
You can change the weight vector size in the animation
* [Simplex-lattice design](animation/SLD.html){:target="_blank"}
* [Incremental lattice design](animation/ILD.html){:target="_blank"}
* [Riesz 𝑠-energy](animation/Energy.html){:target="_blank"}
* Hammersley method

### Weight Vector Change Method
You can change the weight vector distribution in the animation
* [Change method 1](animation/Change1.html){:target="_blank"}
* [Change method 2](animation/Change2.html){:target="_blank"}
* [Change method 3](animation/Change3.html){:target="_blank"}
* [Change method 4](animation/Change4.html){:target="_blank"}
* Normalized change method 1 (This distribution does not change)
* [Normalized change method 2](animation/NChange2.html){:target="_blank"}
* [Normalized change method 3](animation/NChange3.html){:target="_blank"}
* [Normalized change method 4](animation/NChange4.html){:target="_blank"}

## Reference 
Dan Simon, Evolutionary Optimization Algorithms: Biologically-Inspired and Population-Based Approaches to Computer Intelligence, John Wiley & Sons, 2013.
[https://academic.csuohio.edu/simond/EvolutionaryOptimization](https://academic.csuohio.edu/simond/EvolutionaryOptimization)  