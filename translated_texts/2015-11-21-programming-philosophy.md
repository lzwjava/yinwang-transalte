---
layout: post
title: "Programming Intelligence"
---


Programming is a creative job, an art. Mastering any art requires a lot of practice and understanding. The "intelligence" mentioned here is not a magic weight loss pill, it cannot replace your own diligence. However, due to the software industry's love for novelty and complexity, I hope these words can guide those who are confused and help them avoid unnecessary detours, achieving a roughly one-to-one ratio of effort and reward.

### Repetitively Refactor Code

Some people boast about how many millions of lines of code they have written, as if the quantity of code is the standard for programming proficiency. However, if you always write code in a hurry without ever looking back to refactor, modify, and optimize, you won't be able to improve your programming skills. You'll produce increasingly mediocre or even poor code. In this sense, the "work experience" many people talk about may not correlate with the quality of their code. If someone has decades of work experience but never goes back to refactor and reflect on their code, they might not be as good as someone with only a few years of experience who meticulously refactors and deeply understands their code.

A famous author once said, "A writer's level is not determined by how much they've published, but by how much they've thrown away." I believe the same principle applies to programming. Good programmers, they delete more code than they keep. If you see someone who has written a lot of code but hasn't deleted much, their code is bound to have a lot of garbage.1. Just like literary works, code cannot be mastered in one stroke. Inspiration seems to always come in pieces, gradually and gradually. No one can write a perfect piece in one go, not even the most brilliant programmer. After refining a piece of code for a while, you may feel you've reached the peak, but after a few months, you may find room for improvement and simplification. This is similar to writing articles; revisiting old work several months or even years later always reveals areas for improvement.

2. If you've hit a plateau in refining your code and it no longer shows progress, take a break for a few weeks or months, then revisit it. You might find new inspiration. Repeat this process multiple times, and you'll accumulate both inspiration and wisdom, enabling you to make progress when encountering new problems.

### Writing elegant code

People dislike "spaghetti code" (tangled code) because it resembles spaghetti in its tangled and disorganized nature, making it difficult to follow a train of thought. So, what does elegant code generally look like? After observing for many years, I've found that elegant code has distinct characteristics in its shape.

If we disregard specific content and focus on the overall structure, elegant code appears to be a series of neatly arranged, interconnected boxes. If we make a comparison to organizing a room, it becomes clear. If you throw all items into a large drawer, they will mix together, making it difficult to organize and find specific items quickly. However, if you place smaller boxes within the drawer and categorize items, they will not be scattered about, and you can easily find and manage them.: The elegant code's another feature is that its logic generally looks like a clear tree structure (tree). This is because the program does almost everything through information transmission and branching. You can think of the code as a circuit, with current flowing through wires, diverging or merging. If you think this way, there will be fewer if statements with only one branch in your code, which will look like this:

if (...) {
// code for the if condition
} else {
// code for the else condition (optional)
}

In this case, the tree structure refers to the way control flows through the code, with conditional statements acting as branches that split or merge based on the evaluation of conditions. The absence of single-branch if statements can make the code more readable and maintainable, as it reduces the number of simple conditional statements and encourages more logical grouping of related code. I if (...){ // code block

...

} if (condition is false) {
// code here
}

else {
// code here
}

In this context, the Chinese text does not provide any meaningful information to translate, as it is just the basic structure of an "if-else" statement in programming. if (...) {
else {
if (...) {

Translation:

If (condition 1) {
// code for condition 1
} else {
If (condition 2) {
// code for condition 2
}
}

This is a simple if-else statement in C-like programming languages, where the first if statement checks for condition 1, and if it's true, the code inside the first curly braces is executed. If condition 1 is false, the code inside the else statement is executed, which is another if statement checking for condition 2. if (condition is false) {
// code to be executed if condition is false
}
else {
// code to be executed if condition is true
}

Here's the English translation of the given Chinese text, which is actually a code snippet written in C++ or a similar programming language:

if (condition is false) {
// code to be executed if condition is false
}
else {
// code to be executed if condition is true
} I noticed that, in my code, if statements almost always have two branches. They may be nested and have multiple levels of indentation, and the else branch may contain some repeated code. However, this structure is logically very tight and clear. I will tell you why having two branches in an if statement is best in the next part.

### Writing Modular Code

[Note: The text provided seems to be incomplete as it ends abruptly. The translation is based on the available context.] some people argue loudly for modularization of the program, but their methods result in dividing the code into multiple files and directories, then calling these directories or files "modules". They even put these directories in different VCS repos. However, this approach did not bring smooth cooperation but caused a lot of trouble. This is because they actually do not understand what modularization means, shallowly cutting the code and placing it in different locations cannot achieve the purpose of modularization, and it also created unnecessary trouble.

True modularization is not textual but logical. A module should be like a microchip, it has clearly defined inputs and outputs. In fact, a good modularization method already exists, it's called "functions". Each function has clear inputs (parameters) and outputs (return values), and the same file can contain multiple functions. Therefore, you don't actually need to split the code into multiple files or directories, you can still accomplish code modularization in the same file. I can write all the code in one file, yet it is still very modularized code.

To achieve good modularization, you should do the following:

- Avoid writing long functions. If you find a function is too long, you should split it into several smaller ones. Generally, I write functions that are no longer than 40 lines. Compared to this, a typical notebook computer screen can only display about 50 lines of code. I can see a 40-line function in one glance without scrolling, while a 50-line function would require scrolling. The reason for 40 lines instead of 50 lines is that my eyes don't need to move if I don't, and the largest field of view can only see 40 lines of code. If I look at the code without moving my eyes, I can completely map the entire code to my visual nervous system, allowing me to remember the entire code even if I close my eyes. I find that closing my eyes helps my brain process the code more effectively. You can imagine that this code can take on various other forms. Forty lines is not a big constraint because the complex parts of the function are usually extracted and made into smaller functions, then called from the original function.

- Create small utility functions. If you carefully observe the code, you will find that there are actually many repetitions. These common codes, no matter how short, can be extracted and made into functions, which can simplify the logic of the main function. Some people don't like using small functions because they want to avoid the overhead of function calls, but modern compilers can automatically inline small functions into the calling location, so there is no actual function call and no additional overhead. Similarly, some people like to use macros instead of small functions, but this is an outdated notion. In early C language compilers, only macros were statically "inline", so they used macros to achieve inlining. However, whether a function can be inlined or not is not the fundamental difference between macros and functions. Macros and functions have huge differences (which I will talk about later), and you should try to avoid using macros as much as possible. Using macros to inline is an abuse of macros, which can lead to various problems, such as making the program difficult to understand, difficult to debug, and prone to errors. 1. Each function should only do one simple thing. Some people like creating some "general" functions that can do this and that, with internal logic based on certain variables and conditions to determine what the function should do. For instance, you might write a function like this: void foo() { if (getOS().equals("MacOS")) { a(); } else { b(); } c(); if (getOS().equals("MacOS")) { d(); } else { e(); } } The person who wrote this function decides what to do based on the system being "MacOS." You can see that only c() is common to both systems, while a(), b(), d(), e() belong to different branches. This kind of "reuse" is actually harmful. If a function can possibly do two things, and their common points are fewer than their differences, it's better to write two separate functions instead. This way, the logic will be clearer and less error-prone. In fact, the above function can be refactored into two functions: void fooMacOS() { a(); c(); d(); } and void fooOther() { b(); c(); e(); } If you find that two things have a large common part and only a small difference, you can extract the common part into a helper function. For example, if you have a function like this: void foo() { a(); b(); c(); if (getOS().equals("MacOS")) { d(); } else { e(); } } where a(), b(), c() are the same, but d() and e() differ based on the system, you can extract a(), b(), c() into: void preFoo() { a(); b(); c(); } and then create two functions: void fooMacOS() { preFoo(); d(); } and void fooOther() { preFoo(); e(); } This way, we share code while ensuring each function does one simple thing.

2. Avoid using global variables and class members (class members) to transmit information, prefer using local variables and parameters instead. Some people write code that frequently use class members to transmit information, like this: class A { String x; void findX() { ... x = ...; } void foo() { findX(); ... print(x); } } First, they use findX() to assign a value to member x. Then, they use x's value. In this way, x becomes a data channel between findX and print. Since x is a member of class A, the program loses modularity. Both functions depend on the class member x, losing clear input and output, and instead depending on global data. findX and foo cannot exist independently of class A, and due to the possibility of class members being modified by other code, the code becomes hard to understand and hard to ensure correctness. If you use local variables instead of class members to transmit information, these two functions no longer depend on a specific class, making the code clearer and easier to understand: String findX() { ... x = ...; return x; } void foo() { String x = findX(); print(x); }

3. Don't rely on excessive comments to make code readable. Some people believe that writing many comments makes code more readable, but they find that it doesn't live up to their expectations. Comments not only fail to make the code readable, but the abundance of comments in the code makes it hard to read. Moreover, when the logic is modified, many comments become outdated and need to be updated. Updating comments is a significant burden, so an abundance of comments becomes an obstacle to improving the code.

In reality, elegant and readable code requires little to no comments. If you find yourself writing many comments, your code is likely confusing and unclear in its logic. Programming languages have strengths that natural language lacks: subjects, verbs, objects, nouns, if, then, else, is, isn't, etc. If you fully utilize the expressive power of programming languages, you can express what the code is doing through the code itself, without the need for natural language assistance.1. In some cases, you might write code that goes against common practices to bypass certain design issues. In such cases, you can use very short comments to explain why it is written that way. Such situations should be rare, as it indicates that the entire code design has issues.

2. If you don't effectively utilize the advantages of the programming language, you will find that the code is still difficult to understand, requiring comments. Here are some points that might help you significantly reduce the need for comments:

a. Use meaningful function and variable names. If your function and variable names can clearly describe their logic, you won't need comments to explain what they do. For example: // put elephant1 into fridge put(elephant1, fridge2); The function name put, combined with the meaningful variable names elephant1 and fridge2, already convey what is happening (putting an elephant into a fridge). Therefore, the above comment is unnecessary.

b. Local variables should be defined as close as possible to their usage. Some people like to define many local variables at the beginning of a function and then use them far away, like this: void foo() { int index = ...; ... bar(index); ... } Since there is no use of index between its definition and usage, and no change to the data it depends on, this variable definition can be moved closer to its usage: void foo() { ... int index = ...; bar(index); ... } This way, readers can see bar(index) and understand how index is computed without having to look far up. Additionally, this short distance strengthens readers' understanding of the "calculation order." Conversely, if index is at the top, readers might suspect that it holds some mutable data or has been modified later. If index is at the bottom, readers clearly know that index does not hold any mutable value and has not changed since its calculation. If you understand the essence of local variables—they are like wires in a circuit—you will better grasp the benefits of proximity. The closer the variable definition is to its use, the shorter the wire length. You don't need to touch a wire and trace it back to find its terminal, making the circuit easier to understand.

c. Local variable names should be short. This may seem contradictory to the first point, but consider that local variables are local, and the second point has already placed them as close as possible to their usage. For example, you have a local variable representing whether an operation was successful: boolean successInDeleteFile = deleteFile("foo.txt"); if (successInDeleteFile) { ... } else { ... } This local variable successInDeleteFile can be made less verbose. Since it is only used once and its usage is right below it, readers can easily infer its meaning. For instance, you can rename it as success: boolean success = deleteFile("foo.txt"); if (success) { ... } else { ... } This way, readers can quickly grasp its meaning from the context, and the code remains semantically equivalent while being more readable. successInDeleteFile, with its "camelCase," can be quite bothersome if it consists of more than three words. Therefore, if you can represent the same meaning with a single word, that is preferable. 1. Do not reuse local variables. Many people dislike defining new local variables and prefer to "reuse" the same local variable by repeatedly assigning values to it to represent completely different meanings. For example, the following code: String msg; if (...){msg="succeed"; log.info(msg);} else {msg="failed"; log.info(msg);} Although this code is logically correct, it is not clear and easy to confuse. The variable msg is assigned two different values, which are immediately used by log.info and do not get passed to other places. This way of assigning values enlarges the local variable's scope unnecessarily, making people think it may change in the future and might be used elsewhere. A better approach is to define two variables: if (...){String msg="succeed"; log.info(msg);} else {String msg="failed"; log.info(msg);} Since the scope of these msg variables is limited to their respective if statement branches, you can clearly see their usage ranges, and you know there is no relationship between them.

2. Extract complex logic into "helper functions". Some people write long functions, making it hard to tell what the statements inside are doing, so they mistakenly believe they need to write comments. If you carefully observe these codes, you will find that unclear pieces of code can often be extracted and made into a function, then called in the original place. Since functions have a name, you can use meaningful function names instead of comments. For example: // put elephant1 into fridge 2 openDoor(fridge2); if (elephant1.alive()) { ... } else { ... } closeDoor(fridge2); ... If you extract this piece of code and define it as a function: void put(Elephant elephant, Fridge fridge) { openDoor(fridge); if (elephant.alive()) { ... } else { ... } closeDoor(fridge); } The original code can then be changed to: ... put(elephant1, fridge2); ... It is clearer, and the comments are no longer necessary.

3. Extract complex expressions into intermediate variables. Some people, having heard that "functional programming" is a good thing but not understanding its true meaning, use nested functions excessively in their code. For example: Pizza pizza = makePizza(crust(salt(), butter()), topping(onion(), tomato(), sausage())); This code is too long and has too many nestings, making it hard to understand. Experienced functional programmers know the benefits of intermediate variables and do not blindly use nested functions. They will transform this code into: Crust crust = crust(salt(), butter()); Topping topping = topping(onion(), tomato(), sausage()); Pizza pizza = makePizza(crust, topping); This way of writing, not only effectively controls the length of a single line of code, but also because the introduced intermediate variables have "meaning", the steps become clear, and it becomes easy to understand.

4. Reasonably split long lines. For most programming languages, the logic of the code is unrelated to white space characters, so you can almost arbitrarily wrap lines, and you can also choose not to wrap lines. This design is good because it gives programmers the ability to control their code format. However, it also brings some problems, as many people do not know how to reasonably wrap lines.

Some people rely on IDE's automatic line breaking feature, editing the code and then using a hotkey to reformat the entire code automatically. However, this automatic reformatting often does not follow the logic of the code and cannot help in understanding the code. Automatically reformatted code may look like this:

[1] Pizza pizza = makePizza(
[2] crust(salt(), butter()),
[3] topping(onion(), tomato(), sausage())
[4] );

This automatically reformatted code may make it hard to follow the logical flow of the code. if (someLongCondition1() && someLongCondition2) {
// code block
}

Translation:

if (condition 1 is true and condition 2 is true) {
// code block
} if (someLongCondition3) {
// code here
}

&&

// code here

if (someLongCondition3) {
// code here
} if (someLongCondition) {

// code here

}

In this context, "someLongCondition" refers to a boolean expression that determines whether the code inside the curly braces ({}) should be executed or not. The parentheses are used to group the boolean expression for better readability and to ensure proper precedence in more complex conditions. due to someLongCondition4() exceeding the line width limit, it was automatically wrapped to the next line by the editor. Although it met the line width limit, the wrapping position was quite arbitrary and did not help in understanding the logic of the code. These several boolean expressions are all connected with &&, so they are actually at an equal position. To express this point, when wrapping is necessary, each expression should be put on a new line, like this:

if ( someLongCondition1 ()

if ( someLongCondition2 ()

if ( someLongCondition3 ()

if ( someLongCondition4 () ) { ... } if (someLongCondition2) {
// code block for someLongCondition2
}
if (someLongCondition3) {
// code block for someLongCondition3
}
// and operator for both conditions
if (someLongCondition2 && someLongCondition3) {
// code block for both conditions met
} if (someLongCondition4) {

// code here

}

In this code snippet, the Chinese text does not appear. The text is written in JavaScript syntax with English keywords. The parentheses and the "if" statement are used for conditional statements in JavaScript programming. The "someLongCondition4" is a variable or a condition that will be evaluated by the JavaScript engine. If the condition is true, the code inside the curly braces will be executed. Such that each condition aligns, the logic within becomes clear. For instance:

log [condition1] && condition2 && ... && conditionN;

or

if (condition1) && (condition2) && ... && (conditionN) {
// logic here
} "Could not find file {} for command {}, exception {}"
-----

file (variable representing file name)
command (variable representing command name)
exception (variable representing exception message) file, command and exception are of the same kind but two of them are left on the first line, the last one being wrapped to the second line. It would look better if it is manually lined up like this:

exception
file
log
command "Could not find file {} for command {}, exception {}"
.....
file
command
exception I. Command and exception

II. Format string on a separate line, place its parameters on another line for clearer logic.

III. To prevent IDEs from messing up manually adjusted line breaks, many IDEs (such as IntelliJ) have a "preserve original line breaks" setting in their automatic formatting options. If you find that the IDE's line breaks don't make sense, you can modify these settings and manually preserve your line breaks in certain places. "At this point, I must warn you, the "no need to comment, let the code explain itself" mentioned here, is not about making the code look like some natural language. There is a JavaScript testing tool called Chai, which allows you to write code like this:"

expect(
foo
).
to.
be.: string;
expect: foo;: To be equal
(
' bar '
);

Translation:
To be equal, bar; expect to have length.

This is a simple English sentence that can be translated from the given Chinese text, which appears to contain some missing or incorrect characters. The English sentence conveys the idea that there is an expectation for something to possess a certain length. anticipate having tea

This is a simple English sentence derived from the given Chinese text. The Chinese text seems to be incomplete or fragmented, so I assumed it was meant to convey the idea of anticipating or looking forward to having tea. The English sentence is a close translation of that concept.:
Properties:
(
'flavors'
).
with:
Length:: This approach is very wrong. The programming language is already simple and clear in itself, but this way makes it look like natural language, making it unnecessarily complex instead.

### Write simple code

Programming languages love to be innovative and offer various "features," but some features are not as good as they seem. Many features do not withstand the test of time and bring more trouble than they solve. Some people blindly pursue "short and clever" or show off their intelligence by learning and using language-specific constructs to write overly "clever," hard-to-understand code.:

It is not because of the language that you have to use all its features. In fact, you only need a small part of its functions to write excellent code. I have always been against fully utilizing all the features of a programming language. In reality, I have a preferred set in my mind. No matter how "magical" or "new" the features a language provides, I mostly rely on the proven and trusted set.

Regarding some problematic language features, I will introduce some coding conventions I use and explain why they make the code simpler.

- Avoid using increment/decrement expressions (i++, ++i, i--, --i). These increment/decrement expression operations are actually historical design mistakes. They have ambiguous meanings and are easily confused. They mix up reading and writing operations, making the semantics messy. Expressions containing them may have results depending on evaluation order, making them potentially correct in some compilers but causing odd errors in others. In reality, these two expressions can be decomposed into two steps, separating reading and writing: one step updates i's value, and the other uses i's value. For example, if you want to write foo(i++), you can decompose it into int t = i; i += 1; foo(t);. Similarly, for foo(++i), decompose it into i += 1; foo(i);. The decomposed code has the same meaning but is much clearer. It's clear which update is before or after the value is taken. Some people might think i++ or ++i have higher efficiency than decomposed code, but this is a misconception. These codes become identical machine code after basic compiler optimization. Increment/decrement expressions are safe to use only in two situations: in for loop update parts, like for(int i = 0; i < 5; i++), and as standalone statements, like i++ or i--. You should avoid using them in other situations, such as in complex expressions like foo(i++), foo(++i) + foo(i), … Nobody should know, or even bother to understand, what these mean.

- Never omit braces. Many languages allow you to omit braces in some cases, like C and Java, when there is only one statement in an if statement: if(...) action1(); It looks cleaner, but it often leads to strange issues. For instance, if you later want to add action2() to this if statement, you change it to if(...) action1(); action2(); You carefully indent action1() to make it look like they are in the same if block. However, action2() is actually outside the if statement and runs unconditionally. I call this phenomenon the "optical illusion." Every programmer should be able to spot this error, but it is often overlooked. So, you might ask, why not just add braces when adding action2()? However, from a design perspective, this is not a sound practice. First, you might later remove action2(), and to maintain style consistency, you'd have to remove the braces as well, which is inconvenient. Second, this inconsistent coding style makes the code harder to read, as some if statements have braces and some don't. Moreover, why should you remember this rule? If you don't question three seven twenty-one, just put braces in every if-else statement, and you'll never have to think about it. Some people might argue that putting braces in every statement is more cumbersome, but after implementing this coding standard for a few years, I haven't found it to be more annoying. Instead, the presence of braces makes the code boundaries clearer, reducing the mental load on my eyes.

- Use parentheses reasonably, and don't blindly rely on operator precedence. Using operator precedence to reduce parentheses is fine for common arithmetic expressions like 1 + 2 * 3. However, some people hate parentheses so much that they write expressions like 2 << 7 - 2 * 3 without them. The problem here is that the shift operator << has a different precedence than most people are familiar with, and it goes against common sense. Since x << 1 is equivalent to x multiplied by 2, many people mistakenly believe that the expression 2 << 7 - 2 * 3 is equivalent to (2 << 7) - (2 * 3), resulting in 250. However, the << operator has lower precedence than addition +, so the expression actually corresponds to 2 << (7 - 2 * 3), resulting in 4! The solution to this problem is not to have everyone memorize operator precedence tables but to reasonably use parentheses. For example, in the previous example, it's best to add parentheses and write it as 2 << (7 - 2 * 3). Although the expression has the same meaning without parentheses, adding parentheses makes it clearer, and readers don't need to memorize the precedence of the << operator to understand the code.:

Avoid using continue and break in loops. Using return inside loop statements (for, while) is fine, but if you use continue or break, it complicates the loop logic and termination condition, making it hard to ensure correctness. Reasons for using continue or break often stem from a lack of clear understanding of the loop logic. If you have considered all aspects, you should rarely need to use continue or break. If your loop contains continue or break, you should consider rewriting it. Ways to rewrite loops include reversing the condition for continue and removing it, merging the break condition into the loop termination condition and eliminating break, or replacing break with return. Here are some examples:

Case 1: The following code contains a continue:
List<String> goodNames = new ArrayList<>();
for (String name : names) {
if (name.contains("bad")) {
continue;
}
goodNames.add(name);
...
}
This code says: "If name contains the word 'bad', skip the rest of the loop code..."
Notice that this is a negative description, telling you what not to do rather than what to do. To understand what it's actually doing, you need to figure out which statements are being skipped due to the continue, and then reverse the logic in your head. This is why loops with continue and break are hard to understand – they rely on control flow to describe what not to do, what to skip, and the final result may not be clear. Instead, we can reverse the continue condition, and this code can be easily transformed into an equivalent, continue-free version:
List<String> goodNames = new ArrayList<>();
for (String name : names) {
if (!name.contains("bad")) {
goodNames.add(name);
...
}
}
The code inside the if statement and the rest of the code after it have been moved into the if statement, with an extra indentation level, but the continue statement is no longer needed. Reading this code, you'll find it clearer. It now positively states: "Add name to the goodNames list if it does not contain the word 'bad'..."

Case 2: Both the for and while loop headers have a loop termination condition, which should be the unique exit condition. If you have a break in the middle of the loop, it actually adds another exit condition. You can usually merge this condition into the loop header and eliminate the break. For example, consider the following code:
while (condition1) {
...
if (condition2) {
break;
}
}
When condition is true, break exits the loop. Instead, you can move condition2 to the while header and reverse its logic to eliminate this kind of break statement:
while (condition1 && !condition2) {
...
}
This situation seems to only apply to break statements at the beginning or end of the loop, but in reality, most break statements can be moved to the beginning or end of the loop through some means. I'll add specific examples when they come up.

Case 3: Many break statements exit the loop and then return. These break statements can often be replaced with a return. Consider the following example:
public boolean hasBadName(List<String> names) {
boolean result = false;
for (String name : names) {
if (name.contains("bad")) {
result = true;
break;
}
}
return result;
}
This function checks whether the names list contains a name with the word "bad" in it. Its loop contains a break statement. This function can be rewritten as:
public boolean hasBadName(List<String> names) {
for (String name : names) {
if (name.contains("bad")) {
return true;
}
}
return false;
}
The improved code checks for the presence of "bad" directly in the for loop and returns true if found, eliminating the need for the result variable and the break statement. If the loop finishes without finding "bad", it returns false. Replacing break with return, these statements are removed. I've seen many other examples of continue and break usage that can be eliminated, and the resulting code becomes much clearer. My experience is that 99% of breaks and continues can be removed using return statements or flipping if conditions. The remaining 1% involves complex logic, but it can also be simplified by extracting a helper function. Modifying the code in this way makes it easier to understand and ensures correctness. I have a principle when writing code: if there is a more direct and clear way, I choose it, even if it looks longer and dumber. For example, there is a "clever" way to write commands in Unix command line as follows:

command1 && command2 && command3

Due to the short-circuit logic property of "a && b" in Shell language, if "a" is false, then "b" doesn't need to be executed. That's why command2 is only executed when command1 succeeds, and command3 is only executed when command2 succeeds. Similarly,

command1 || command2 || command3

This is called "short-circuit evaluation" or "short-circuit logical operator" in programming. It can help to improve the efficiency of the script by avoiding the unnecessary execution of some commands when the result can be determined by the previous command's result. This operator also has similar features. The command line above, if command1 is successful, command2 and command3 will not be executed. If command1 fails but command2 is successful, command3 will not be executed.

This is more clever and concise than using if statements to judge failure. Therefore, people have borrowed this method and used it in their program code. For example, they may write code like this:

if ! command1 && ([success] command2) ! command3; action2
()

&&

action3
())

This translates to:

action2 ()

&&

action3 (): You can tell what this code is intended for, under what conditions action2 and action3 are executed, and under what conditions they are not? You might need to think about it a bit to figure it out: "If action1 fails, execute action2, if action2 succeeds, execute action3." However, this meaning is not directly mapped onto this code. For instance, what does "fail" correspond to in the code? You can't tell, because it's included in the || semantics. You need to know the short-circuit property and the meaning of the logical or operator to understand "if action1 fails..." in this context. Every time you see this line of code, you have to think about it, which accumulates a heavy mental load.

In fact, this writing style is an abuse of the short-circuit property of logical operators && and ||. These operators might not execute the right-hand expression, for the sake of the machine's execution efficiency, not to provide this "clever" usage for you. Their intended purpose is only as logical operations, they are not meant to replace if statements. In other words, they can only achieve some effects of if statements by chance, but you should not use them to replace if statements. If you do, your code will become obscure. if (!action1) {
// code here
}

In English, the Chinese text translates to: "The code written above can be made simpler:

if (
!action1
) {
// code here
}

So, the English translation of the simplified Chinese code is:

if (!action1) {
// code here
} if (action2()) {
// code block for if condition is true
}

In this code snippet, "if" is a conditional statement in programming, and "(action2())" is a function call to "action2". The code block following the curly braces "{}" will be executed only if the function call returns a true value. I can see clearly from here what this code is saying, no need to think about it: if action1() fails, then execute action2(), if action2() succeeds, then execute action3(). Do you see the one-to-one correspondence here? if = if, != = failure, ... You don't need to use logical knowledge to figure it out.

Translation:

if (action1() != SUCCESS) {
 action2();
 if (action2() == SUCCESS) {
 action3();
 }
} I mentioned in the previous lesson that my code rarely contains a single-branch if statement. Most of the if statements I write have two branches, so my code often looks like this:

if (...) {
 (...)
} else {
 (...)
} if (...){

 // code here

} This Chinese text does not contain any readable or meaningful information as it is written in a programming language syntax (JavaScript) and does not contain any Chinese characters. The text is simply a code snippet for returning a false value in JavaScript. if (true) {
// code here
} else {
// code here, but it will not be executed since the condition is true
}

// This translation assumes that the given Chinese text is not the actual code, but rather a comment or explanation in Chinese for the given code snippet in JavaScript. The code snippet itself is written in English and does not need to be translated. Else, if {

(...)

If

}

Else, if {

(...)

If no return false if (condition) {
// code block for true condition
}
else {
// code block for false condition

 return;
}

In English, this code snippet is an "if-else statement" in the C programming language. It checks a condition, and if the condition is true, it executes the code block inside the first set of curly braces. If the condition is false, it executes the code block inside the second set of curly braces, and then returns from the function. I. True statement;

II. This approach is used to relentlessly handle all possible cases, preventing omission of corner cases. Each if statement has two branches of reasoning: if the if condition is met, you do something; if not, you know what else to do. No matter if your if has an else or not, you cannot escape the need to consider this question.

III. Many people writing if statements like to omit the else branch because they feel some else branches' code is redundant. For instance, in my code, both else branches are return true. To avoid redundancy, they omit those two else branches and only use a final return true. Such an if statement without an else branch will automatically "fall through," reaching the final return true. Their code looks like this:

[End of Translation]

I. The statement is true.

II. This method is used to exhaustively handle all possible cases, preventing the omission of corner cases. Each if statement has two branches of reasoning: if the if condition is met, you perform some action; if not, you know what else to do. No matter if your if has an else or not, you cannot escape the need to consider this question.

III. Many programmers writing if statements tend to omit the else branch because they believe some else branches' code is redundant. For example, in my code, both else branches return true. To avoid redundancy, they omit those two else branches and only use a final return true. Such an if statement without an else branch will automatically "fall through," reaching the final return true. Their code looks like this: if (...) {

// code here

}

In English, the Chinese characters for "if" translate directly to the English keyword "if". The text provided is written in a programming context, so the English translation would be the standard syntax for an "if" statement in a programming language. if (condition) {
// code here
}

return false; if (condition) {
// code block 1
} else if (another condition) {
// code block 2
}
// else:
// code block 3

This is a basic conditional statement structure in programming, written in C-like syntax. The semicolons at the beginning are likely a mistake and should be removed. (...)
 {
 ...

 return;
 ...

 } 1. false
2. return
3. true This kind of writing seems simpler and avoids repetition, but it is easy to result in oversights and loopholes. The omission of some elses in nested if statements relies on the control flow to handle else situations, making it difficult to correctly analyze and infer. If your if conditions contain && and || type logical operations, it becomes even harder to determine if all cases are covered.

Due to oversights, all omitted branches will automatically "fall through", resulting in unexpected outcomes. Even if you are convinced it is correct after reading it once, you cannot be sure it handles all cases, and you have to rethink it every time. This simple writing brings about repetitive and heavy mental overhead. This is called "spaghetti code", as the logical branches of the program are not like a clear-cut tree, but rather like tangled spaghetti.

Another way to omit else branches is as follows:

String s

if (s.length() > 0 && s.charAt(0) == 'a') {
// do something
}

// This code snippet lacks an else branch for the case where s.length() > 0 but s.charAt(0) is not 'a'. This can lead to unintended consequences. if (x) {
// code block for if condition is true
} five brackets or parentheses

This translation is based on the given Chinese text which consists of five brackets or parentheses. The text itself does not contain any meaningful content that can be translated into English words. The programmer of this code likes to use a "default value" approach in his mind. If x is less than 5, change (mutate) s to "ok". The drawback of this approach is that when x is not less than 5, you need to look up to know what the value of s is. This is fortunate if s is not far away. However, when writing this code, s's initial value may be some distance from the judgment statement, and there may be other logic and assignment operations inserted in between. Such code, with variables being changed back and forth, is easy to make errors as it can be confusing to follow. I'll compare my writing now:

String
s
;

if ( five brackets or parentheses

Here's the English translation without any Chinese characters or punctuation:

five brackets or parentheses "if (s == "ok") {\n else"

In English, this code snippet translates to:

"if s is equal to 'ok' {\n else" I
am
a
computer
program
designed
to
understand
and
process
natural
language
text
.

Here
is
a
Chinese
text:

{

它
是
一
台
计
算
机
程
序
，
旨在
理解
和
处理
自然
语言
文
本
。

;

Translation:

It is a computer program designed to understand and process natural language text. This writing style seems to have added a few more characters, yet it becomes clearer. This is because we explicitly indicated what s's value is when x<5 is not true. It is "". Note that even though I also used an assignment operation, I did not "change" s's value. S had no value initially, and it never changed after being assigned. My writing style is usually referred to as "more functional" because I only assign once.

If I overlooked the else branch, the Java compiler would not spare me. It would complain: "s is not initialized in one of the branches." This forces me to clearly set s's value under various conditions, leaving no case unattended.

Of course, due to the simplicity of this situation, you can also write it as:

String s;
if (x < 5) {
// some code here
} else {
s = "";
} selx e = 5

This text appears to be a combination of English and Chinese characters, but it is not grammatically correct or meaningful in either language. The Chinese characters do not form a complete word or phrase, and the English letters do not form a recognizable English word. It is likely that there is an error or mistake in the input. I'm sorry, the given Chinese text consists only of symbols that do not form a meaningful sentence or word in Chinese. Therefore, there is no translation to provide. For more complex situations, I recommend writing as an if statement.

### Properly handling errors

Use an if statement with two branches, which is just one reason why my code is unbeatable. The approach to writing if statements in this way, in fact, embodies a common reliable programming idea: exhaustively cover all cases, leaving none behind.

The majority of a program's functions are for processing information. From a pile of intricate, borderline, and ambiguous information, exclude most of the "interfering information," and find what you need. Correctly dealing with all possibilities is the core idea of writing unbeatable code. In this section, I will discuss how to apply this thinking to error handling.

Error handling is an old problem, but even after several decades, many people still don't understand it. The system API manual for Unix systems usually tells you about possible return values and error messages. For example, the Linux read system call manual contains the following:: On success, the number of bytes read is returned.

On error, -1 is returned, and errno is set accordingly.

ERRORS:
EAGAIN, EBADF, EFAULT, EINTR, EINVAL, ...

Many beginners often forget to check the return value of read for -1, thinking it is tedious to check every time, and it seems safe not to check. This thinking is actually dangerous. If the function's return value tells you it either returns a positive number, indicating the length of data read, or returns -1, then you must make appropriate and meaningful handling of this -1. In no case should you ignore this special return value, as it represents a "possibility." Neglecting any possible scenario in your code can result in unforeseen catastrophic consequences. For Java, this is more convenient. In Java, if a function encounters a problem, it is generally indicated through exceptions (exception). You can add exceptions to the function's original return type, considering it as a "union type." For example:

String
foo()
throws
[Exception1, Exception2]; This is where MyException represents an error return. You can think of this function returning a union type: {String, MyException}. Any code calling foo must make reasonable handling of MyException, in order to ensure the correct running of the program. Union types are a rather advanced type, only a few languages (such as Typed Racket) have this type. I mention it here only to facilitate the explanation of the concept. Once you understand the concept, you can actually implement a union type system in your mind, so you can write reliable code using ordinary languages. due to Java's type system requiring functions to declare potential exceptions within their types and forcing callers to handle potential exceptions, this safety mechanism rarely allows oversight. However, some Java programmers have a habit that renders this safety feature almost completely ineffective. Whenever the compiler errors with "you haven't caught this exception that foo function might throw," some people, without a second thought, modify the code like this:

try {
  foo();
} (catch (Exception e))

This is a code snippet written in C# programming language. The English translation of the Chinese text is the given C# code itself, which represents a try-catch block. The block catches any Exception that might be thrown during the execution of the code within the try block and handles it in the catch block. Or you can put a log in it at most, or simply add throws Exception to the type of your function, so the compiler will stop complaining. These methods seem convenient, but they are all wrong, you will eventually pay the price for it.

If you catch an exception and ignore it, then you won't know that foo actually failed. This is like driving a car and seeing a sign at the intersection that says "construction ahead, road closed," but continuing to drive. This problem will certainly occur eventually, because you don't know what you're doing.

When catching exceptions, you shouldn't use the so broad Exception type. You should catch the specific exception A that might occur. Using a broad exception type has a big problem, because it will accidentally catch other exceptions (such as B). Your code logic is based on judging whether A occurs, but you catch all exceptions (Exception class), so when other exceptions B occur, your code will have strange problems, because you think A occurred but it didn't. These bugs, sometimes even debuggers have difficulty discovering.

If you add throws Exception to the type of your function, then you cannot avoid handling this exception where it is called. If the called function also writes throws Exception, this problem will spread further. My experience is to handle exceptions as soon as they occur. Otherwise, if you return it to your caller, it might not know what to do. Outside, in try { ... } catch, there should be as little code as possible. For example, if foo and bar both may cause exception A, your code should be written as:

try {
foo();
}
catch (ExceptionA e) {
// handle exception A
}

// or use a try-catch block for each function call, if preferred:

try {
foo();
}
catch (ExceptionA e) {
// handle exception A
throw; // or handle it here
}

try {
bar();
}
catch (ExceptionA e) {
// handle exception A
throw; // or handle it here
} Catch the A e.

This text appears to be incomplete and may not have a clear meaning without additional context. The parentheses and brackets suggest that it might be a fragment of code or a formula, but without more information it is difficult to provide an accurate translation. The English text within the parentheses appears to be "A e," which does not make sense on its own. try {
 // code for the try block
 bar();
} // end of try block. Catch the A e.

This text appears to be incomplete and may not have a clear meaning without additional context. The brackets and parentheses suggest that it could be part of a programming code or a mathematical expression, but without more information, it's difficult to provide an accurate translation. The English text provided is a rough interpretation based on the given Chinese characters, but it may not make complete sense in the intended context. instead of
try {

// code here

} fool();

//

bar();

}

// catch { // in C++, use "try-catch" block instead
// } The first way of writing can clearly distinguish which function caused the problem, while the second way mixes them all up. It is beneficial to clearly identify which function caused the problem. For instance, if your catch code contains log, it can provide you with more precise error information, significantly accelerating your debugging process.: Correctly handling null pointers.

The exhaustive approach is so useful, based on this principle, we can derive some basic rules that will help you relentlessly handle null pointers.

First, you should know that many languages (C, C++, Java, C#, ...) have type systems that incorrectly handle null. This error stems from Tony Hoare's earliest design, who dubbed this mistake his "billion dollar mistake," as the financial and human resources lost due to it far surpassed ten billion dollars.

These languages' type systems allow null to appear in any place where an object (pointer) type can appear, yet null is not a legitimate object. It's not a String, not an Integer, not a custom class. Null's type should have been NULL, meaning null itself. Based on this fundamental notion, we derive the following rules:

- Strive to avoid null pointers. Try not to use null to initialize variables, and functions should strive not to return null. If your function returns "nothing" or "error," try to use Java's exception mechanism instead. Although the syntax is a bit awkward, Java's exceptions and function return values are essentially a union type. For instance, if you have a function find that can help you find a String, but might not find anything, you can write it like this: public String find() throws NotFoundException { if (...) { return ...; } else { throw new NotFoundException(); } } Java's type system will force you to catch this NotFoundException, so you won't overlook this situation like you would with a null check. Java's exceptions are a rather easily misused thing, but I've already told you how to use exceptions correctly in the previous section. Java's try...catch syntax is quite cumbersome and clunky, so if you're careful enough, you can also return null to indicate "not found." Many people write functions that return null to indicate "error," which is actually a misuse of null. "Error" and "not found" are entirely different things. "Not found" is a common and normal situation, like not finding something in a hash table. "Error," on the other hand, signifies a rare situation where there should normally be a meaningful value, but something unexpectedly went wrong. If your function is meant to indicate "error," it should use exceptions, not null.:

- Don't let NullPointerException occur. Some people write nice code and they like "error handling." First, they write some functions without careful null pointer checks: void foo(){String found = find(); int len = found.length(); ...} When foo calls cause an exception, they don't care, they just change the calling place to: try{foo();} catch(Exception e){...} This way, NullPointerException is captured and handled when found is null. However, this is incorrect practice. First, as mentioned earlier, "catch (Exception e)" type of writing should be avoided because it catches all exceptions, including NullPointerException. This may lead to unexpected capture of NullPointerException in the try statement, thus confusing the code logic. Additionally, even if you write "catch (NullPointerException e)", it is still not allowed. Since foo's internal lacks null checks, NullPointerException occurs. Now, instead of treating the symptom, you are making every call site add a catch, which will make your life harder. The correct way is to change foo, not the calling code. foo should be changed to: void foo(){String found = find(); if(found != null){ int len = found.length(); ...} else{ ...}} Check for null at the time when it might occur and handle it accordingly.

- Don't put null in "container data structures." A container (collection) refers to objects gathered in some way, so null should not be put in Arrays, Lists, Sets, or in Map keys or values. Putting null in a container is a strange error source. Since an object's position in a container is usually dynamically determined, once null enters from some entry point, it becomes difficult to figure out where it went, forcing you to check for null at every value extraction point. It's also hard to determine who put it there, making debugging more difficult as the code grows. The solution is: if you really want to represent "none," don't put it in (Arrays, Lists, Sets have no elements, and Map has no entry), or you can specify a legitimate, special object to represent "none." Note that class objects are not part of a container. So, null can be a value of an object member, indicating its absence. For example: class A{String name = null; ...} Since null can only appear in A object's name member, you just need to check it for null whenever you access the name member, not other members.

- Function callers: Understand what null represents, process and handle null return values early, and reduce its propagation. Null is annoying because it can mean different things in different places. Sometimes it means "none," "not found," sometimes it means "error," "failure," and sometimes it even means "success," ... There are many misuses, but you must understand each null's meaning and avoid confusion. If a function you call can return null, you should process and handle null at the earliest opportunity. For instance, the function find returns null when "not found," so the calling code should check for null immediately upon its return and handle the "not found" case meaningfully. "Meaningfully" refers to the user of the function knowing exactly what to do when receiving null, taking responsibility. They should not just "report up" and pass the responsibility to their caller. If you violate this, you might adopt an irresponsible, dangerous writing style: public String foo(){String found = find(); if(found == null){return null;}} When find() returns null, foo also returns null. This way, null travels from one place to another and represents a different meaning. If you write code without thinking, null can appear anywhere in your code without warning.

- Function authors: Clearly state that you don't accept null parameters, and crash immediately when a parameter is null. Don't try to "error handle" or "gracefully handle null," as it encourages callers to be careless with nulls. The problem with the example arises from people's "tolerant attitude" towards null. This "protective" writing style tries to "error handle" and "gracefully handle null," but it allows callers to be even more reckless with nulls. Eventually, your code becomes a mess of nonsense, with null appearing anywhere, and no one knows what it means or what to do. The correct approach is to take a firm stance. Tell function users that none of your parameters can be null, and if they give you null, the program crashes. As for the caller's code containing null, they should know how to handle it (refer to the previous points), not your responsibility. Adopting a firm stance is simple: use Objects.requireNonNull(). It's a simple definition: public static <T> T requireNonNull(T obj){if(obj == null){throw new NullPointerException();} else{return obj;}} You can use this function to check every parameter you don't want null, and if the passed parameter is null, it will immediately trigger a NullPointerException crash, effectively preventing null pointers from propagating to other places.1. Using Optional Types

Optional types are a feature provided by languages like Java 8 and Swift to mitigate null issues. Proper usage of this type can prevent null pointer problems, which exist because you can access an object's members without checking for null. The design principle of Optional types is to combine "checking" and "accessing" into a single atomic operation. This way, you cannot access without checking. This approach is a special case of pattern matching (ML, Haskell) in languages like Swift. In Swift, for example, you can write:

```swift
let found = find()
if let content = found {
    print("found: \(content)")
}
```

Here, the `find()` function returns an Optional type of value `found`. Assuming its type is `String?`, the question mark signifies it may contain a `String`, or it may be `nil`. The special `if` statement checks for null and unwraps the optional value in a single statement. The meaning of this statement is: if `found` is `nil`, the entire `if` statement is skipped; if it's not `nil`, the variable `content` is bound to the value in `found` (unwrap operation), and then the `print` statement is executed.

Java 8's approach is less elegant. If you obtain an `Optional<String>` type of value `found`, you must use functional programming methods to write the subsequent code:

```java
Optional<String> found = find();
found.ifPresent(content -> System.out.println("found: " + content));
```

This Java code is equivalent to the Swift code, containing a "check" and a "take value" operation. The `ifPresent` first checks if `found` has a value (equivalent to checking if it's not `null`). If it does, it binds its content to the `content` parameter (unwrap operation), and then executes the lambda inside. If `found` doesn't have a content, the lambda doesn't execute.

Java's design has a problem. The code after the check must be written inside the lambda. In functional programming, this lambda is called a "continuation," and Java calls it a "Consumer." It represents "if `found` is not `null`, take its value, and then do something." Due to the lambda being a function, you cannot return from it to the outer function. For example, if you want to refactor the following function (containing null):

```java
public static String foo() {
    String found = find();
    if (found != null) {
        return found;
    } else {
        return "";
    }
}
```

You would have to write it like this:

```java
public static String foo() {
    Optional<String> found = find();
    String result = "";
    found.ifPresent(content -> { result = content; }); // can't assign to result
    return result;
}
```

In the Java code, the return `a` in the lambda cannot return from the `foo` function. It only returns from the lambda, and due to the lambda's return type being `void`, the compiler will report an error, saying you returned a `String`. Since closures' free variables are read-only in Java, you cannot assign to lambda's outer variables. Therefore, you cannot adopt this writing style:

```java
public static String foo() {
    Optional<String> found = find();
    String result = "";
    found.ifPresent(content -> { result = content; }); // can't assign to result
    return result;
}
```

Although you have the found content in the lambda, using it and returning a value is confusing. You must use Java 8's provided functional programming operations like `map`, `flatMap`, and `orElse` to express the original code's meaning. For example, the previous code can be rewritten as:

```java
public static String foo() {
    Optional<String> found = find();
    return found.orElse("");
}
```

This simple case works fine. However, more complex code might be challenging to express. I have my doubts about Java 8's Optional type's expressiveness. A few things lack expressiveness, but they can lead to discussions on advanced theories like functors, continuations, and even monads. Using Optional seems to turn the language into something other than Java.

Although Java provides Optional, I believe its usability is relatively low and may not be widely accepted. Compared to Swift's design, it is more complex and less intuitive. Swift's design is simpler and more similar to traditional procedural programming. You only need to remember the special syntax `if let content = found {...}`, which has no difference in writing style compared to procedural languages. The main idea is to use the atomic operation of Optional to combine null checking and value access. This requires using the special syntax I introduced earlier. If you violate this principle and separate checking and accessing, you may still make mistakes. For instance, in Java 8, you can use `found.get()` to directly access the content in `found`. In Swift, you can use `found!` to directly access without checking. You can write Java code like this to use Optional:

```java
Optional<String> found = find();
if (found.isPresent()) {
    System.out.println("found: " + found.get());
}
```

If you use this method and separate checking and accessing, you might encounter runtime errors. The `if (found.isPresent())` statement is essentially the same as a regular null check, and if you forget to check `found.isPresent()` and directly call `found.get()`, you will get a `NoSuchElementException`. This is the same as a `NullPointerException`. Therefore, using this style is not much different from the traditional null usage. If you want to use Optional types effectively, follow the atomic operation writing style I introduced earlier.1. Excessive focus on future issues leading to unnecessary complexity: Many software projects are complex because people add unnecessary complexity for future considerations, even before current issues are resolved.
2. Overengineering due to excessive concern for code reuse: People focus on reusability before the code is even written, which leads to an abundance of frameworks that restrict progress, resulting in poor quality code that is rarely reused.
3. Over-emphasis on testing leading to overengineering: Some people change simple code to make it "testable," introducing complexity and causing an influx of bugs.

Principles to prevent overengineering:

1. Focus on the present: Solve current problems before extending functionality.
2. Keep it simple: Write code that is easy to understand and maintain.
3. Test only what is necessary: Write tests for critical functionality, but avoid excessive testing that adds unnecessary complexity.
4. Prioritize maintainability: Write code that is easy to modify and extend in the future.
5. Avoid unnecessary abstractions: Only abstract when necessary to simplify complex systems.
6. Keep dependencies minimal: Minimize the number of external dependencies to reduce complexity.
7. Refactor when necessary: Regularly refactor code to keep it clean and maintainable.
8. Follow established design patterns: Use proven design patterns to simplify development and reduce complexity.
9. Continuously evaluate and simplify: Regularly review your codebase and eliminate unnecessary complexity.
10. Embrace change: Be open to changing your approach when necessary to avoid overengineering. 1. Solve the problems at hand first, solve them, then consider expanding issues later.
2. Write out usable code first, debug it repeatedly, then consider whether to reuse it.
3. Write out usable, simple, obviously bug-free code first, then consider testing issues.

End. (This is not a free article. If you want to keep this information in mind, please go here to pay. Otherwise, please see:

[Some Link])