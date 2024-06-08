---
layout: post
title: "About language pondering"
---


I have written so much about Haskell's drawbacks but haven't mentioned its advantages. In truth, I must admit that I learned something very important from Haskell, which is the way of thinking about "types". Although Haskell's type system has excessive constraints from a "philosophical" perspective (not a mathematical one), if a programmer has never studied Haskell, then his mind will lack a crucial thing. This thing is hard to learn from other languages besides Haskell, ML, Clean, Coq, and Agda.

### Inspiration from Haskell

A Scheme programmer who has never studied Haskell is most likely to make a mistake of treating any value other than #f (Scheme's logical "false") as #t (Scheme's logical "true"). Many people think this is a Scheme feature, but they are unaware that this is one of Scheme's rarest flaws. If you are familiar with the history of Lisp, you will find that in the earliest days, Lisp used nil (an empty list) as "false" and treated all other values as "true". This led to logical confusion.

Scheme made some improvements regarding Lisp's confusing practice, so in Scheme, the empty list '() and the logical "false" value #f are distinguished. This is obvious, one is a list, and the other is a bool, how can they be mixed up? Lisp's mistake influenced many other languages, such as C. C treats 0 as "false" and any non-zero value as "true". That's why you see some clever C programmers writing code like this:

## C Programmer's Error

int a = 0;
if (a) {
// some code here
}

// This code is incorrect, it should be:

int a = 0;
if (a == 0) {
// some code here
} In Scheme, nil is not considered false, but all values other than #f are considered true. Scheme's devotees usually tell you that this has the advantage that you can use

(or x y z)

instead of

(if (not (or x y z)) ...)

to test if none of x, y, z are true (or non-empty in the case of lists). In your given code snippet, since i is initially 0 and then incremented in the condition of the if statement, the condition will be true only when i is 1, so the code inside the if statement will be executed once. Such an expression, if any of its components is not #f, will directly return its actual value instead of #t. Therefore, you can write the code as:

(cond
 [(or x y z)
 [(lambda (found)
 [do-something-with found])]])

Rather than:

(let ([found (first-non-false x y z)])
[]
[do-something-with found]) (cond
 (not found)
 (do-something-with found))

The first code segment uses a special syntax in Scheme, the (lambda (found) ...) after => will take the value returned by (or x y z) as its parameter found, and then return the result of the function calculation. The second code segment does not assume that anything other than #f is "true", so it does not put (or x y z) in the condition of cond, but first binds its returned value to found, and then puts this value in the condition of cond.

This second code segment has an additional let and increased indentation, making it seem more complex to many people, so they think it's reasonable to treat anything other than #f as "true". However, Scheme made this situation short and simple at the cost of losing type accuracy. This cost is not worth it.

Haskell's type system helps you think rigorously about similar issues related to types. If you have never studied Haskell before, you won't find a type error in this place. However, Haskell went a bit too far. Due to its obsession with type inference, first-order logic, and category theory, Haskell introduced a lot of unnecessary complexity. I have designed over ten types of inference, some of which are much stronger than Haskell. Category theory is not really anything special. Many mathematicians call it "abstract nonsense," meaning it's too "general" and therefore says nothing. I finished an entire book on category theory one night and found that I had already understood the content through my own hands-on experience (implementing compilers, designing type systems, and static analysis, etc.). The theories in this book did not simplify programming languages. Quite the opposite, they made them more complex.

I am tired of the "genius attitude" of Haskell programmers, so I don't want to use Haskell anymore, but the things it "inspired" in me remain. My understanding of Haskell made me a better Scheme programmer, a better Java programmer, a better C++ programmer, and even a better shell script programmer. I can replicate the essence of Haskell's programming style in any language. However, continuing to use Haskell is like being imprisoned. Simple things become mysterious new terms in Haskell. I have read most of the papers by Haskell's designers, and I know how they came up with that stuff in just a few minutes. The truth is, there's not much new there. Most of it is due to the "new concepts" introduced (like monads), which create unnecessary problems. There are smarter people in the world with simpler and more powerful theories. So don't think Haskell is the pinnacle of the world.

Well, every programmer's life should ideally have a few months of dedicated Haskell study. Learning Haskell is like eating a few days of vegetarian food. Eating vegetarian food every day may leave you lacking in essential nutrients, but if you eat meat every day, you may never realize how much toxins are in your body.

[Being a specialist in one language's drawbacks]

I once told someone that there are some good things in C++, but I didn't mention that the bad things in C++ are numerous. C++ is a "toxic" language with many bad elements, just like pork. Some people have been writing C++ since childhood, spending their entire lives on it, just like eating pork every day. As a result, they have become very reliable in C++'s "pearls," leading to a phenomenon known as "obsession." For instance, many C++ programmers are very proficient in writing functors, but in reality, functors are just a workaround due to C++ not having first-class functions. C++ functors can never be as convenient as Scheme's lambda functions. Since you need a functor every time, you have to define a new class and then create its object. If there are free variables in the function, these variables must be put in the functor's fields through the constructor so that the functor knows their values when its "main method" is called. Thus, you need to define more fields. After all this effort, you end up with something that Scheme programmers use as easily as breathing.

Many proficient in functors believe that using functors shows their high proficiency. However, they don't realize that functors are not only a workaround but also something borrowed from functional programming languages. In the early days, C++ programmers were actually unaware of functors. If you think about it, C++ was born in 1983, while Scheme was born in 1975, and Lisp in 1958. C++ was born eight years later than Scheme, yet Scheme had lexical scoping lambda from the start. Functors are just a twisted imitation of lambda. In fact, many things added to C++ later (including the Boost library) are essentially imitations.

I remember November 11, 2011, when Bjarne Stroustrup, the creator of C++, gave a talk at Indiana University about C++11's new features. I was also there, and the host was Andrew, one of the chief designers of Boost (he later became my advisor for a while). He lamented that Stroustrup had chosen the date, only regretting that the talk wasn't at 11:00 am.

Although I admired Stroustrup's wit and humility, I could see that C++11 had little genuinely new compared to languages like Scheme. Most of the time, it was about correcting its own bad habits and learning from other languages, then hiding the traces of learning. However, due to C++'s widespread use and the abundance of existing code, its position and importance are still hard to shake. These "elders' sins," we will likely need several generations to make amends for.: What does C++ have that other languages don't? In fact, it's very little. I'll talk about it later if I have time.

### About learning several programming languages



Today I want to say that there's no language worth dedicating your entire life to mastering. Mastering a language means becoming a machine, not a person with your own thoughts. You should approach every language with a certain degree of skepticism, not blindly embrace it. Everyone should learn multiple languages to avoid having their thinking limited by a single language and unable to accept new, more advanced ideas. It's like learning at least one foreign language; otherwise, you'll be trapped in your own cultural thinking. Sometimes, these traditional cultural thoughts will lead you into unnecessary suffering that you can't escape.