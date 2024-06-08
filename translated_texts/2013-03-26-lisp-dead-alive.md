 Lisp is dead, long live Lisp!

There is an old saying, called "The king is dead, long live the king!" It means that the old king is already deceased, but his son has taken the throne. The humor lies in the fact that these two "kings" actually refer to different people, and it seems contradictory at first glance. Today, I chose a topic that mimics this saying and called it "Lisp is dead, long live Lisp!" I hope you will understand the meaning by the end.

First, let me summarize the advantages of Lisp. You might already know that some of Lisp's major advantages have been "inherited" into almost every popular language (Java, C#, JavaScript, Python, Ruby, Haskell, ...). Since I have already elaborated on some of these advantages in other blog posts, I will only list the main points here (key parts linked):

- Lisp's syntax is the most refined and beautiful in the world, and it is also the most efficient for parsing. This is a unique advantage of Lisp, as no other language has this feature. Some people like to design flashy-looking syntax, but in reality, they are making things harder for themselves. Why is this so? Please refer to this article "On Syntax."

- Lisp was the first language that could define functions at any position in a program and pass functions as values. This design gives it extremely powerful expressiveness. This concept was adopted by Python, JavaScript, Ruby, and others.: Lisp has the most powerful macro system in the world. The expressiveness of this macro system is almost at the theoretical limit. If you have only seen macros in C language, I can tell you that they are incomparable to Lisp's macro system.

Lisp was the first language to use garbage collection in the world. This forward-thinking idea was later adopted by languages like Java and C#.

You might not believe it, but many modern language features actually originate from Lisp — one of the oldest programming languages in the world. So, it's no wonder that every modern language is "evolving" towards Lisp. If you believe this, you might wonder why Lisp isn't mainstream today and why Lisp Machines lost to Unix. Besides business reasons, there are also technical issues.

Early Lisp versions suffered from a very serious problem: they used dynamic scoping. In other words, if your function definition contains "free variables," the value of these free variables will change depending on the location of the function call.

For instance, consider the following function f that takes a parameter y and returns the product of x and y.
[

Function f [
(lambda (y)
(* x y))]

In dynamic scoping, the value of x would change depending on where function f is called. This made the code unpredictable and difficult to reason about, which limited the adoption and practicality of Lisp. Later versions of Lisp, such as Common Lisp, adopted static scoping to address these issues. (SETQ f (LET ((X 1)) (LAMBDA (Y) (* X Y))))

In this code, x is a "free variable" for the function (LAMBDA (Y) (* X Y)), as it is not a parameter.

One might naturally assume, given the value of x is 1, that when f is called, the result should be (* 1 y), that is, equal to y's value. But what about in a dynamic scoping language? Let's see.

(You can try the following results in Emacs Lisp, as it uses dynamic scoping.) if we define a x as 2 in the outer layer of the function call:

(let ((x 2))
 (funcall f 2))

The scope of this x is different from that of x in the definition of f, so they should not interfere with each other. Therefore, we should get 2. However, the result returned by this code is 4.

Let's try another definition of x, with a value of 3:

[

In this context, the code snippet provided is written in Scheme, a dialect of Lisp programming language. The issue is that the value being returned by the function `f` is not as expected. The `let` form is used to define a local binding for the variable `x` with the value 2 before calling the function `f` with the argument 2. However, the result is 4 instead of 2.

The code snippet also includes an incomplete definition of a list, which is not relevant to the issue at hand. The issue can be reproduced with the following simpler code:

```scheme
(define x 2)
(display (funcall f 2)) ;; expected output: 2
(newline)
(define x 3)
(display (funcall f 2)) ;; expected output: 2
(newline)
(display (funcall f)) ;; expected output: error, due to undefined variable x in f

(define f (lambda (x) (+ x 2)))
```

In the provided code, the `x` defined in the outer layer is shadowing the `x` in the function `f`. When `f` is called with the argument 2, it uses the local `x` in its definition, which has a value of 3. Therefore, the result is 4 instead of 2.

To avoid this issue, the `x` in the outer layer should be defined with a different name, or the function `f` should be defined with a different name for its local variable. For example:

```scheme
(define y 2)
(display (funcall f 2)) ;; expected output: 2
(newline)
(define y 3)
(display (funcall f 2)) ;; expected output: 2
(newline)
(display (funcall f)) ;; expected output: error, due to undefined variable x in f

(define f (lambda (x) (+ x 2)))
```

Or:

```scheme
(define x1 2)
(display (funcall f 2)) ;; expected output: 2
(newline)
(define x1 3)
(display (funcall f 2)) ;; expected output: 2
(newline)
(display (funcall f)) ;; expected output: error, due to undefined variable x in f

(define f (lambda (x) (+ x 2)))
```

In both cases, the `x` in the outer layer has a different name than the `x` in the function `f`, so they do not interfere with each other. Our expected value is still 2, but the result is 6.

Let's try again. If we directly call:

(funcall f 2)

You would think this time we should get 2, right? But an error occurred:

Error: Funcall: Wrong number of arguments (1 for 2).

This error message indicates that the function 'f' is expecting two arguments, but we are only passing one (the number 2). Let's see what the definition of 'f' is to understand why this is happening. Lisp error: (void-variable x)
(* x y)
(lambda (y) (* x y))(2)
(funcall (lambda (y) (* x y)) 2)
(eval-r (funcall f 2) nil)
(eval-last-sexp nil)
(call-interactively eval-last-sexp nil nil)

Translation:

Lisp error: (void-variable x)
* x y
(lambda (y) (* x y))(2)
(funcall (function (lambda (y) (* x y))) 2)
(eval-r (funcall f 2) nil)
(eval-last-sexp nil)
(call-interactively 'eval-last-sexp nil nil)

Error: Unbound variable: x
Multiplication of x and y.
Anonymous function definition with argument y, multiplication of x and y.
Application of the function to the argument 2.
Evaluation of the result of the function call.
Evaluation of the last expression.
Interactive call of the last expression with no input and no output. I see the problem now? The behavior of f is influenced by the value of a variable named x at the call location. However, this x is not the same variable as x in the definition of f, they only share the same name. This can lead to hard-to-find errors, which was a major pain point in early Lisp. Fortunately, most modern languages have learned from this lesson, so you won't encounter this frustrating pain anymore. Neither Scheme, Common Lisp, Haskell, OCaml, Python, nor JavaScript use dynamic scoping.

Now that you might have understood what dynamic scoping is that drives people insane, if I tell you that Lisp Machine Lisp, which was used in Lisp Machines, employed dynamic scoping, you might understand why Lisp Machines failed. Because it is a world apart from modern Common Lisp and Scheme. I'd rather write C++, Java, or Python than Lisp Machine Lisp or Emacs Lisp.

Coming back to the point, why did early Lisp use dynamic scoping? It was not a deliberate "design," but rather an unintended "coincidence." You barely need to do anything, and it just turns out that way. This is not a joke, if you display f's value in Emacs, it will print:

'(lambda (y) (* x y))

This indicates that f's value is actually an S-expression, rather than a "closure" (closure) like in Scheme. In fact, Emacs Lisp directly treats the S-expression '(lambda (y) (* x y)) at the function definition as the function's "value," which is a naive approach. As a first-time functional language implementer, you might make the same mistake. The designers of Lisp made the same mistake back then. simple is indeed simple, but troublesome events followed. When calling f, for instance (funcall f 2), the value of y certainly comes from parameter 2, but what about x's value? The answer is: we don't know! What do we do then? Go to the "outer environment" and look for it, use the one we find, and if not found, report an error. This is why you have seen the previous phenomenon, the behavior of the function changing due to a completely unrelated variable. If you call (funcall f 2) alone, it will error due to the lack of x's value.

So what is the correct way to implement a function? It is to create a "closure". This is how Scheme, Common Lisp, and Python, C# do it. When a function definition is interpreted or compiled, the value of the free variables (like x) at that time is bound to the function code and put into a structure called a "closure". For example, the above function can be represented as (Closure '(lambda (y) (* x y)) '((x . 1))).

Here I use (Closure ...) to represent a "structure" (like C's struct). The first part is this function's definition. The second part is '((x . 1)), which is an "environment", essentially a mapping from variable to value. By using this mapping, we remember the value of x in the function definition instead of looking for it at the call site.

I won't delve into details here. If you're interested in implementation languages, check out my other blog post "How to Write an Interpreter". It teaches you how to implement a correct, bug-free interpreter.

The opposite of dynamic scoping is "lexical scoping". I just told you about closures, which is a way to implement lexical scoping. The first language to implement lexical scoping was not from the Lisp family, but Algol 60. Algol was named after its goal to implement algorithms. Although Algol had many drawbacks compared to Lisp, it got lexical scoping right. Scheme learned lexical scoping from Algol 60 and became the first Lisp dialect to use it. Nine years later, the "grandfather" of the Lisp family, Common Lisp, was born, and it also adopted lexical scoping. It seems heroes have similar visions. You might have found out, Lisp is not a single language, but a family of languages. These languages called the "Lisp family" share a common point: they all use S-expressions as their syntax. If you praise them for this reason, then what you are praising is actually S-expressions, not these languages themselves. A language's essence should be determined by its semantics rather than its syntax. You can even design multiple different syntactical variations for the same language without changing its essence. For instance, I once designed a Lisp syntax for TeX, which I named SchTeX (Scheme + TeX). SchTeX files look like this:

(documentclass article (11pt))
(document
 (abstract (...))
 (section (First Section)
 ... )
 (section (Second Section)
 ... )
): It's clear that although it looks like Scheme, its essence is still TeX.

So, because Scheme uses S-expressions for syntax, it's called a "dialect" of Lisp, but that's not entirely accurate. Scheme, Emacs Lisp, and Common Lisp are actually three different languages. Racket was once called PLT Scheme, but its differences from Scheme have grown so much that PLT renamed it Racket. They had their reasons.

So, you might understand why this article's title is called "Lisp is dead, long live Lisp!" Since the two "Lisps" in the sentence are completely different languages. "Lisp is dead" refers to Lisp Machine Lisp and other Lisps that have died out due to serious design issues. "Lisp long live" refers to Scheme, Common Lisp, and other Lisps that will continue to exist. They lead in advanced areas and will be more widely adopted and showcased.

(In fact, the death of old Lisp also has another important reason, which is that the efficiency of the code generated by early Lisp compilers was extremely low. I'll save that topic for the next blog post.)