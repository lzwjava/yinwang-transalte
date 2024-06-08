---
layout: post
title: "How to Write an Interpreter"
---


Writing an interpreter is usually the first step in designing and implementing a programming language. An interpreter is a simple yet profound thing, and many people don't know how to write one, so I decided to write an introductory piece on this topic.

Although I try to start from the most basic principles and depend as little as possible on other knowledge, this is not a programming introductory textbook. I assume you already understand Scheme language and basic programming techniques (such as recursion). If you have no idea about these, I suggest you read the first and second chapters of SICP or the first few chapters of HtDP, but don't worry too much about the exercises. Remember not to read too many books, or you might get lost ;-). Of course, you can also read this article directly, and look up anything you don't understand.

A common mistake when implementing a language is to start by trying to implement a very complex one (like JavaScript or Python). You'll soon be discouraged by the complexity of these languages and their historical design issues. The best way to learn to implement a language is to start with the simplest, cleanest language and quickly write a usable interpreter. Then gradually add features while maintaining correctness. This way, you can construct a complex interpreter methodically.

For this reason, this article focuses on a very simple language called "R2." It can be used as a simple calculator and has features like variable definition, function definition, and invocation. Our tool: Racket

The interpreter for this article is implemented in Scheme language. Scheme has many "implementations", and I used one called Racket here, which can be downloaded for free. To keep the program simple, I used a little Racket's pattern matching feature. I don't have a particular preference for Scheme implementations, but Racket is convenient and suitable for teaching. If you use other Scheme implementations, you may need to make some adjustments.

Racket has macros, so it can actually become many kinds of languages. If you have used DrRacket before, the "language setting" in it might have been changed to R5RS or something similar. So if the following program cannot run, you may need to check the "language setting" in DrRacket and set it to "Racket".

Racket allows the use of brackets instead of just parentheses, so you can write code like this:

( [ ) )

( ( [ ] ) )

( ( [ a ] [ b ] ) [+ a b] )

( ( [ ( a b ) ] ) [* a b] )

( ( [ ( a ) ( b ) ] ) [+ a (- b a)] )

( ( [ ( a ) ] ) [* a a] )

( ( [ ] ] ) 42 )

( ( [ x ] [ ( [ x ] [ x x ] ) ] ) [car] )

( ( [ x ] [ ( [ x ] [ x x ] ) [ x ] ] ) [cdr] )

( ( [ ( a b ) ] [ ( [ a ] [ a ] ) [ ( [ b ] [ b ] ) ] ) ] ) [cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ) ] ) [list] )

( ( [ x ] [ x ] ) [identity] )

( ( [ x ] [ ( [ x ] [ x ] ) ] ) [quoted] )

( ( [ x ] [ ( [ x ] [ x ] ) [ ( [ x ] [ x ] ) ] ] ) [quasiquoted] )

( ( [ x ] [ x ] ) [if] )

( ( [ p q r ] [ if p r q ] ) )

( ( [ x ] [ ( [ x ] [ x ] ) [ ( [ x ] [ x ] ) ] ] ) [cond] )

( ( [ p ] [ p ] ) [else] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [let] )

( ( [ x ] [ x ] ) [lambda] )

( ( [ x ] [ x ] ) [define] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [let-values] )

( ( [ x ] [ x ] ) [begin] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [define-values] )

( ( [ x ] [ x ] ) [quote] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [unquote] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [unquote-splicing] )

( ( [ x ] [ x ] ) [define-syntax] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [syntax-rules] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [syntax-case] )

( ( [ x ] [ x ] ) [require] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [apply] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [list-ref] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-ref] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-ref] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-length] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-length] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-set!] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-set!] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-trim] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-split] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-replace] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-reverse] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-list->vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-vector->list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-vector->string] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [string-list->string] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector->list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [list->vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector->string] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [list->string] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reverse] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reverse] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reverse] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reverse] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-map] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-filter] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reduce] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-for-each] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-cons] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-list] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-vector] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-append] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-copy] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-concat] )

( ( [ x y ] [ ( [ x ] [ x ] ) [ ( [ y ] [ y ] ) ] ] ) [vector-reverse] )

( ( [ x y ] [ ( [ x ] [ let [x] be the first element.2 + x

This is a simple mathematical expression in Chinese characters. The left side represents the number 2, and the right side represents the variable x. The "+" symbol is represented by the character "+" in this context. I. Brackets and parentheses can be interchanged, the only requirement is that brackets must match. I usually use brackets to represent "static" data (like [x 1],[y 2] up above), which helps distinguish it from function calls and other "action" code. This improves code readability, as it becomes visually monotonous with too many parentheses.

II. Interpreter is what

An interpreter is a type of computer software that directly executes instructions written in a programming or scripting language without compiling them into machine code first. It reads and executes the code line by line, interpreting each instruction as it goes. This makes it a popular choice for prototyping, experimenting with new ideas, and developing scripts or small applications. Interpreters can also provide interactive environments for users to enter and run code in real-time. Examples of popular interpreted languages include Python, Ruby, JavaScript, and Racket. Preparation is done here. Now let's talk about interpreters. To put it simply, an interpreter is similar to a calculator. An interpreter is a function that takes an "expression" and outputs a "value." For example, if you input the expression '(+ 1 2), it outputs the value, the integer 3. An expression is a "representation" or "symbol," while the value is more akin to the "essence" or "meaning." We "interpret" the symbol to get its meaning, which might be why it's called an "interpreter."

It's important to note that an expression is a data structure, not a string. We use a structure called an "S expression" (S-expression) to store expressions. For instance, the expression '(+ 1 2) is actually a linked list (list), containing three symbols: +, 1, and 2, rather than the string "(+ 1 2)."

Extracting information from structured data like this is convenient and reliable, while extracting information from strings is cumbersome and error-prone. Scheme (Lisp) language uses structured data extensively and minimally uses strings, which is one of the advanced aspects of Lisp systems compared to Unix systems.

From a theoretical computer science perspective, every program is a description of a machine, and an interpreter is simulating the operation of this machine, or performing the "computation." In a sense, an interpreter is the essence of computation. Of course, different interpreters will result in different computations. A CPU is also an interpreter, specialized in executing machine language. If you deeply understand interpreters, you can understand from the essence why CPUs are designed in a certain way and what their advantages and disadvantages are, not just as their passive users.

Abstract Syntax Tree (AST)

The code represented by S-expressions is essentially a kind of data structure called a "tree." More specifically, this is called an "Abstract Syntax Tree" (Abstract Syntax Tree, abbreviated as AST). In the following text, for simplicity, we will refer to it as a "syntax tree."

Like a normal tree structure, a syntax tree consists of nodes that are either "leaf nodes" or a "subtree." Leaf nodes are indivisible "atoms," such as numbers, strings, operators, and variable names. Subtrees are divisible "structures," such as arithmetic expressions, function definitions, function calls, etc.

For example, the expression '(* (+ 1 2) (+ 3 4)) corresponds to the following syntax tree structure:

[Multiplication
 [Addition
 [Number 1]
 [Number 2]
 ]
 [Addition
 [Number 3]
 [Number 4]
 ]
] In the given, *, two plus signs, 1, 2, 3, 4 are all leaf nodes, while the three red nodes represent subtree structures: '(+ 1 2), '(+ 3 4), '(* (+ 1 2) (+ 3 4)).

### Tree Traversal Algorithm

In our basic data structure courses, we all learned the traversal operations of binary trees, i.e., preorder traversal, inorder traversal, and postorder traversal. Syntax trees and binary trees have no significant differences, so you can also perform traversals on them. The algorithm of the interpreter is one such traversal operation on the syntax tree. Since this originates from the same source, let's first practice traversing binary trees. Once we've done that, we can extend this code into an interpreter.

This exercise is as follows: write a function named tree-sum that performs "summation" on binary trees, adding up all the numbers in the nodes and returning their sum. For example, (tree-sum '((1 2) (3 4))) should return 10. Note: this is a binary tree, so it won't contain subtrees longer than 2, you don't need to consider cases like ((1 2) (3 4 5)). The examples to consider are like (1 2), (1 (2 3)), ((1 2) 3), ((1 2) (3 4)), ...

(As a way to maximize your learning experience, it's best if you try writing out this function before continuing.) Alright, I hope you got similar results. Here's my code:

Racket

(define
 [function-name]
 ...
) tree-sum (lambda (exp))

This is likely a Lisp-style function definition in Chinese characters. The English translation would be:

tree-sum (function (exp))

or

tree-sum (defun exp () ...)

in Lisp, where `exp` is the name of the parameter. The function `tree-sum` takes an expression `exp` as an argument and performs some computation on it. The exact meaning of the function depends on the context in which it is used. (match // perform pattern matching on input exp

[( // [
[ // [

This text appears to be a snippet of Lisp or Scheme code, likely written in a text editor or IDE that does not support rendering Chinese characters. The English translation of the comments is as follows:

(match // perform pattern matching on input exp

[( // [
[ // [ two x's

This text appears to represent two "x" characters in Chinese, but without the actual characters or punctuation, it is impossible to provide an accurate translation. The question mark at the beginning suggests that this is a query or incomplete sentence in Chinese, and the parentheses may indicate some additional context or information. However, without the actual characters, it is not possible to determine the meaning of the text with certainty. Is `exp` a number x? If yes, return this number x. Is exp a node with two subtrees?

(function () {
var v1;
// function body here
})(); recursive call to tree-sum for sub-tree e1. Recursively call "tree-sum" on right subtree e2.1st version:
+
v1
v2
++++++++++

2nd version:
+
v1
v2
++++++++++

Translation:
+ Version 1
v1
Version 2
++++++++++

Note: The text provided seems to be incomplete and contains extra symbols, so the translation is based on the given context. return the sum of v1 and v2, which are the results of recursively calculating the sum of the left and right subtrees;

You can test its correctness using the following example:

(tree-sum
 [1]) Two parentheses with nothing inside => Three

tree-sum 1
(
2
(
3
))
;; => Six

Explanation:
The Chinese text consists of numbers and symbols. The numbers are "1" and "6", and the symbols are "(" and ")". The text can be interpreted as a mathematical expression with the following meaning:

1 * (2 * (3))

Using the given semicolon ";;" as a separator for successive expressions, the text can be interpreted as:

1 ;; (2 * (3))

Evaluating the expression, we get:

1 ;; 6

Using the semicolon as a separator for concatenation instead of successive expressions, we get:

"One Six"

However, since we are asked to provide only the English translation without any Chinese characters or punctuation, the correct answer is "Six". tree-sum
[
[1, 2]
] three parentheses are equal to six

function tree-sum 1

2

(
3 
4
)

* Empty parentheses: ()
* Character 1: 1
* Character 2: 2
* Characters 3 and 4: [3 4]1. If exp is a number, return this number.

2. 如果输入exp是一个字符 '('，那就创建一个空栈 s ，然后继续处理下一个字符。

[

3. 如果输入exp是一个字符 ')'，那就检查栈 s 是否为空。如果栈不为空，那就不断地弹出栈顶元素，直到遇到一个 '('，并且返回这个 '(' 所包含的子表达式的值。如果栈为空，那就抛出一个错误，因为 ')' 没有对应的 '(' 。

[

4. 如果输入exp是一个运算符，那就取出栈顶两个元素，分别是运算符 op2 和运算符 op1，并且检查 op1 和 op2 的优先级关系。如果 op1 优先级高于 op2，那就将 op1 和 op2 都弹出栈，并将 op1 放入栈顶，继续处理下一个字符。如果 op1 优先级低于 op2，那就计算 op2 运算符对应的运算，将结果压入栈中，然后继续处理下一个字符。

[

5. 如果输入exp是其他字符，那就直接将这个字符压入栈中，继续处理下一个字符。

[

6. 最后，当所有字符都被处理完毕后，栈中只剩下一个元素，那就返回这个元素，即最后一个运算符的运算结果。

[

7. 注意，这个算法假设输入表达式中没有空格字符，因此不需要处理空格字符。如果输入表达式中有空格字符，那就需要在处理字符时先过滤掉空格字符。

[

8. 这个算法的时间复杂度为 O(n)，其中 n 是输入表达式的长度。

[

9. 这个算法的空间复杂度为 O(h)，其中 h 是表达式中最大递归深度的长度。

[

10. 这个算法适用于中缀表达式，如 "3 + 5 * 2"。对于后缀表达式，如 "3 5 + 2 *"，需要使用不同的算法。: If tree is of the form (,e1 . e2) where e1 and e2 are sub-trees, recursively call tree-sum on e1 and e2, obtain v1 and v2, then return v1 + v2.

Your own code might use if or cond statements for branches, while mine uses Racket's pattern matching (match). This example could also be done with if or cond, but I am planning to extend this code into an interpreter, so I used match earlier. This way, when comparing later code, the patterns will be more obvious. Now, let me briefly explain how this match expression works.

### Pattern Matching

Since this text involves some Racket-specific technical details, feel free to skip this section if you're already familiar with Racket's pattern matching. You can also refer to the Racket pattern matching documentation instead. However, I recommend not to read too much documentation as I only use a few pattern matching features here, which I will explain below.

The general form of pattern matching is as follows:

(match exp
[(_ e1 . e2) v1]
[(_ e1) v2]
[(_) v3]
...)

The match expression takes an expression (exp) and checks it against the patterns in the list. When a pattern matches, the corresponding value (v1, v2, v3, etc.) is returned. The patterns in the list are in order of preference, meaning the first pattern that matches will be executed.

In the provided text, the pattern (_ e1 . e2) matches a tree with two sub-trees, e1 and e2. This pattern is used in the first branch of the match expression. The other patterns can be understood similarly.

In summary, the text describes a recursive tree sum function, implemented using Racket's pattern matching. The function takes a tree as an argument and recursively sums the values of its sub-trees. The pattern matching expression is used to check the structure of the tree and apply the recursive call accordingly. Mode
Result Mode
Result It first evaluates x, then branches based on the value structure. Each branch consists of two parts: the left is a pattern, and the right is a result. The semantics of the entire match statement are as follows: from top to bottom, find the first pattern that can match x's value, and return its right result. The left pattern in matching may bind some variables, which can be used in the right expression.

Pattern matching is a kind of branch statement. Logically, it is the same as Scheme (Lisp)'s cond expression or Java's nested condition statement if ... else if ... else ... However, unlike the conditions in the if statement, each match statement's left pattern can accurately and concretely describe the shape of the data structure, and at the same time, bind members of the structure during matching. This allows us to conveniently access structure members in the right side without using accessor functions or property syntax (attribute). Moreover, patterns can have nested substructures, so they can represent complex data structures in one go. I'll give you a concrete example. In my code, I used the following match expression:

(match
 exp
 [
 [
 [

Here is the English translation of the Chinese text without any Chinese characters or punctuation:

I'll give you a concrete example. In my code, I used the following match expression:

(match exp [ [ [ ] ] ] ) two x's

This text appears to be representing two "x" characters in Chinese, but without the actual Chinese characters or punctuation, it is impossible to provide an accurate translation. The question mark before "number" suggests that the text is asking for the translation of a Chinese number, but without the number itself, it cannot be translated. (
e1

,
e2
)

This text appears to be an empty parentheses with two placeholders "e1" and "e2". It does not contain any meaningful Chinese characters or text to translate. let [v1 tree-sum]

This is a Lisp-like syntax representation of a function definition in Chinese, where "let" is used for local variable binding, "[v1]" represents an unnamed variable, and "tree-sum" is the name of the function. The function takes no arguments. tree\_sum

This appears to be a segment of code or a variable name in Chinese characters, likely used in a programming context. The English translation is "tree sum," which could refer to the sum of the values in a tree data structure. e2):
( +
v1
v2

This appears to be a fragment of code written in a programming language such as Python or JavaScript, likely representing some sort of arithmetic operation or function call. However, without more context or complete information, it's difficult to provide an accurate English translation. The text does not contain any discernible Chinese characters or punctuation. In the second line, '(e1, e2)' is a pattern (template) used to match 'exp'. If 'exp' is '(1 2)', then it matches with '(e1, e2)' and binds 'e1' to '1' and 'e2' to '2'. This is because they have the same structure:

(
,e1

,
e2 1
2

This text appears to be empty or contains only numbers without any context or clear meaning in Chinese. The English translation would simply be the numbers 1 and 2. I'll translate the text into English for you, providing only the English translation without any Chinese characters or punctuation:

Said in essence, a pattern is a structure that can contain "names" (like e1 and e2), such as (,e1 ,e2). We use this named structure to match actual data, like (1 2). When they correspond one by one, these names get bound to the values at the corresponding positions in the data.

The first line's "pattern" is special, (? number? x) means a regular condition test, similar to (number? exp), if this condition is met, it binds exp's value to x, so x can represent exp on the right side. For structures that cannot be further divided (like numbers, booleans), you can only use this method to "match". It may seem strange at first, but you'll get used to it.

Pattern matching is quite useful for interpreters and compilers because the syntax trees of programs often have nested structures. Without pattern matching, you would have to write verbose, complex, and less readable code to describe the expected structure. Due to the deep nesting of structures, it's easy to overlook boundary cases, leading to errors. Pattern matching can intuitively describe the expected structure, prevent overlooking boundary cases, and conveniently access structure members.

For this reason, many languages derived from ML (like OCaml, Haskell) have pattern matching capabilities. Since ML was originally designed for implementing programming languages, Racket's pattern matching was also influenced by ML, and their principles are identical.

Well, we've finished the tree traversing exercise. However, what does this have to do with interpreters? Let's just make a few adjustments, and we'll have a simple interpreter. A calculator is also an interpreter, but it can only handle arithmetic expressions. Our next goal is to write out a calculator. If you give it '(* (+ 1 2) (+ 3 4)), it will output 21. Don't underestimate this calculator; we will later modify it to obtain a more functional interpreter.

The code above uses recursive traversal to sum the numbers in the tree. In that code segment, there is actually a hidden interpreter framework. Observe carefully, an arithmetic expression '(* (+ 1 2) (+ 3 4)) is not much different from a binary tree '((1 2) (3 4)). Do you notice? The only difference is that there is an additional operator: one '* and two '+ in each subtree structure. It is no longer a binary tree, but a more general tree structure.

This difference also brings about the distinction between summing a binary tree and the interpreter algorithm. When summing a binary tree, we do addition at every node. When interpreting an expression, we don't necessarily do addition at every node. Depending on the operator of the subtree, we may choose addition, subtraction, multiplication, or division.

Here is the code for this calculator. It accepts an expression and outputs a number as the result. (define
 (

This is a Racket definition. Here is a translation:

(define
 [

This defines a list of variables with the given names. The values of these variables will be empty lists initially.

1. i
2. j
3. sum
4. n
)

; 初始化 n 为给定值

(define
 n 5
)

; 使用递归计算和初始化 i 和 sum

(define
 (sum-list lst)
 (cond [(null? lst) sum]
 [else
 (let ([i (car lst)])
 (sum-list (cdr lst)
 (define
 temp (+ i sum)
 )
 (sum-list '()
 sum temp)
 )
 )
 )
)

; 调用 sum-list 函数计算和初始化 i 和 sum

(sum-list '(1 2 3 4 5) 0)

; 输出和 sum

(display sum)
(newline)

This Racket code declares the use of the Racket language and then defines a list of variables named i, j, sum, and n. The variable n is initialized to the value 5. The sum-list function is defined using recursion to calculate the sum of the elements in a given list and initialize i and sum. The sum-list function is then called with the list (1 2 3 4 5) and an initial sum value of 0. The final sum value is then displayed. calclamode (
exp function
)

This appears to be a Lambda expression in Scheme or a similar Lisp dialect. The English translation of the given Chinese text would be:

calculate (
expression function
)

So, the English translation of the Chinese text is to calculate using an expression function. Branch matching: two situations of expression

[(
[

This text appears to be describing branch matching, which is a concept in computer science related to pattern matching and expression evaluation. The text mentions that there are two situations or cases in the context of branch matching and expression evaluation. However, without additional context or specific terms defined, it's difficult to provide a precise translation without introducing Chinese characters or punctuation. The provided text seems to be incomplete or fragmented. two x's

This text appears to be representing two "x" characters in Chinese, but without the actual characters, it's impossible to provide an accurate translation. The number before the characters, "？number？", is also missing and might provide context for the translation. It is a number, just return.

In the context of programming, this comment in Chinese translates to English as follows:

This is a number, just return. Matching extraction operator op with operands e1, e2

(
let[v1

(calculate

e1)
]

This text appears to be written in a programming or markup language, possibly Lisp or similar. The English translation is:

[v1

(calculate

e1)
]

This means that the value of 'v1' should be passed to the 'calculate' function, and the result should be assigned to 'e1'. Recursively call calc with self, getting the value of e1.

In other words, the function `calc` calls itself with `self` as an argument to obtain the value of `e1`.): recursively call calc to get e2's value

(
match

op
[
{
// function body for matching operator
}
]
) Branch matching: operator op has 4 cases

+ (
+ v1

This text describes the concept of branch matching in programming, specifically focusing on the four different situations that can arise when using the '+' operator in a branch condition. The text begins with a semicolon, which is not typically used at the beginning of a sentence in English, but it does not affect the meaning of the text significantly. The English translation is provided below:

Branch matching: operator op has 4 cases:
+ (
+ v1

This can be interpreted as:

Branch matching for operator op involves the following four cases:
1. '+' sign followed by an open parenthesis '('
2. '+' sign followed by '+' sign
3. '+' sign followed by a variable 'v1'
4. Open parenthesis '(' followed by '+' sign and a variable 'v1'

Each case represents a different way that the '+' operator can be used in a branch condition. The first case represents the use of the '+' operator as a unary operator before an expression in parentheses. The second case represents the use of the '+' operator as a binary operator between two expressions. The third case represents the use of the '+' operator as a prefix increment operator for a variable. The fourth case represents the use of the '+' operator as a postfix increment operator for a variable, but since the text only shows the symbol '+' following the variable 'v1', it can be assumed that this is a typo and the intended meaning is the third case. if it is a plus sign, output result as (v1 + v2)

In other words, if the input is a plus sign, the output should be the sum of v1 and v2. if it is a minus sign, multiplication sign, or similar, handle it similarly

v1 - v2

or

v1 * v2 for multiplication
v1 / v2 for division [Empty]

(Version 1)

(Version 2)1/
/
(
/
Version 1
/

This text appears to be a comment or code snippet in Chinese characters with some English words mixed in. It's not clear what the Chinese characters represent without additional context. The English words "Version 1" are easily translatable and can be provided as is. You can obtain the following result:

(
calc
) 1. +: addition
2. ): right parenthesis
3. ;; : comment
=> : arrow

So, the given Chinese text is actually not Chinese characters but Lisp-like code. The translation in English would be:

1. addition
2. right parenthesis
3. comment
=> : arrow. Calc
( multiply
2
3
); Semicolon; => 6

(
calc

'
(
*
[

This text appears to be a mix of Lisp-style code and comments in English and semicolon notation for Lisp. The semicolon is used in Lisp to denote a comment. The text translates to:

; Semicolon; => 6

(calc '(*) ; this is a comment
[

The comment indicates that the multiplication operator (*) is being used. The number 6 is not part of the code and is likely a placeholder or an error. The text does not contain any Chinese characters.1.
2.

This text appears to be empty or incorrect as it only contains parentheses and whitespaces. The numbers 1 and 2 are outside of any parentheses and do not seem to be related to the text inside the parentheses. Without additional context, it is difficult to provide an accurate translation. Three
Four
Double quotation marks quadrupled

;; => twenty-one

(Here is the complete code and example. You can download it here.) In contrast to the previous binary tree sum code, you will find they are surprisingly similar due to the fact that interpreters are essentially tree traversal algorithms. However, do you notice any differences between them? The differences lie in:

1. The expression pattern in the arithmetic part includes an additional "operator" (op) leaf node: (, op ,e1 ,e2)

2. Instead of returning (+ v1 v2), we return different results based on the op's distinction after evaluating the subtrees e1 and e2: (matchop['+(+v1v2)']['-(-v1v2)']['*(*v1v2)']['/(/v1v2)])

Ultimately, an arithmetic expression interpreter is just an extended tree traversal algorithm.

### R2: A very small programming language

In comparison to the previous binary tree sum code, you'll notice they share striking similarities because interpreters are essentially tree traversal algorithms. However, have you identified any differences? The distinctions are as follows:

1. The arithmetic expression pattern incorporates an additional "operator" (op) leaf node: (, op ,e1 ,e2)

2. Rather than returning (+ v1 v2), the outcome depends on the op distinction after evaluating the subtrees e1 and e2: (matchop['+(+v1v2)']['-(-v1v2)']['*(*v1v2)']['/(/v1v2)])

In conclusion, an arithmetic expression interpreter is merely an expanded tree traversal algorithm. I have implemented a calculator, now let's transition to a more powerful language. For convenience, I gave it a cute name, R2. R2 has only four additional elements compared to the previous calculator. They are: variables, functions, bindings, and calls. With the previously introduced arithmetic operations, we get a simple programming language that only has 5 distinct constructs. In Scheme syntax, these 5 constructs look like this:

- Variable: x
- Function: (lambda (x) e)
- Binding: (let ([x e1]) e2)
- Call: (e1 e2) Arithmetic: (• e2 e2)

(Here, • is an arithmetic operation symbol, which can be chosen from among +, -, *, /)

In general programming languages there are many other constructs, but trying to implement all of them at the outset will only confuse you. It's best to first understand these few things correctly before gradually adding other elements.

The meaning of these constructs is almost identical to those in Scheme. If you don't know what "binding" is, you can consider it as a "variable declaration" in common languages.

However, note that unlike common languages, our functions only accept one parameter. This is not a serious restriction, as in our language, functions can be passed as values, i.e. "first-class functions". So you can use nested function definitions to represent functions with more than one parameter. A example, (lambda (x) (lambda (y) (+ x y))) is a nested function definition, which can also be regarded as a function with two parameters (x and y), returning the sum of x and y. When such a function is called, it requires two layers of calls, like this:

((
lambda
(x)
[
 lambda
(y)
(+ x y)
])
x
) Anonymous function:

Function (y) {
Summation;
}

Sum: (
+
)

Function (y) {
Sum of y;
} x, y, happy or laughing, 1, parenthesis or bracket.

Without additional context, it is difficult to provide an accurate translation as the Chinese characters provided do not form a complete sentence or phrase. The parentheses and emoticons may have different meanings depending on the context in which they are used. two => three

In programming language terminology, this approach is called currying. It may look tedious, but our interpreter can keep it simple once we understand the basics. We'll be able to implement real multi-parameter functions without delay once we grasp the fundamentals.

Additionally, our binding syntax (let ([x e1]) e2)), compared to Scheme's binding, has some limitations. Our let only binds one variable, whereas Scheme can bind multiple, like (let ([x 1] [y 2]) (+ x y)). This isn't a significant restriction, as we can work around it by using nested let bindings: let [x] be the array with the following content:
1

Therefore, the English translation of the given Chinese text without any Chinese characters or punctuation would be:

let x be [1] let [y 2]

This appears to be a Lisp-style code snippet in Chinese characters. The English translation would be:

let [y 2]

This means that the variable 'y' is being assigned the value 2 in this Lisp-like code. R2 interpreter

This is a simple English translation of the given Chinese text which appears to be describing an "R2 interpreter." The text itself does not contain any meaningful content beyond this identification. Below is our interpreter for today, which can run an R2 program. Please take note of the comments for each part.

#
lang racket

;;; Following three definitions, env0, ext-env, lookup, are basic operations on environment:

;; Empty environment
[env0]
([])

;; Extend environment
[ext-env env ext-bindings]
(cond [(null? ext-bindings) env]
[(cons (car ext-bindings) (cons env (cdr ext-bindings)))]
)

;; Lookup variable in environment
[lookup var env]
(cond [(eq? (car env) var) (cdr env)]
[(lookup var (cdr env))]
) (define (extend env x v)
;; Extension. Extend the environment 'env' by binding variable 'x' to value 'v',
;; resulting in a new environment)
(cond ((null? env) (list v))
((eq? (car env) x) (cons (cons x v) (cdr env)))
(else (cons (car env) (extend (cdr env) x v)))) (define
 ext-env

 (lambda [
 ...
 ]
 ...
 ))x is void, v is a verb, env is an environment.

Therefore, without context, it is difficult to provide a precise translation. However, a possible translation based on the given information could be:

"Void a verb in an environment."

or

"Environment for voiding a verb."

or

"Verb voiding in an environment."

It's important to note that the given Chinese characters do not form a complete sentence or phrase, and the meaning may vary depending on the context in which they are used. conf, x, ., comma, x, dot, comma, v, space, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, space, v, space, (define (find-value x env)
 (if (null? env)
 #f
 (if (equal? x (car env))
 (cdr env)
 (find-value x (cdr env)))))) look up
(lambda (x env)
...
)

This is a Lambda expression in Scheme or similar functional programming languages. The English translation would be "look up" as a verb meaning to search for or find information. The lambda expression defines an anonymous function that takes an argument `x` and an environment `env` as inputs. The body of the function is not provided in the given code snippet. let (p) {
  // code block for variable p
}

// function declaration with one parameter p selction function for associative lists in list data structure, checks if an element with a specific key exists and returns its value.

env: environment, a collection of bindings or associations between names and values.

function definition, the function takes no arguments and returns multiple values.

The first bracket '[' indicates the beginning of a list. The second bracket ']' indicates the end of the list.

The parentheses '(' and ')' are used for function calls or grouping expressions.

The 'cond' keyword is used for conditional expressions.

Therefore, the Chinese text 'assq' can be translated to 'selection function for associative lists'.[Not a valid Chinese character sequence. This sequence appears to be a combination of English characters, a parenthesis, and a hash symbol, which do not have a direct translation to Chinese characters.] else
( cdr
p
)
)
)
)

This is likely a Lisp-style code snippet. The English translation would be:

else
( cdr p )
)
)
)

Here, 'else' is a keyword in Lisp used for conditional statements, 'cdr' is a function that returns the rest of a list, and 'p' is a list or a variable. The code inside the parentheses is executed if the condition before 'else' is not met.: Closure structure definition, includes a function definition f and the environment in which it was defined

(
struct Closure {
 function f;
 environment;
}
) (interpreter's recursive definition (accepts two parameters, expression exp and environment env))

;; explanation of interpreter's recursive definition (accepts two parameters, exp expression and env environment)

;; there are 5 cases (variable, function, binding, call, number, arithmetic expression)

[1. Variable:
env (variable 'x)
(if (assoc 'x env)
(cdr (assoc 'x env))
(error "undefined variable x"))]

[2. Function:
(function-call (car exp) env)
(cons 'function (cons (list 'function-name (car exp)) (cdr exp) env))]

[3. Binding:
(binding-expression (car exp) (cadr exp) env)
(cons 'binding (cons (list 'binding (car exp) (cadr exp)) env))]

[4. Call:
(apply (car exp) (cdr exp) env)
(cons 'call (cons (list 'call (car exp) (cdr exp)) env))]

[5. Number:
(number (car exp))
(cons 'number (list (car exp) 0) env)]

[6. Arithmetic Expression:
(arithmetic-expression (car exp) (cadr exp) env)
(cons 'arithmetic-expression (cons (list 'arithmetic-expression (car exp) (cadr exp)) env))] (define (interp 
 (lambda ([func arg] 
 (func arg))) 

This is a Lisp-style definition of an interpreter function. The interpreter takes a function and an argument as inputs and applies the function to the argument.match
expressionexp

This appears to be a fragment of code written in the Lisp programming language. The English translations of the given Chinese characters are as follows:

- `exp`: expression
- `env`: environment
- `match`: pattern matching.

So, the English translation of the given Chinese text would be:

expression environment match expression.

This suggests that the code is defining or using a function with the name `match` that performs pattern matching on expressions within an environment. Match pattern to exp

(
?
 symbol
 x var

(function() {
// function declaration
// v is the variable name

var v;

})(); look up environment

This text appears to be written in Python syntax, with "lookup" being a function name, "x" being a variable name, and "env" being a list or dictionary name. The square brackets and parentheses are used for defining and calling functions or accessing elements in lists or dictionaries in Python. The text seems to be encouraging the execution of the "lookup" function with argument "x" in the context of the "env" environment or dictionary. if (not condition) {
// code block for when condition is false
}

In English, this is a conditional statement in JavaScript or a similar programming language. The statement checks if the condition is false, and if it is, the code block within the curly braces will be executed. "Error: undefined variable x" Else,

Empty,

If,

Question mark.

This text appears to be a fragment of code written in a programming language such as Python or JavaScript, but without additional context it is difficult to determine the exact meaning or purpose of this code snippet. The English translation provided is based on the given text alone, and does not include any Chinese characters or punctuation. number (or) digit(s) (lambda x:)

This is a Lambda expression in Python syntax. It takes one argument, x, and does not have a body or statement to execute. Function (Closure)

This text appears to contain Chinese characters representing the English words "Function" and "Closure," likely in the context of computer programming. The parentheses and semicolon are common in programming languages for denoting function definitions or calls. However, without the specific context or the exact Chinese characters used, it's impossible to provide a completely accurate translation. The provided English translation is based on the given context and the visible English text. let // This is likely an incomplete fragment of Lisp or Scheme code. The English translation would be something like:

(let // Begin let binding
[ // Begin list of bindings
env // Variable name: environment
exp // Variable name: expression
] // End list of bindings
// The rest of the code would follow here, but it's missing in the provided input. [x, e1,
 e2]

In English, this would be represented as a list with three elements: [x, e1, e2]. bond (v1)

In this context, "绑定" (biáo dìng) translates to "bond" in English. The parentheses and brackets are likely used for programming or coding purposes, so I have included them in the translation as well. The "v1" inside the square brackets likely represents a variable or value in a programming context. (interpreter

e1

environment)

This text appears to be enclosed in parentheses and contains three English words: "interpreter," "e1," and "environment." The first word, "interpreter," refers to a person or software that translates or explains something, while "e1" is likely a variable or identifier used in a programming context. The last word, "environment," refers to the surrounding conditions or context in which something exists or operates. imperative form of the verb "to be" (e.g., "be," "am," "is," "are," "have been," "had been")
ext-env
variable x empty environment or context

This text appears to be written in a programming or scripting language syntax, likely Lisp or Scheme, but it does not contain any meaningful Chinese characters. The text represents an empty environment or context in the programming language. call

let[v1
 (interpret
 e1
 env)
]

This is likely a Lisp-like code snippet. The English translation would be:

[v1
 (interpret e1 env) ]

This means to interpret the expression `e1` in the environment `env` and assign the result to `v1`.2. (Interpretation of) e2:

This text appears to be a portion of code or programming script, likely written in a markup language such as XML or JSON. The English translation of the text would depend on the specific context and meaning of the variables and functions used. However, based on the given text, it seems to be a comment or instruction for interpreting or executing the code represented by the "e2" variable. Without further context, it is impossible to provide a precise English translation. envelop (v1)
match[Closure

(lambda (x)
]

[Anonymous function (x) - Lambda expression in Scheme or similar functional programming languages] env-save // environment variable save

This text appears to be a simplified Chinese representation of the English phrase "environment variable save". The characters "env-save" are likely a transliteration of the English words into Chinese characters.i. interpretation
ii. external environment

Note: This is an approximation based on the context provided. The given text appears to be fragmented and may not form a complete sentence or phrase in either Chinese or English. env-save
)))))

[
(
,op e1, e2 - arithmetic expression

Explanation:
The given Chinese text appears to be a comment written in Simplified Chinese. It describes that the following code segment contains an arithmetic expression, represented by the variables e1 and e2. let [v1]
(interpret [interp]) envelope (or envelope symbol)
v2 (version 2) interpreter
e2 is
enviro
)]) match

Based on the given context, it seems like this text is fragmented and incomplete, likely meant to represent code snippets in English. The translation above is an attempt to make sense of the given Chinese characters based on their context and the provided English words.

The first line, "interpreter e2 is," suggests that "e2" is a reference to a specific interpreter. The second line, "enviro," appears to be a misspelled version of "environment," implying that it might be describing the environment for the interpreter. The last line, "match," could be a command or instruction for the interpreter to perform a comparison or pattern matching operation. However, without more context, it's difficult to be certain of the exact meaning of this text. op (
+ [
+

This text appears to be invalid or incomplete Chinese characters. It's likely that some characters are missing or incorrect. Without a complete and valid Chinese text, it's impossible to provide an accurate English translation. I.

II.

(

This text appears to be in a format of a document or a code, with Chinese characters missing. Without the Chinese characters, it's impossible to provide an accurate translation. However, based on the structure, it seems like there are two sections or versions labeled as "v1" and "v2". The text in parentheses may represent some additional information or instructions for the sections. I
II

Note: The given Chinese text seems to be in an incomplete or incorrect format, as it only contains some square brackets and asterisks. The provided English translation is based on the assumption that "v1" and "v2" are intended to be placeholders for the Chinese text that is missing. I.

v1

II.

v21 version 1
//////////////////////////
//////////////////////////
2 version 2 Interpreter's "user interface" function. It wraps interp, hiding the second parameter, initially set to env0.

(define
r2

(lambda (interp)
(lambda (x)
(interp x env0)))) lambda expression
( interpretation

In English, this would be written as:

lambda expression
( interpretation

So, the translation of the given Chinese text to English would be:

lambda expression interpretation this is some test cases:

(
r2
) 1 + 2 * 3
;; => 7

Translation:
The expression inside the parentheses is evaluated first, which results in 1. Then, the multiplication operation is performed, giving 2 * 1 = 2. Lastly, the addition operation is carried out, resulting in 1 + 2 = 3. However, the semicolons in the input text are not valid in this context and should be removed. The correct expression should be: 1 + 2 * 3.

Therefore, the translation is:
1 + 2 * 3
=> 7 (The result of evaluating the expression) r2
'
[
*
2

Translation:
r2 - prime number 2
' - apostrophe
[
* - asterisk
2 - number 2. 3) => 6

( r2
'
(

This text appears to be a mix of Chinese characters and programming code. The Chinese characters "三" (three) and " => " (becomes) are visible, along with some parentheses and a semicolon that are commonly used in programming languages. However, without additional context, it's difficult to provide an accurate translation or interpretation.

Assuming the semicolon is part of the programming code and not Chinese, the text could be interpreted as follows:

In Chinese: 三 => 六 (three becomes six)
In code: 3) => 6

This suggests that the Chinese text is describing a programming concept, possibly a variable assignment or function call, where the value of "three" is being replaced with the value "six". The code interpretation is a shorthand representation of this concept using parentheses and a semicolon to denote function call syntax. Two plus three is seven.

However, the given Chinese text does not seem to contain any meaningful information. The parentheses and the "+" symbol do not have any significance in this context.; Semicolon (;) => 14

(
r2
'
(
*
[

; A semicolon (;) is used to separate multiple statements in a single line in some programming languages, such as JavaScript. In this case, there are 14 semicolons in the given text.

r2 refers to a variable or a function named "r2". The exact meaning depends on the context.

The single quote (') is used to denote a string literal or a character literal in some programming languages.

The opening parenthesis (() and the asterisk (*) suggest a comment or a multi-line comment, depending on the programming language being used. The closing parenthesis and the square bracket [ are also used for different purposes in various programming languages.

Therefore, it is difficult to provide an accurate English translation without more context. The provided text appears to be a snippet of code or a comment in a programming language. (Bracket 1)
1
2

(Bracket 2) Three 4 double parentheses
;; => twenty-one

(

Here is the English translation without any Chinese characters or punctuation:

Three Four double parentheses
=> twenty-one (lambda x [
 
 
])

This is a Lambda expression in Scheme programming language. It defines an anonymous function that takes one argument 'x' and does not have any body or code inside it. two x's
three triple parentheses; semicolon, no translation needed
;; => 6

(
r2

'
(
let
// This is a Lisp-style code, likely written in Scheme or similar language.
// The translation would depend on the specific implementation and context.
// However, based on the given code snippet, it seems to define a let binding with one variable 'r2' and no initial value, and the rest is not provided.
// So, the English translation would be:

let r2 ;; uninitialized variable

// or, if you want to provide a placeholder value for r2, you could use:

let r2 #f ;; or any other value as a placeholder, such as 0 or nil.[
[
let
]

2
]

This text appears to be an incomplete and formatted code snippet written in the JavaScript programming language. The English translation of the code would be:

[
[
let
]

2
]

This code defines an empty array, initializes a variable named 'let' with no value, and then assigns the number 2 to that variable. However, since 'let' is a reserved keyword in JavaScript, it cannot be used as a variable name directly. Instead, you should use a different variable name for your code to function properly. (lambda y)

This is a Lambda expression in parentheses in Scheme or other Lisp-family programming languages. It defines an anonymous function that takes one argument, y.x, y in parentheses and brackets, multiplied by each other, repeated and enclosed in parentheses and brackets multiple times.

Translation:

xy in parentheses and brackets, multiplied by each other, repeated and enclosed in parentheses and brackets multiple times. three sets of parentheses containment, result is six

(
r2 (function (x) {
  // function body here
})(2); // pass argument '2' to the function. (let
[(lambda [f])
...]
...)

This is a Lisp-style code snippet in Chinese, where `let` is a binding construct used to introduce new local variables, and `lambda` is a function definition construct. The square brackets `[` and `]` are used to delimit the arguments of the `lambda` function. However, the code snippet is incomplete as it lacks the body of the `let` binding and the `lambda` function.1 star
or
5 persons. let x = 4; // or: x is assigned the value 4. The given text is not a valid Chinese character sequence. It appears to be a combination of English letters, digits, and parentheses. The semicolon (;) and the arrow (=>) are also not valid Chinese characters.

Therefore, there is no valid Chinese text to translate to English. In the following sections, let's take a closer look at the different parts of this interpreter.

### Interpreting Basic Arithmetic Operations

Arithmetic operations are generally the most basic constructs in a program and cannot be further divided into multiple steps, so let's first look at how arithmetic operations are handled. Here is the part of R2 interpreter that handles arithmetic, which is the last branch of interp.

(

Translation:

In the following sections, we will examine the different parts of this interpreter in detail.

### Handling Basic Arithmetic Operations

Arithmetic operations are the most fundamental constructs in a program and cannot be further broken down into smaller steps, so let's start by looking at how arithmetic operations are processed. The following is the part of the R2 interpreter responsible for arithmetic, which is the last branch of interp.

( match
exp

(Note: The given Chinese text seems incomplete as it only contains a few characters.) op e1 e2

This appears to be a fragment of code written in a programming language like Python or JavaScript, possibly incomplete or missing some context. The Chinese characters do not seem to correspond to any recognizable words or phrases in the Chinese language. Therefore, it is impossible to provide an accurate English translation without additional context. let [v1]

This is likely an incomplete or fragmented piece of code written in the Lisp programming language. The English translation of the given Chinese text would be:

let [v1]

This means that a variable named 'v1' is being defined or assigned a value in the Lisp programming language. interp recursive call, get value of e1

function interp:
e1 = e1 // function call to interp for e1, get its value

env:
// function definition or declaration of env, no English translation provided in the text.2

(interpret
 
e2
 
env
)])

Interpret e2 in env. Recursively call interp for myself to get the value of e2.

(
match

op

; Branch: handle the 4 cases of operation op
[

Recursively call interp for myself to get the value of e2.

(match

op

; Branch: handle the 4 cases of operation op
[

Recursively call interp with the current context to evaluate the right expression and get the value of e2.

(define (interp context e)
; Interpreter function for the given context and expression e
(cond ((number? e) e) ; if e is a number, return it
((symbol? e) (lookup context e)) ; if e is a symbol, look up its value in the context
((op? e) (apply-op context (interp context (car e)) (interp context (cadr e)))) ; if e is an operator, apply the operation on the values of its operands
(else (error "Invalid expression"))) ; if e is neither a number, symbol nor an operator, throw an error

; Apply the given operation op on the values x and y
(define (apply-op context x y op)
(cond ((eq? op '+) (+ x y)) ; if op is '+, return the sum of x and y
((eq? op '-) (- x y)) ; if op is '-, return the difference of x and y
((eq? op '*) (* x y)) ; if op is '*, return the product of x and y
((eq? op '/) (/ x y)) ; if op is '/, return the quotient of x and y
(else (error "Invalid operator")))

; Given context and expression to evaluate
(interp (make-empty-context) '(+ x y)) ; evaluate the expression '(+ x y) in an empty context

; Output the result
(display (interp (make-empty-context) '(+ x y)))
(newline) plus
(
plus
 v1 if it is a plus sign, output result as (v1 + v2)

In other words, if the symbol is '+', then the output should be the sum of the two variables (v1 and v2). if it is a minus sign, multiplication sign, or division sign, process similarly

       
[or]

if it's a minus sign, multiplication sign, or division sign: process similarly. *
(
*
 v1
 v2
)

Translation:

* comment 1
(
* comment 2
 v1 variable 1
 v2 variable 2
)

Explanation:

The given Chinese text appears to be a code snippet written in a markup language like Markdown or Jupyter Notebook. The text contains two comments marked with '*' and two variables named 'v1' and 'v2' enclosed in parentheses. The English translation is provided as a textual representation of the code snippet with comments and variable names in English. Slash, open parenthesis, forward slash, version one, close parenthesis. You can see that it is almost identical to the calculator written before, the only difference being an additional parameter "env" in the call to interp. This env is called "environment", which we will talk about soon.

### Interpretation of numbers

The interpretation of numbers is simple, just return them unchanged.

[(? number? x) x]Variable and Function

Variables and functions are the most complicated parts in an interpreter, so let's take a closer look.

The emergence of variables, one of the greatest breakthroughs in mathematical history, is essential for the implementation of functions. For instance, in the mathematical function f(x) = x * 2, x is a variable that transfers the input value into the function body x * 2. Without variables, functions would not be possible.

The most fundamental operations on variables are their "binding" (binding) and "evaluation" (evaluate). What is binding? Using the function f(x) as an example, when we call f(1), the x inside the function body is equal to 1, so x * 2 equals 2. When we call f(2), the x inside the function body is equal to 2, so x * 2 equals 4. In this case, the function f was bound twice, with x being bound to 1 the first time and to 2 the second time.

You can understand "binding" as this action: just like when you plug the plug into an electrical outlet. The plug's prong is x in f(x), while the x in x * 2 is the other end of the wire. When you plug the plug into the outlet, the current flows through this wire to the other end. If the wire conducts electricity well, the voltages at both ends should be equal. Environment

Our interpreter can only handle tasks one step at a time. For instance, when it needs to find the value of f(1), it breaks down into two steps:

1. Bind x to 1, so that the function body can see this binding.

2. Enter the function body and evaluate x * 2.

This is similar to a person performing these two actions: 1. Plug the plug into the outlet.

2. Measure the voltage at the other end of the wire and multiply the result by 2.

How do we remember the value of x between step 1 and step 2? By using what is called "environment"! We record the variable values in the environment and pass them into the variable's "visible area". The visible area of a variable, which is called its "scope" (scope), handles this in our interpreter.

Here's the code for handling the environment in our interpreter:

;; Empty environment
[
] (define (extend-env env x v)
;; Extend environment env, map x to v
(cons x v (cons 'frame env))) (define
 ext-env

 (lambda
 [])
)

English translation:

(define ext-env
 (lambda ()
))x is void, v is a verb, env is an environment.

Therefore, the English translation without any Chinese characters or punctuation would be:

void verb environment.con
x,
.
, with
v get-value. Look up value of x in environment variable 'env'

(define look up
(lambda (x env)
...
)

This is likely a Lisp-style function definition in Chinese characters. The English translation would be "look up" as a verb, meaning to search for information. The function definition is an anonymous function that takes one argument `x` and an environment `env`, but the body of the function is missing. let (p) {
  // code block for variable p
}

// function declaration with one parameter pasq:

function:
(lambda (x)
(cond ((assq x env) t)
(t nil)))

;; This is a Lisp function definition in Chinese characters. The English translation is:

; asq:
; (defun asq (x)
; (cond ((assoc x env) t)
; (t nil)))

; This function, named "asq", checks if the given variable "x" is in the environment "env". If it is, the function returns "t" (true). Otherwise, it returns "nil" (false).[Not a valid Chinese character sequence. It appears to be a combination of English letters, parentheses, and a hash symbol, which do not have direct translations into Chinese characters.] Else,
(cdr p)

This appears to be a Lisp-style code snippet in Chinese characters. The English translation is provided above. Here we use a simple data structure, Scheme's association list, to represent the environment. An association list looks like this: ((x . 1) (y . 2) (z . 5)). It is a pair list, with the left element being the key and the right element being the value. In simpler terms:

((
x
.
1
)
[
[
y
.
2
]
[
z
.
5
]
]) two dots or commas

This text does not contain any Chinese characters that can be translated into English words. The symbols "y" and "." are not Chinese characters, but rather English letters and punctuation marks, respectively. The text consists only of two dots or commas. I. Table lookup operation is a search from beginning to end. If the key on the left is the variable to be found, return the entire pair. Simple enough? Inefficient but sufficient for our current task. Extend the environment function adds an environment. For instance, if the initial environment env1 is ((y . 2) (x . 1)), then (ext-env x 3 env1) will return ((x . 3) (y . 2) (x . 1)). This means that (x . 3) is added to the front of env1.

When do we need to extend the environment? We need to extend the environment during binding. Binding can occur during function calls or during let bindings. We have chosen this data structure to naturally give environments the properties of a scope.

Environments are actually a stack. Bindings in inner scopes will appear at the top of the environment, which is "pushing onto the stack". This way, when we look up variables, we will first find the one defined in the inner scope.

For example:

(let ((x 3) (y 4) (f (lambda (z) (+ x y z))))
(f 2))

In this example, when we evaluate (f 2), the environment stack will look like this:

((x . 3) (y . 4) (f . (lambda (z) (+ x y z))) (z . 2))

When we evaluate the body of the lambda function, the environment stack will look like this:

((x . 3) (y . 4) (z . 2))

When we evaluate (+ x y z), we will first find z in the current environment, then x and y. So the result will be 3 + 4 + 2 = 9. let x = 1;
// assign value 1 to variable x.(function () {
  var y = [];
  let i = 2;
})(); binding y 2.

(let
 ([x 3])
 ...)

The above Chinese text translates to the following English code snippet:

(bind y 2.
 (let ([x 3])
 ...))

This code snippet is written in Scheme programming language. The Chinese text describes the following actions:

1. Define a variable `env` with a value of `((x . 1))`.
2. Bind the variable `y` to the value `2`.
3. Define a local variable `x` with the value `3`.

So, the English translation of the Chinese text would be:

bind y 2.
(let ([x 3])
 ...)

Or, in a more readable format:

(bind y 2)
(let ((x 3))
 ...) binding x to 3.

(add x)

In this context, it seems like this is a Lisp-style code snippet. The first line is defining a list `env` with two elements, where the first element `y` is bound to the number 2, and the second element `x` is bound to the number 1. The second line is binding the variable `x` to the value 3. The third line is adding the value of `x` (which is now 3) to the result of the previous expression. However, since there is no output or return statement in this code snippet, it's unclear what the final result would be.; environment = ((x . 3) (y . 2) (x . 1)) .
; find x, get 3; find y, get 2.

;; => 5

This code returns 5. This is because the innermost binding places (x . 3) at the front of the environment, so when we look up x, we first see (x . 3) and return its value 3. The (x . 1) that was previously put in is still there, but we overlook it.

This does not mean that (x . 1) can be rewritten or discarded, as it is still useful. A slightly different example will show you how this works:
[(x . 1) (x . 3)] .
; find x, get 3.

;; => 1.

In this case, the innermost binding of x overwrites the previous one, so when we look up x, we get the value 3 instead of 1.[Function (
x // parameter
) {
// function body
}
]// anonymous function. bond x to 1.

(
(define
(
[
[
[bind]
x 1]
]
]
)
)
)
)

In English, this code snippet is defining a function `bond` that takes a single argument `x` and binds it to the value 1. The function uses a combination of parentheses and let/define statements to accomplish this in Scheme, a dialect of Lisp. The English translation of the Chinese text should convey the same meaning. (setf env (cons (list 'x 1) env)) ; bind x to 1 in environment.

x: env = ('(x . 2) (x . 1)) .
; find x, get 2.

x
)

;;; :env = ('(x . 1)) .
; find x, get 1.

;;; => 3
; two different x's sum, 1+2 equals 3. This example returns 3. It is the sum of the two x's in the third and fourth lines. Since the x in the third line is in the inner let, its environment is ((x . 2) (x . 1)), so finding the value of x results in 2. The x in the fourth line is in the outer let but inside the outermost let, so its environment is ((x . 1)), resulting in a value of 1. This is consistent with intuition, as x is always found in the innermost definition.

It is worth noting that the environment is extended to form a new environment, but the original environment remains unchanged. For instance, the ((y . 2) (x . 1)) in the example has not been deleted or modified; it has just been "referred to" in a larger list.

These data structures that do not modify existing data are called "functional data structures." Functional data structures generate new data without changing or deleting old data. They may reference old structures, but they do not modify old structures. This "immutable" property is important in our interpreter because when we extend an environment, enter recursion, and return, the outer code must still be able to access the original outer environment.

Of course, we could also use more efficient data structures (such as balanced trees or chained hash tables) to represent environments. If you are familiar with such concepts, you could even represent environments using functions. In this case, for the sake of simplicity in the code, we chose the most basic, yet correct, understandable data structure. I have understood variables, functions, and environments. Now let's look at how an interpreter handles a "lookup" operation on a variable, which is the first kind of situation for the `match`.

[(? symbol? x) (lookup x env)]

This is looking up the value of a variable in the environment, following the "scoping order" from inner to outer.

Here, (? symbol? x) is a special pattern. It uses the Scheme function `symbol?` to check if the input is a symbol. If it is, then it binds it to `x`, allowing you to use `x` to refer to this input on the right side.

### Interpreting Bindings
[
[symbol? x]
(lookup x env)]

This checks if `x` is a symbol, and if so, performs a lookup in the `env` for the value associated with that symbol. In this post, let's examine the explanation of let binding:

```javascript
(
let
  [
  ,x
  ]
)
``` e1,
e2)

This text appears to be a list with two items, each represented by a pair of parentheses containing an identifier (e1 and e2). let
[
v1
(
interp
e1
)
]

This is likely a Lisp-like code snippet. The English translation would be:

let
[
v1
(
interp
e1
)
]

Let:
[assign the value of e1 to variable v1] Explanation of the right expression e1, getting value v1

(
interp // interp function call
) e2,
ext-env,
x,
v1,
env. I. Expanding `(x . v1)` to the environment top and evaluate e2:

From the code comments, you might have already understood what it is doing. We first evaluate e1 to get v1. Then we expand `(x . v1)` into the environment, so that all inner parts of `(let ([x e1]) ...)` can see the value of x. We then use this expanded environment to recursively call the interpreter itself, to evaluate the body e2. Its return value is the value of this let binding.

II. Lexical Scoping and Dynamic Scoping

Before discussing function definition and call, let's first understand the subtle concept of "scoping" rules. Functions may contain variables from the outer layer, called "free variables." So, before analyzing function code, let's learn about different "scoping" rules.

Lexical scoping, also known as static scoping, is a rule that determines the accessibility of variables based on their position in the program's source code. In other words, the variable's scope is determined at compile time, and the variable can only be accessed from within the block where it is defined.

Dynamic scoping, on the other hand, is a rule that determines the accessibility of variables based on the order of execution or the call stack. In this approach, the variable's scope is determined at runtime, and the variable can be accessed from any enclosing lexical scope that has been active during the execution of the current function call.

In functional programming languages, lexical scoping is more commonly used due to its simplicity and predictability. However, dynamic scoping can be useful in certain situations, such as implementing certain types of closures or implementing certain types of dynamic binding.

In the context of the code you provided, the let binding and the interpreter's behavior are based on lexical scoping. This means that the value of x in the body of the let expression is the value that was bound to x in the let expression itself. The interpreter uses the lexically scoped environment to look up the value of x, and this value is then used in the evaluation of e2. In this example, what should the value be for the following code snippet?

(
let
([
x 2
])
...)

Answer: The value of `x` is 2. (let
(function (
[f]
(lambda

This text appears to be a fragment of Lisp or Scheme code written in Chinese characters. Here's the English translation:

(let
(function (
[f]
(lambda

This translates to:

(let
(function (f)
(lambda

In English, this code defines an anonymous function that takes one argument, `f`, and returns another function as its result. The inner function takes no arguments and simply returns the value of `f` that was passed to the outer function.

Therefore, the translation in English without any Chinese characters or punctuation would be:

(let (function (f) (lambda))
(function (f) f)m empty star x[Function (let [x]) {
// body of the function goes here
}]
)

In this context, the Chinese text seems to represent a Lisp-like function definition in code format. However, without the body of the function, it's impossible to provide an accurate English translation. The provided text only shows the function definition's header, which includes the keyword "let" and a variable named "x" inside a list. four open parentheses
(
f
 
three close parentheses
))))

In English, the translation would be: "four open parentheses (, (, ), ) three close parentheses" or simply "four open parentheses and three close parentheses". In this place, the x in the body of the f function (lambda (y) (* x y)), is a "free variable". x is not this function's argument and is not defined in this function, so we need to find x's value outside the function.

In our code, there are two bindings for x, one equals 2, the other equals 4. So, which binding should x point to? This may seem irrelevant, but when we call (f 3), a serious problem arises. The function body is (* x y), we know y's value comes from parameter 3, but what is x's value? Should it be 2 or 4?

Historically, this code may have had two different results, which continues to this day. If you write the above code in Scheme (Racket), its result is 6.

;; Scheme

(let ((x 2)
      (f (lambda (y) (* x y))))
  (f 3))[Empty array]

(
let
[
-- No translation needed as the given text is already in English. It's a Lisp-like code snippet written in parentheses, and it declares a variable named 'let' with an empty array as its value.[Function (y) {}]

This is a lambda function expression in Lisp-like syntax. The English translation would be:

[Function (y) {}]

or

(function (y) {})

This is a self-contained anonymous function that takes one argument, 'y'. The function body is empty. xy in parentheses, repeated and nested multiple times.

There seems to be a mistake in the input as it only contains brackets and spaces, without any actual Chinese characters or text. Therefore, it is not possible to provide a translation in this case. let [x = 4]

This is a JavaScript-like code snippet in the form of a template literal. The English translation would be:

let x = 4. At present, let's see what result we get by inputting equivalent code in Emacs Lisp. If you are not familiar with Emacs Lisp usage, you can follow me: input the code into Emacs's buffer named *scratch*. Place the cursor at the end of the code and press C-x C-e. In this way, Emacs will execute this code segment, and the result will be displayed in the minibuffer:

;; => 6: The result is 12! If you bind the innermost x in the code to other values, the output will change accordingly.

Strange, isn't it? Scheme and Emacs Lisp, what exactly are the differences? In fact, these two seemingly similar "Lisp dialects" have adopted completely different scoping methods. Scheme's method is called lexical scoping (or static scoping), while Emacs Lisp uses dynamic scoping.

Which one is better? Or does it matter which one is used? The answer is, dynamic scoping is a terribly wrong approach. History has taught us that it brings about countless mysterious bugs, making dynamic scoping languages almost unusable. Why is that?

The reason lies in the fact that bindings like (let ((x 4)) ...) should only affect the value of the internal x that can be seen. When we see (let ((x 4)) (f 3)), we don't see any variable named "x" in the let's interior, so we intuitively believe that the binding of x in (let ((x 4)) ...) should not affect the result of (f 3).

However, our intuition is wrong for dynamic scoping. The reason being, f's function body contains an x, even though we don't see it in the (f 3) call, it exists in the definition of f. Keep in mind, f's definition might be several hundred lines of code away, or even in another file. And why should the person calling the function know that f's definition contains a free variable named x? Therefore, dynamic scoping, from a design perspective, is a counter-intuitive design :).m oppositely, lexical scoping is intuitive. Although we bind x to 4 in (let ((x 4)) (f 3)), f's function body is not defined there, and we don't see any x in it, so the x in f's function body still refers to the one we defined it with, which is the one at the top (let (*x 2*) ...), with a value of 2. Therefore, (f 3) should have a value of 6, not 12.

### Explanation of the function

To implement lexical scoping, we need to make functions into "closures" (closures). A closure is a special data structure consisting of two elements: the function definition and the current environment. We define closures as a Racket struct:

(
struct
Closure
[
env
proc
]
) With this data structure, our interpretation of (lambda (x) e) can be written as follows:

[ [function x body e] ] (lambda x: e) Closure expression environment.

In programming, a closure is a function that has access to its own scope, and any outer function's scope, even after the outer function has completed execution. This allows the inner function to access and manipulate variables from the outer function, even if the outer function is no longer in scope. The "exp" and "env" likely refer to the expression and environment associated with the closure. I. Attention here, the 'exp' in this place is `(lambda (x) e)` itself.

Interestingly, our interpreter does almost no computation when it encounters (lambda (x) e). It merely wraps this function and puts it along with the current environment into a data structure (Closure). This closure records the environment we can see at the location of function definition. Later when we call the function, we can get the values of the free variables in its body from this closure's environment.

### On the Call

Finally, we have reached the climax, the function call. For clarity, we copy the code for function call below:

[
[car (f x)]

To execute this call, our interpreter performs the following steps:

1. Look up 'f' in the current environment to find the closure.
2. Get the environment from the closure.
3. In the environment, look up the binding for 'x'.
4. Substitute 'x' with the value found in step 3 into the body of the function.
5. Evaluate the resulting expression.

So, the interpreter effectively performs a series of substitutions and evaluations to execute the function call. (
e1

,
e2
)

The text appears to be an empty parentheses with two variables e1 and e2 inside. Therefore, there is no actual translation as the text does not convey any meaningful information in English. let (
interpreter

e1
) Calculate the value of function e1

v2 Calculate the value of parameter e2

Here's the English translation of the given Chinese text without any Chinese characters or punctuation:

calculate parameter e2 value.1. Match:

1.1. Closure:

Function that retains access to its own scope, even when it is called from another function. In functional programming, a closure is a function that has access to its own lexical environment, which includes any variables declared in the outer function, even if that outer function has already completed execution. This allows inner functions to access and manipulate variables from their outer context. (lambda x: e)

This is a Lambda expression in Python syntax. It takes one argument 'x' and returns the value of 'e' after performing some computation with 'x'. env-save:
; extract various sub-structures in closure using pattern matching

(interp:
) ext-env
x v2
env-save In the environment env-save, bind x to v2 in the function body

Functions are called in the form of (e1 e2), where e1 is the function and e2 is its argument. We first need to determine the values of the function e1 and argument e2.

Function call is like plugging an appliance's plug into an outlet to make it work. For example, when (lambda (x) (* x 2)) is applied to 1, we bind x to 1 and then interpret its function body (* x 2). However, there is a problem here: what should the value of the free variable be in the function body? From the discussion of the closure, you already know that the value of the free variable should be queried from the closure's environment.

The value v1 of the operands e1 is a closure, which contains the environment saved when the function was defined. We take this environment env-save out and can query it to get the value of the free variable in the function body. However, the function body not only has free variables but also uses the function argument, so we need to expand this env-save environment by adding the value of the argument. This is why we use (ext-env x v2 env-save) instead of just env-save. You might find it strange that the interpreter's environment env is not used here? Yes. We use env to calculate the values of e1 and e2 because the variables in e1 and e2 are visible in the "current environment" (env). However, the function definition, in the current environment, is not visible. Its code is in another place, and the environment where it is visible is saved in closed environment env-save. So we take out the closed environment env-save from v1 and use it to compute the value of the function body.

Interestingly, if we use env instead of env-save to interpret the function body, our language would become dynamic scoping. Let's experiment a bit: you can change env-save to env in (interp e (ext-env x v2 env-save)) and try the code we discussed earlier. Its output will be 12. That's what we discussed before: dynamic scoping results.

(
r2

'
(
let
[v1
(lambda (x)
(let
[env-save (copy-env env)]
(list
(interp e1 env)
(interp e2 (ext-env x v2 env-save))))]
(interp e (ext-env x v2 env-save))))

In English:

You might find it strange that the interpreter's environment env is not being used here? Yes. We use env to calculate the values of e1 and e2 because the variables in e1 and e2 are visible in the "current environment" (env). However, the function definition, in the current environment, is not visible. Its code is in another place, and the environment where it is visible is saved in closed environment env-save. So we take out the closed environment env-save from v1 and use it to compute the value of the function body.

It's worth noting that if we use env instead of env-save to interpret the function body, our language would become dynamic scoping. Let's experiment a bit: you can change env-save to env in (interp e (ext-env x v2 env-save)) and try the code we discussed earlier. Its output will be 12. That's what we discussed before: dynamic scoping results.

(r2

'
(let
[v1
(lambda (x)
(let
[env (copy-env env)] ; instead of env-save
(list
(interp e1 env)
(interp e2 (ext-env x v2 env))))]
(interp e (ext-env x v2 env)))) [empty array]

function
let [_, two] = ... // destructuring assignment, assigning the first element to an unused variable (_) and the second element to the variable 'two'[Function (y) {
// function body here
}]

This is likely a fragment of Lisp or Scheme code written in Chinese characters. The English translation would be:

[Function (y) {
// function body here
}] xy in parentheses, repeatedly enclosed in brackets

This is a rough translation as the given Chinese text seems to be a series of symbols without clear context or meaning. The text appears to represent the characters "xy" enclosed in parentheses, which are then enclosed in brackets multiple times. let [x]: number[] = [4]; // or let x: number[] = [4]; depending on the intended variable name. You might have found out that if our language was dynamic scoping, we wouldn't need closures anymore since we wouldn't need the environment saved in closures. Thus, a dynamic scoping interpreter could be written as follows:

[f
3
)))))

;; => 12

This text appears to be a mix of Chinese characters and Lisp-like code. The Lisp-like code translates to "set f to the function that returns 12" or simply "f -> λ()->12". The Chinese text above it seems to be discussing the concept of dynamic scoping versus static scoping and how dynamic scoping eliminates the need for closures. (define (interp 
 (lambda ([func arg] 
 (func arg))) 

This is a Lisp-style definition of an interpreter function. The function takes another function (`func`) and an argument (`arg`) as inputs, and applies the function to the argument. The interpreter function itself is defined as a lambda function.match
expression I. Introduction

II. Background
A. Overview of the Chinese Education System
B. Importance of English Language Education
C. Current Status of English Language Education in China

III. Challenges in English Language Education in China
A. Lack of Native Speaker Teachers
B. Limited Resources
C. Large Class Sizes
D. Cultural and Psychological Factors

IV. Solutions to Improve English Language Education in China
A. Increase Investment in Education
B. Recruitment of Native Speaker Teachers
C. Use of Technology in Teaching
D. Curriculum Reforms
E. Encouraging English Language Use in Daily Life

V. Conclusion

VI. References

VII. Appendices
A. List of Abbreviations
B. List of Figures
C. List of Tables

VIII. Glossary

IX. Index

X. About the Authors.

This is a general outline of a research paper on English language education in China. The actual content of the paper would depend on the specific research question and data being presented. lambda function definition:

function x:
begin
e
end. function: directly returns itself as expression

...

exp

(Note: The Chinese text seems incomplete as it is missing context before and after the given code snippet.) (e1,
e2)

This appears to be a parentheses with two variables, e1 and e2, inside of it. The commas are optional in this context, as parentheses can be used to group expressions in programming languages. (let
[(v1
(interp)])

This is likely an incomplete or incorrectly formatted Lisp code snippet. The English translation without Chinese characters or punctuation would depend on the context and meaning of the code. Here's a possible interpretation based on the given code:

Let v1 be the value returned by the interpreter function. e1

environment
)

v2 interp e2 env

This text appears to be Lisp-style code with some missing or incorrect formatting. Based on the given text, the English translation would be:

interp e2 env Anonymous function:

if (arg1 === arg2):
then
# Code block to be executed if condition is true.

else
# Code block to be executed if condition is false. call: directly using the function expression itself

; function call: directly using the function expression itself. (interpret

ext-env
x)

In English, this text appears to be describing the use of an interpreter function with an external environment variable named "x". The interp function likely interprets or executes code, while the ext-env variable is a dictionary or environment in which the interpreter operates. The "x" is likely a value or key associated with this environment.2

env
))))]

...

...

Function 2

environment
))))]

...

... I notice that the interpreter's function is easy to implement, isn't it? It is just the expression of the function itself, unchanged. Using the function's expression itself to represent its value is a straightforward and common approach. However, this results in a language that adopts dynamic scoping unwittingly.

This is why many early Lisp languages, such as Emacs Lisp, use dynamic scoping. This is not because their designers deliberately chose dynamic scoping over lexical scoping, but because using the function's expression itself as its value is the most direct and common approach.

Furthermore, we also see the benefits of using "functional data structures" to represent the environment in this case. When a closure is called, its environment is extended, but this does not affect the original environment, and we get a new environment. Therefore, when the function call returns, the parameter bindings are automatically "deregistered."

If you use a non-functional data structure to bind parameters without generating a new environment and instead assign values to the existing environment, the assignment operation will permanently change the contents of the original environment. Therefore, you must delete parameter bindings when the function returns. This is not only cumbersome but also prone to errors in complex situations.: Ponder question: Some people may have seen lambda calculus, these people might know that (let ([x e1]) e2) is equivalent to a function call: ((lambda (x) e2) e1). Now comes the problem: In our discussion about functions and calls, we went into great depth about the difference between lexical scoping and dynamic scoping. Since let binding is equivalent to a function definition and call, why didn't we discuss the problem of lexical scoping and dynamic scoping during our earlier discussion about bindings, and why didn't we create closures?

### Limitations

Now that you have learned how to write a simple interpreter that can handle a fairly powerful functional language, for pedagogical reasons, this interpreter does not take into account practical requirements. Therefore, I point out some of its limitations.

1. Lack of necessary language constructs. Our language lacks some essential constructs that are necessary for practical languages: recursion, arrays, assignment operations, strings, custom data structures, ... As a foundational text, I cannot add all of these in. If you are interested in these, you can look at other books or wait for my future works.

2. Lack of error checking and reporting for invalid code. You might have noticed that the interpreter's match expressions assume all input is valid code, and they don't check for invalid cases. If you give it invalid code, it won't immediately report an error but will instead try to compute it, leading to strange consequences. A practical interpreter should include comprehensive checks for code format and report invalid code structures before running the code. 1. Inefficient data structures. The search for variables in an association list is linear in complexity. When a program has many variables, there are performance issues. A practical interpreter requires more efficient data structures. This data structure doesn't necessarily have to be functional. You can also use non-functional data structures (like hash tables), which, after certain modifications, can achieve the same properties but with higher efficiency.

Additionally, you can transform the environment into an array. Assign an index to every variable in the environment, and you can find its value in this array. If you represent the environment as an array, this interpreter takes a step towards the compiler.

2. Ambiguity problem with S-expressions. For teaching purposes, our interpreter directly uses S-expressions to represent syntax trees and performs branch traversal using pattern matching. In actual languages, this approach brings significant problems because S-expressions are a general data structure, and things represented by them look similar. When the syntax constructs of the program become numerous, directly pattern matching on S-expressions can cause ambiguity.

For example, (,op ,e1 ,e2) may seem to only match binary arithmetic operations like (+ 1 2). However, it can also match a let binding: (let ([x 1]) (* x 2)). This is because they have the same number of top-level elements. To eliminate ambiguity, you must carefully arrange the order of patterns, such as putting (let ([,x ,e1]) ,e2)'s pattern before (,op ,e1, e2). Therefore, the best solution is not to write an interpreter directly on S-expressions but to first write a "parser" that converts S-expressions into Racket's struct structures. The interpreter then performs branch matching on the structs. This way, the interpreter avoids ambiguity issues and gains efficiency improvements.

[Paid version]

To further optimize the interpreter, you can employ techniques like memoization, tail recursion, and static single assignment (SSA) form. Memoization can help avoid redundant computations by caching the results of function calls. Tail recursion allows the compiler to optimize recursive functions into iterative loops, which can improve performance and prevent stack overflow issues. SSA form ensures that each variable is defined once and only once in the program, which simplifies the analysis and optimization of the code.

Moreover, you can explore the use of just-in-time (JIT) compilation. JIT compilers translate and execute code at runtime, allowing for dynamic optimization and improved performance. This can be especially effective for interpreters working with complex or large programs, as it can provide significant performance gains by converting the interpreted code into machine code.

Lastly, consider implementing a garbage collector to manage memory allocation and deallocation automatically. This can help reduce the overhead of manual memory management and improve the overall efficiency of the interpreter.

By combining these techniques, you can create a more efficient and effective interpreter that can handle complex programs with ease. if you like this article, you can buy it at this place for a fee.