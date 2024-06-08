---
layout: post
title: "Hindley-Milner"
---

: The fundamental error of Hindley-Milner type systems

In the past, I once presented a slide sequence publicly which was my last talk at Indiana University in October 2012. At that time, I didn't explicitly state the significance of these conclusions. In fact, it revealed a fundamental error in ML and Haskell type systems based on Hindley-Milner.

This error originated from the misunderstanding of the relationship between first-order logic's "universal quantifier" (universal quantifier, usually written as ∀) and program functions in the HM system. In the HM system, a polymorphic function can be inferred to have a type containing a universal quantifier, such as x->x being inferred as ∀a.a->a. However, the HM system determines the position of this universal quantifier in an arbitrary way, leading to the bias of type variable scopes.

My research shows that this error stems from a crucial design decision in the HM system called let-polymorphism. If the right-hand side function is a polymorphic function, such as:

let f = \x->x in
[

In this case, the universal quantifier's position is determined by let-polymorphism, leading to the aforementioned issues. This can result in unexpected type inference results and make it difficult to reason about program behavior.

To address this issue, researchers have proposed alternative type systems, such as System F and dependent type systems, which provide more explicit control over the scopes of type variables and the relationships between functions and their types. These systems offer more predictable and reliable type inference results, making it easier to reason about program behavior and avoid potential errors.: Let-polymorphism always places quantifiers in the position to the right of let's "=" sign. However, this is a very incorrect approach, with a degree of error similar to that of early Lisp's dynamic scoping. This results in the position of quantifiers changing not based on the program's structure, but on its format. As for what dynamic scoping is, you can refer to my blog post on the subject.

To rectify this error, numerous papers have been published over the past 30 years, proposing various "improvement measures" such as value restriction, MLF, etc. However, my research shows that all these "improvement measures" are ugly hacks because they don't address the root cause of the problem, making them effective only for certain situations but not universally. As a result, I can easily write a correct program that bypasses these type systems' checks, as shown in this English blog post. If you understand the root cause of the problem, you'll find that HM system's error is irreparable because it touches upon the foundations of the HM system. To address this issue, let-polymorphism must be removed.

I propose a solution to this issue by performing "generalization" at the lambda position, which means putting the ∀ at the lambda position instead of let. This eliminates let-polymorphism. However, this approach renders the HM system no longer an HM system, as its "modular type inference" property disappears. Since types contain program control structures, this type system appears to be doing "modular type checking," but in essence, it's performing "interprocedural static analysis" across procedures. In other words, modular type inference, in an HM system without "type tags," is inherently unachievable.

To achieve fully general modular type checking while allowing for the existence of polymorphic functions, we will ultimately need to manually write types for function parameters. This results in a complete loss of the HM system's original design intent.