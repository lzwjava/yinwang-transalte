---
layout: post
title: "language-design-mistake1"
---

I often take pride in writing "very concise" code. Some people are very appreciative of this and then say they also enjoy writing concise code, and then go on to praise the clever design features of C language that allow for very concise code. I then realize that their idea of concise and mine are completely different.

My program's concise is based on semantics being clear and concepts being clear. On this foundation, I strive to eliminate redundant, convoluted, and confusing code, making the program more direct and efficient in expressing my mental "model." This is a form of optimization at the conceptual level, and the program's concise elegance is just one of its "appearances." Just like organizing a tangled mess of wires, it's not a matter of rolling them into a ball and putting them in a box. This approach will only bring more trouble and danger to future work.

So my concise is usually at the level of semantics and logic, not just in syntax. I will never sacrifice readability or error-proneness for the sake of making the program appear concise. On the contrary, many other people's pursuit of concise is haphazard and lacks principles. In many cases, these tricks are only on the syntax level, such as trying to combine two lines of code into one. This kind of "myopic pursuit of concise" error tendency has led to many design errors in languages and a breed of programmers who are proficient in using these errors.

Now I will give a few simple examples of "myopic pursuit of concise" language designs. Self-increment and self-decrement operations

In many languages, there are i++ and ++i for self-increment, and i-- and --i for self-decrement (hereafter referred to as "self-increment-decrement operations"). Many people like to use self-increment-decrement operations in their code because they can "save a few lines of code." However, the few lines saved are actually less valuable than the confusion and errors caused by such merging of read and write operations.

From a theoretical perspective, self-increment-decrement operations themselves are flawed designs. They combine the distinctly different operations of "read" and "write" without any clear distinction, leading to errors that are difficult to detect. Instead, a simpler, less elegant but clearer alternative, i = i + 1, is not only easier to understand but also clearer logically.

Some people care deeply about the difference between i++ and ++i, and investigate the meaning of expressions like (i++) + (++i). These investigations are futile. For instance, the difference in efficiency between i++ and ++i comes from the foolishness of early C compilers. Since i++ needs to return the original value of i after incrementing, it is actually compiled as:

(tmp = i, i = i + 1, tmp) In this kind of statement:
for (int i = 0; i < max; i++)

You don't actually need the value of i before the increment in i++. So some people suggest using ++i instead of i++ to avoid unnecessary assignment to a temporary variable tmp. However, a well-designed compiler should generate the same code for both situations. This is because in the i++ case, the code is actually transformed into:

for (int i = 0; i < max; (tmp = i, i = i + 1, tmp))

Since tmp this temporary variable is never used, it will be eliminated by the compiler's "dead code elimination". Therefore, the compiler eventually gets: I. For loop in Chinese:
for (int i = 0; i < max; i++)

II. Translation:
Therefore, "mastering" these subtle issues won't make you a good programmer. Many supposedly clever tricks are often due to early system design flaws. Once these systems are improved, these tricks become obsolete.

III. Correct Approach:
Instead, don't use increment or decrement operations, as they are inherently flawed designs.

IV. Assignments and Return Values:
A small example might have made you aware of the cognitive and time costs of pursuing short, concise code. Unfortunately, language designers continue to make similar mistakes. Some new languages have added numerous such features aimed at "shortening code" and "reducing typing," but in reality, these code shortcuts only waste your time, offering momentary excitement instead. In most languages similar to C, C++, Java, assignment statements can be used as values. This design is for enabling code like:

if (y = 0) { ... }

rather than

y = 0;
if (y) { ... } The program seems to have shortened a line, but this way of writing often leads to a common error: instead of writing if (y == 0) { ... }, some people accidentally leave out the = sign and write if (y = 0) { ... } instead. Many people make this mistake because the = sign in mathematics means "is equal to."

By mistake, a single character can cause a bug in the program. No matter what y's original value was, after this "condition," y's value will be changed to 0. This judgment statement will always be "false," and without making a sound, it changes y's value. This kind of bug is quite hard to discover. This is another example, illustrating the problem of pursuing brevity at the expense of appropriateness.

What is the correct way to do it? In a type-safe language, an assignment statement like y = 0 should not be able to return a value, so it doesn't allow you to write:

x = y = 0

or

[...] = 0;: If (y equals 0) { ... }

The working principle of this code is actually like this: after being parsed by the parser, it actually becomes x = (y = 0) (because the = assignment operator is "right-associative"). The expression x = (y = 0) means that x is assigned the value of (y = 0). Note that I'm talking about the value of (y = 0) as a whole, not the value of y. So here, (y = 0) has both side effects and a value, returning the "new value" of y.

The correct way is: y = 0 should not have a value. Its function should be "assignment" this kind of "action", not having any "value". Even if we forcefully say it has a value, its value should be void. In this way, x = y = 0 and if (y = 0) will be rejected by the compiler due to "type mismatch", avoiding potential errors.

Think carefully, x = y = 0 and if (y = 0) bring very little benefits but consume a lot of time and effort from many people. That's why I call them "little clever". 1. Question:

1. In Google's coding standards, curly braces are required to be written after both for statements and if statements, even when they only contain one line of code. For instance, you cannot write for (int i=0; i < n; i++) some_function(i); instead, it should be written as for (int i=0; i < n; i++) { some_function(i); } Analyze: Is it better to write two extra curly braces in this manner? (Hint: Google's coding standards are correct in this regard. Why?)

2. During my second internship at Google, I found that the code I had written for them a year prior had been restructured in many places. Almost all instances of the following structure: if (condition) { return x; } else { ... } 1. The following Chinese text translates to:

if (condition) {
 return x;
}
return y;

This code snippet omits an "else" statement and two brackets. The omission may lead to unintended consequences, as the "if" statement may not behave as intended without the "else" statement and proper bracketing. For instance, if there are other statements following the "if" block, they may be executed even when the condition is not met.

2. Based on the text's view on increment/decrement operations, and considering the design of a traditional Turing machine, I see some similarities. In a Turing machine, the read/write head's position can be altered by incrementing or decrementing it. However, this can lead to ambiguity, as the operation may be applied to the cell being read or the cell next to it, depending on the implementation. To avoid this issue, we can introduce an explicit move operation to separate the reading and writing processes, ensuring that the read/write head's position is only updated after the current cell has been processed.

3. Regarding the given "Go Language Beginner's Guide," I believe I can identify a design flaw caused by an overemphasis on brevity. While the guide emphasizes the simplicity and readability of Go's syntax, it omits discussing the importance of error handling. This oversight can lead to errors being ignored or handled improperly, potentially causing significant issues in larger programs.

4. In the context of the "Go Language Beginner's Guide," I would suggest adding a section on error handling to ensure that beginners are aware of this crucial aspect of programming in Go. This section should cover best practices for error handling, such as using the error type and error values, and provide examples of how to handle errors effectively. By doing so, the guide will better prepare beginners for real-world programming scenarios and help them avoid potential pitfalls.