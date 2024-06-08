---
layout: post
title: "purely-functional"
---

I was initially introduced to "functional programming languages" as Lisp, because in Lisp, functions could be defined at almost any location in a program and passed as values (known as first-class functions). However, I was later told that Lisp was not truly "functional," as Lisp functions were not "pure."

A "pure function" is one that behaves like a mathematical function, giving the same output for the same input. Then you realize that almost all functions in most programming languages, including random number functions (random), are not pure. Although the input is always the same (no parameters), the output is different each time. They told me that impure functions are error-prone and cannot be verified for correctness.

In my fear of using an impure, unsafe language, I began to explore Haskell, a language touted as "purely functional" and safe. I firmly believed that Haskell's functional purity dogma had been in place for years, and I scoffed at the "side effects" (side-effects) in other languages. I believed that the universe was pure, and mathematics was the ultimate language of the universe, so programming languages should be pure as well...

Have you noticed that all cult leaders initially used people's fear psychology to make them blindly believe they had found a savior? It was a shocking realization when I hit a wall multiple times and suddenly woke up to the fact that Haskell was just such a cult :p Every religion has a mysterious symbol representing its spirit. Haskell's is as follows:

When a beginner enters the IRC chat room of Haskell, the veterans will be extremely patient in answering his questions. They tell him that the Haskell community is the friendliest, most secular, and most scientific and rational community. However, the longer you stay, you find out it's not that way. They are friendly only if you don't point out Haskell's fatal flaws. If you know about these flaws and want to discuss them, you will find everything changed. They will say, you don't understand! We are scientists! If you don't acknowledge this, we will kill you!:p

The Haskell community likes to omit the "pure" character in their concepts and call Haskell a "functional language." They like to "correct" others' concepts. They tell people that "impure" functional languages are not worthy of being called "functional languages." Under their definition, even an old-school functional language like Lisp is not qualified to be called a "functional language." However, after reading this article, you will find out that their definition is narrow and incorrect.

In Haskell, you cannot use common assignment statements like x:=1 in Pascal, x=1 in C and Java, or (set! x 1) in Scheme, and (setq x 1) in Common Lisp. Consequently, you cannot keep "state" (state) - things like random number seeds, which are essentially "global variables." For instance, in C language, you can define the random() function like this:

int random() {
// code for generating random numbers using a seed
}

However, in Haskell, you cannot define a function like random() with such a state. Instead, you have to use a different approach to generate random numbers, such as using a library function or monadic bind. I. `static int seed = 0;` // A static variable, essentially a global variable, accessible only by the random function.
II. `seed = next_random(seed);` // Generates next random number and updates seed.
III. `return seed;` // Returns the updated seed.

In Haskell, things are quite different. Since Haskell cannot retain state, the same "variable" in its scope always holds the same value. A function always yields the same output given the same input. Therefore, it's not straightforward to express a function like random that returns different outputs each time in Haskell. To make random produce different outputs, you must provide it with "different inputs". But how can you provide it with different inputs? Haskell's approach is to make the "seed" an input and return two values: the new random number and the new seed. Then, find a way to pass this new seed to the next random call. So, Haskell's random's "flow" looks like this:

[RandomNumber, NewSeed] = random (OldSeed) I. (Old seed) --> (New random number, new seed)

Now comes the problem. The new seed obtained must be accurately and error-free transmitted to the next place that uses random(), otherwise you won't be able to generate the next random number. Since there's no place to "store" this seed, you often need to let the seed "pass through" a series of functions to reach its destination. All functions on the "path" must add a parameter (old seed) and return a value (new seed). This is like threading a pipe through this function, with both ends open, allowing the seed to pass through unhindered.

To achieve the goal of "pure functions," we need to do a lot of "plumbing" work, increasing the complexity and workload of the program. If we could store the seed in a global variable and fetch it when needed, we wouldn't have to pass it back and forth. Everything except random() would be oblivious to the seed's existence.

To alleviate visual burden and maintain these coming-and-going "states," Haskell introduced a concept called monads. Its essence is to hide these extra parameters and returns in the type system. This is like stuffing chaotic wires into a junction box, making the surface look cleaner but the underlying complexity still inescapable. Sometimes I'm puzzled, why are things that are easy in other languages a "research problem" in Haskell? Often it's the monad that's causing the trouble. Especially when you have multiple "states," you need to use things like monad transformers. Monad transformers, in essence, are an ugly hack. They don't fundamentally solve the problem but can make your head spin trying to write code around them. Some people think using monads and monad transformers makes them look smart, but in reality, it's just them struggling to get past their own limitations.

When talking about monads, I like to use this analogy:

(Old seed) ----> (New random number, new seed)

Imagine a pipeline where the old seed goes in one end and a new random number and new seed come out the other end. The functions in the pipeline are like filters that take the old seed, process it, and pass it on to the next filter. Each filter takes the old seed as an input and returns a new random number and new seed as output. The pipeline ensures that the new seed is accurately and error-free transmitted from one function to the next, allowing the generation of a new random number each time. This pipeline design abstracts away the details of seed handling, making the code easier to read and maintain. In a world using a "functional programming language" with monads, living is like being in a world without electromagnetic waves.

In this world, there are no radios, no phones, no satellite TV, no wireless internet, not even light! Everything in this world is "wired." You have to think hard and accurately connect these wires through special "connectors" (monads) using these connectors, so that your various information processing devices can work normally, so that you yourself can see things. If you want to live in such a world, then please continue using Haskell.

In fact, to achieve the "pure" effect of functional programming languages, you don't even need to use a language like Haskell that completely opposes "assignment statements." You don't even need to use Lisp, a non-pure functional programming language. You can achieve the same effect using C language or even assembly language.

I'll give an extremely simple example in C language. Although the function body contains an assignment statement, it is a true "pure function":

int f(int x) {
 int y = 0;
 // function body with assignment statement
 return y + x;
}: int z = function1(int x, int y);
int y = function2(int x);
z = function3(int y);
return function4(int z);

function1(int x, int y): return (2 * x + 1);
function2(int x): return (2 * x);
function3(int y): return (y + 1);
function4(int z): return (z / 3);

这些函数调用，也是完全符合“纯函数”的定义的。因为它们的输入与输出完全相关，没有任何的“副作用”。这种写法，可以让代码更易于理解和调试。但是，在实际编程中，这种写法会导致函数调用的开销比赋值语句多。所以，在优化编译器优化的情况下，编译器会自动将这些赋值语句优化成直接的代码。1. function int f(int x) {
2. return g(2*x);
3. }
4.
5. function int g(int y) {
6. return h(y+1);
7. }
8.
9. function int h(int z) {
10. return z/3;
11. }

Function declarations:
1. int f(int x) { return g(2*x); }
2. int g(int y) { return h(y+1); }
3. int h(int z) { return z/3; }

Function calls:
1. f(x)
2. g(2*x)
3. h((2*x)+1)
4. z = (2*x)+1
5. z/3

Translation:
1. int f(int x) { return g(2*x); }
2. int g(int y) { return h(y+1); }
3. int h(int z) { return z/3; }

Function bodies:
1. return g(2*x);
2. return h(y+1);
3. return z/3;

Function calls in English:
1. Call function g with the argument 2*x.
2. Call function h with the argument y+1.
3. Return the result of dividing z by 3.

Function definitions in English:
1. Function f takes an integer argument x and returns the result of calling function g with the argument 2*x.
2. Function g takes an integer argument y and returns the result of calling function h with the argument y+1.
3. Function h takes an integer argument z and returns the result of dividing z by 3. It is clear that the definitions of the two f's are equivalent, yet the second definition lacks any assignment statements. The "assignment statements" in the first function are transformed into equivalent "parameter passing". These two programs, if compiled by my compiler, will generate identical machine code. Therefore, if you argue that assignment statements are incorrect, then function calls should also be incorrect. Should we still write programs then?

Blindly rejecting assignment statements is due to a partial understanding of the concept of "pure functions". Many researchers in languages like Haskell and ML don't seem to understand what I've been saying. They seem to believe that if an assignment is used, the function is no longer "pure". CMU professor Robert Harper is one such extremist. In a blog post, he argued that we shouldn't call the variables in a program "variables", because they're not the same as variables in mathematics and logic. However, is that really the case? If you understand the analysis of the example I gave, you'll find that the variables in a program are no different in essence from the variables in mathematics and logic.

The variables in a program are even stricter. If you consider mathematics as a programming language, it's unlikely that any mathematics book can be compiled and passed. Because they're full of variable name conflicts, undefined variables, and type errors - common programming design errors. Just notice the capital variables representing random numbers in probability theory (like X), and you'll find that mathematical variables are quite imprecise. This variable X doesn't even need to be assigned, it has "side effects" on its own! In fact, over 90% of mathematicians can't write good programs. So comparing the variables in mathematics to the variables in programming languages is reversed. We should judge programming languages' variables based on mathematics' variables, making mathematics' languages more precise.

Logicians are valuable, but they're not infallible, and they're not always right. Due to their infatuation with symbols, they often fail to see the essence of things. Although they understand many symbolic formulas and reasoning rules, they often don't understand what these symbols and reasoning rules represent in the natural world. As a result, they sometimes get even the most basic questions wrong (like confusing the scope of the universal quantifier ∀). Logicians' doctrines and reverence for the past might be the reason why Turing, studying under Church, was so isolated and miserable. In other words, this Turing, in some sense, surpassed Church, freeing some people from the rigid thinking of logic, making them "computer scientists". Of course, some computer scientists fell into another extreme, knowing nothing about the essence of logic, leading to designs without principles. However, that's not the focus of this article.: Therefore, based on what has been discussed, we don't need to pursue anything called "pure functional language," because we can write true "pure functions" without causing confusion by using assignment statements freely. Languages that allow free variable assignment actually surpass the expressive power of traditional logical reasoning. Can't you think of any logical formulas that can infer tomorrow's weather? Why are weather forecasts computed using programs instead of logical formulas? So I believe that programs, in some way, have surpassed the logical reasoning ability of mathematics. Evaluating programming languages solely based on a purely logical thinking mindset is quite narrow.

Regarding the misunderstanding of the concept of "functional language," it should be clarified to a great extent by now. The only requirement for a "functional language" should be the ability to define functions at any location and the ability to pass functions as values, regardless of whether these functions are "pure" or "impure." Therefore, languages like Lisp and ML fully meet the criteria for being called "functional languages."