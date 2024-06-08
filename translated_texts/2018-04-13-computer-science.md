---
layout: post
title: "mystery computer science"
---


To master a subject, you cannot start from the details. The capabilities of the human brain are largely limited by beliefs. A person without faith in himself cannot do what he might be capable of. Confidence is important, but it is easily shattered. If one only sees the trees but not the forest, one will lose faith, thinking it will take a monkey's year and a horse's month to master a subject.

Therefore, we do not start from "trees," but guide the reader to explore the "forest" behind it, explaining the most fundamental concepts of computer science using simple examples, helping readers understand their essence. With these concepts slightly developed, you will gradually gain a complete grasp. You will hold the entire subject from the start, and you will continue to hold it, adding only more details. This is like painting, first sketching out the outline, adding details repeatedly, perfecting it, yet not losing sight of the big picture.

Generally, computer science students have studied many courses, but even after graduation, they cannot answer a fundamental question: what is computation? This chapter will guide you to discover the answer to this question. Do not underestimate this fundamental question, as it is often an essential clue to solving real-world problems. There are countless people in the world who do not understand it, and they have taken many detours and fallen into many pits, creating overly complex or flawed theories and technologies.

Now, let's come to understand a few key concepts and touch the essence of computation.1. When mom asks you "What is 4 plus 3?" she is a programmer, you are a computer. The computer receives the input from the programmer: 4, +, 3.

2. The computer recognizes the symbols and understands that it needs to perform addition. It sets the first number, 4, in the accumulator, a special register that stores the intermediate results.

3. The computer fetches the second number, 3, and adds it to the number in the accumulator. The result, 7, is stored back in the accumulator.

4. The computer then sends the result, 7, back to the programmer, mom, as the output. She receives the answer and is satisfied.

5. The computer, or you, have successfully completed a simple calculation, demonstrating the fundamental principles of computation.1. After listening to your mother's question, you put out both hands, extending four fingers on your left hand and three fingers on your right hand.

2. Then you started your own calculation process. One by one, you counted the fingers that were sticking up, bending each one down as you counted it to indicate that it had been counted. You said, "One, two, three, four, five, six, seven."

3. Now there were no fingers sticking up, so the last number you had counted became the answer: seven! The entire calculation process was now over.

### Symbols and Models

The preschool finger counting arithmetic contains profound philosophical questions. Here, we will begin to intuitively understand this problem. When mom says "help me calculate 4 + 3," the symbols "4," "+," and "3" reach your ears, they are all symbols. Symbols are "surface" things: just looking at the "4" and "3" Arabic numbers with their curved lines, one like a flag, one like an ear, you can't do anything with them. You need to first use your brain to transform them into corresponding "models" in your mind. This is why you extend two hands, one representing "4," and the other representing "3."

The hand gestures are "manipulable." For example, if you bend another finger on your left hand, it becomes "3." If you extend one finger, it becomes "5." Fingers are a quite good mechanical model, as they are movable and operable. Transforming the symbols "4" and "3" into finger models allows you to start calculating.

How do you know which finger model corresponds to "4" and "3"? Because mom taught you before. Ten fingers correspond to the numbers 1 through 10. This is why people use decimal numbers for arithmetic.

We don't need to delve deeper into this issue now. I just want to remind you to distinguish between "symbols" and "models."

### Calculation graph

Calculation process using finger models:

1. Convert symbols "4" and "3" into finger models.
2. Place the "4" finger model on the table.
3. Place the "3" finger model next to the "4" finger model.
4. Count the number of fingers on the "4" finger model (two hands with four fingers each = 8 fingers, subtract 1 for the base = 7 fingers). Add 1 to get the number represented by the "4" symbol (7 + 1 = 8).
5. Count the number of fingers on the "3" finger model (one hand with three fingers = 3 fingers).
6. Place the "3" finger model on top of the "4" finger model, aligning the fingertips.
7. Count the total number of fingers in the stack (8 fingers from "4" and 3 fingers from "3" = 11 fingers).
8. Subtract the number of fingers in the base hand (one hand with five fingers = 5 fingers).
9. Find the difference between the total number of fingers and the base hand (11 - 5 = 6).
10. The result is the sum of "4" and "3," which is "7" in the Arabic number system. Therefore, the calculation result using finger models is "7." In the field of computers, we often use some abstract diagrams to represent computational processes, allowing us to intuitively see the flow and transformation of information. These diagrams look like shapes connected by arrows. I call this kind of diagram a "computation graph" here.

For the finger arithmetic 4 + 3, we can represent it with the following diagram:

The arrows in the diagram indicate the direction of information flow. Regarding "flow," you can imagine the flow of water. Initially, we see numbers 4 and 3 flowing into a circle, inside which there is a "+" sign. This circle represents you, a child who does hand addition. Your mother gives you numbers 4 and 3, and you now add them up to get 7 as a result.

Notice that the input and output directions of the circle are determined by the arrows, and we can adjust the positions of those arrows as needed, as long as the connection relationships and directions remain the same. They don't have to be all from left to right; they could be from right to left or from top to bottom, but the input-output relationships are the same: 4 and 3 go in, and the result 7 comes out. For example, it could also be represented as:

We use a circle with a "+" sign to represent an "adder." As the name suggests, an adder can help us perform addition. In the previous example, you were an adder. We can also use other devices as adders, such as a pile of stones, a balance, or some electronic circuits... as long as they can perform addition.: Specifically how to do addition, it's just like specifically how you fold your fingers, we often don't care about it, we only need to know that this thing can do addition. A circle abstracts specific addition operations, this blue circle can represent many kinds of things. Abstraction is a crucial thinking method in computer science, it helps us think at a high level without being bothered by details.

Expressions:

Computer science is certainly not just about 4 + 3 being that simple, but its basic elements indeed are. We can create very complex systems, but fundamentally they only calculate things in some order like 4 + 3.

4 + 3 is a very simple expression. You might not have heard of the word "expression" before, but let's not define it yet. Let's look at a slightly more complex expression first:

2 * (4 + 3) (4 + 3)

The English translation of the given Chinese expression is: "four plus three". The expression inside the parentheses represents a mathematical operation where you add 4 and 3 together.: This expression has an additional operation compared to 4 + 3. We call it a "compound expression". This expression can also be represented using a computation graph:

Do you know why it looks like that? It means first calculating 4 + 3, then passing the result (7) to a "multiplier", multiplying it with 2, and getting the final result. So it is the same as the expression 2 * (4 + 3), and its result should be 14.

Why do we first calculate 4 + 3? Because when we see a multiplier 2 * ..., one input (2) is known, while the other input must come from the output of an adder. The result of the adder is obtained by adding 4 and 3, so we must first calculate 4 + 3 and then multiply it with 2.

In elementary school, you might have learned: "what's inside the parentheses is calculated first". In fact, parentheses are just "symbolic layer" things, they don't exist in the computation graph. The "computation graph" I'm talking about is the real thing. Mathematical parentheses and such are just symbols or called "syntax". From a certain perspective, the computation graph is the essence or "model" of the expression, while "2 * (4 + 3)" is just a representation or "encoding" (coding) of the computation graph.

Here we feel the difference between "symbol" and "model" again. The symbol is a "representation" or "encoding" of the model. We need to get the model from the symbol to operate. This process of converting from symbol to model is called "parsing" in computer science. We will understand this process in the following chapters. We now come to give a preliminary definition for expressions. This is not a complete definition, but you should try to understand this kind of definition. Later, we will gradually supplement this definition and perfect it.

Definition (expression): An expression can be one of the following things.

1. A number is an expression. For example, 1, 2, 4, 15, ...

2. An expression + an expression. The sum of two expressions is also an expression.

3. An expression - an expression. The difference of two expressions is also an expression.1. Expression * Expression. Two expressions multiplied together are also an expression.

2. Expression / Expression. Two expressions divided are also an expression.

Note that, due to the difference in symbols and models we discussed earlier, to fully adhere to our fundamental understanding, "Expression + Expression" here, although it looks like a string of symbols, must be imagined as its corresponding model. When you see "Expression" in your mind, you should imagine its corresponding computation graph, rather than a string of symbols. The image of this computation graph is roughly as follows, where the large rectangle on the left can contain any two expressions.

Does this definition feel a bit strange? Since we use "Expression" itself in the definition of "Expression," this is called a "recursive definition." Recursion refers to the fact that in the definition of a thing, we refer to that thing itself. It may look strange, as if we're going in circles. Recursion is an important concept, which we will delve deeper into in the future.

Now let's verify that according to our definition, 2 * (4 + 3) is indeed an expression: First, based on the first form, we know that 4 and 3 are expressions since they are numbers.

Therefore, 4 + 3 is an expression, as the definition of an expression's second form is satisfied because the left and right of the '+' sign are both expressions.

Likewise, 2 * (4 + 3) is an expression, as the definition of an expression's fourth form is satisfied because the left and right of the '*' sign are both expressions.

### Parallel Computation

Consider the following expression:
[Parallelizable expression: 2 * (4 + 3)]

This expression can be computed in parallel as follows:

1. Compute 4 + 3 in parallel to obtain 7.
2. Multiply 2 and 7 to obtain the final result, 14. (4 + 3) *

In English, this expression represents addition first, then multiplication, following the order of operations, also known as PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction). So, this expression should be calculated as:

1. First, perform the addition inside the parentheses: 4 + 3 = 7
2. Then, perform the multiplication: 7 * = 7.

Therefore, the result of the expression (4 + 3) * is 7. This corresponds to what kind of computational graph? Approximately like this:

1. Input
2. Operation (could be addition) if your mother has only one child, how should you use your fingers to calculate the result? You probably have two ways.

First method: first calculate 4+3, result is 7. Then calculate 1+2, result is 3. Then calculate 7*3, result is 21.

Second method: first calculate 1+2, result is 3. Then calculate 4+3, result is 7. Then calculate 7*3, result is 21.

Notice that, you either calculate 4+3 first, or calculate 1+2 first, you cannot calculate both at the same time. Why? Because you only have two hands, so when you are calculating 4+3, you cannot calculate 1+2 at the same time, and vice versa. In short, your mother only has one calculator, so she can only do one calculation at a time.

Now suppose you have a younger sister, who is about the same age as you, and she can also do finger arithmetic. Your mother now has more ways to calculate this expression. She can let you calculate 4+3, but before you finish, let your sister calculate 1+2. When both of your results (7 and 3) come out, let either you or your sister calculate 7*3. You don't have it, at some point in time, you and your sister are doing addition calculations simultaneously. This kind of calculation that overlaps in time is called parallel computing.

Your and your sister's calculation speed may be faster than yours alone. If your mother has several other children, calculating complex formulas could be much faster, which is the potential advantage of parallel computing. The term "potential" means this benefit may not be achieved. For instance, if your sister's finger counting speed is significantly slower than yours, you might finish 4+3 first, but then have to wait for her to slowly do 1+2. This might take longer than if you did 4+3 and then 1+2 sequentially.

Even if your sister does arithmetic as fast as you, there's still an issue. After you and your sister get results 7 and 3 respectively, you need to communicate the results to the next person for multiplication (it could be you or your sister). This "communication" brings time delay, called "communication overhead." If one of you speaks slowly, this might be slower than doing the computation alone.

How to maximize computing efficiency based on the differences in computing unit abilities and communication overhead, and reduce the required time, is the subject of research in the parallel computing field. Parallel computing, despite appearing complex, is understandable once you grasp the points mentioned here.

### Variables and Assignment

The text discusses parallel computing, where you and your sister perform addition calculations concurrently, resulting in potential time savings. However, this advantage isn't guaranteed, as your sister's slower calculation speed could make the process slower. Even if your sister calculates as fast as you, there's still the issue of communicating results, which introduces communication overhead. Efficiently managing parallel computing involves maximizing computing abilities and minimizing communication overhead. The research in this field is crucial for achieving significant time savings. if you have a complex expression, such as

(5 - 3) Six + Two = Eight Three minus one is two.
Five.: Due to having quite a few nestings, it is hard for human eyes to make out the meaning clearly. In such cases, you would like to use some "names" for the intermediate results, making the expression easier to understand.

For instance, this is similar to having a relative of yours. He is the husband of your mother's sister's daughter. You don't want to call him "the husband of my mother's sister's daughter" every time, so you use his name "Bengting" to refer to him instead, making it much simpler.

Let's look at an example. The previous compound expression:

[1, [2, [3, 4], 5], 6]

To make it clearer, you can give names to the intermediate results:

[A, [B, [C, D], E], F]

Now, it's easier to understand. Two
(
Four
+
)

The Chinese text provided seems to be a combination of numbers and parentheses, but it doesn't form a complete sentence or phrase in Chinese. Therefore, it's not possible to provide an accurate translation without additional context. The English translation provided above is based on the given numbers only. In fact, it can be transformed into an equivalent code with variables:

{

a =
} a = 4 + 3; // Variable a gets the value of 4 + 3. two
// code block value
}:

Among them, a is a name. a = 4 + 3 is an "assignment statement", which means: use a to represent the value of 4 + 3. Such a name is called a variable in computer terminology.

The meaning of this code can be simply described as: compute 4 + 3, represent its result as a, and then compute 2 * a as the final result.

Some things may have confused your sight. The text after two slashes// until the end of the line is called a "comment", which is explanatory text for human beings. It does not affect the logic of the code during execution and can be ignored. Many languages have similar comments, which can help the reader but will be ignored by the machine.

The execution process of this code will be as follows: first, compute 4 + 3 to get 7, remember the intermediate result 7 using a. Then compute 2 * a, which is 2 * 7, so the final result is 14. It is clear that this is the same as the result of 2 * (4 + 3).

a is called a variable, it is a symbol that can represent any value. Besides a, you have many choices, such as b, c, d, x, y, foo, bar, u21... as long as it does not cause misunderstanding.: If you feel that the "magic" factor in this place is too much, let's delve deeper in understanding....

Let's take a look at the code above once again. This entire piece of code is referred to as a "code block" or a "sequence." This code block consists of two statements: a = 4 + 3 and 2 * a. The statements in the code block are executed in order from top to bottom. Therefore, we first execute a = 4 + 3, followed by 2 * a.

The last statement 2 * a is particularly special; it is the "value" or the final result of this code block. All the previous statements are used to prepare for the generation of this final value. In essence, the entire value of this code block is the value of 2 * a. This is a general principle: the last statement in a code block is always the value of the code block.

We mark the statements within a code block using curly braces {...} for distinction, ensuring they do not get mixed up with the external code. These two curly braces are referred to as "delimiters." We will frequently encounter code blocks in the future, as they exist in almost all programming languages, albeit with slight variations in syntax. For instance, some languages may use parentheses (...) or BEGIN...END instead of curly braces to denote boundaries.

This code snippet is starting to resemble common programming languages, but I don't want to pin down your thought process. In future chapters, we will map this abstract expression to several common languages, enabling you to understand various programming languages. Outside of that, there's something else to note. The same variable can be assigned multiple times. Its value will change with each assignment statement. For example:

{
a = []
a = ["apple"]
a = ["banana"]
} Four equal to three.

However, the given Chinese text does not seem to contain any actual Chinese characters, but rather some symbols and numbers. The text "四" in Chinese means "four" and "三" means "three," so the intended meaning of the text is that "four is equal to three," which is not true in mathematics. Therefore, the English translation provided above is just an interpretation based on the given symbols and numbers, not an accurate translation of any Chinese text. a is equal to 2.

Or, in mathematical notation:

a = 2 five equals to

or

five is equal to: After executing this code segment, the value of b is 7, while the value of c is 10. Do you know why? Because after a = 4 + 3, the value of a is 7. Then, a = 2 * 5 changes the value of a to 10. Therefore, c = a results in a value of 10 for c.

Assigning the same variable multiple times is possible, but it is generally not a good practice as it may lead to confusion in the program. It should be avoided unless the meaning represented by the variable remains the same.

### Compile

Once variables are introduced, we no longer need compound expressions. Since any complex compound expression can be broken down into "single operation arithmetic expressions" (like 4 + 3), we can use variables to store intermediate results and calculate step by step to obtain the final result. I'll give an example that is a bit more complex, which is the expression at the beginning of this section:

(5 - 3)

So, this expression subtracts 3 from 5 to get the result. six + two = eight Three minus five equals:
Negative two It can be transformed into a sequence of statements:

{

    
}

Here is a possible English translation:

It can be transformed into a sequence of statements:

{

} a =
* 2 = 3

This text appears to be a series of symbols, and it's not clear what the intended meaning is. It does not appear to be a coherent Chinese sentence or phrase. b equals a minus 5

or

b is equal to a minus 5. cb *

This text does not contain any meaningful Chinese characters or words. The "c" and "b" are likely typographical errors, and the "=" and "*" may represent symbols or errors as well. Therefore, it is difficult to provide a clear English translation without additional context. six
=
four
+
two

Therefore, the result of the expression in Chinese characters "六" (six), "定" (=), "四" (four), "加" (plus), "二" (two) is the English number "eight" (6 + 4 = 10, 10 - 2 = 8). ce = 5

This looks like a simplified representation of the Chinese character "五" (wu), which means "five". The "ce" represents the sound of the character, and the "=" sign is likely used to indicate that the following number represents the value of the character. So, this can be translated to English as "five". three e d *

This text appears to be a sequence of characters from the Chinese language, but it does not form a coherent sentence or phrase. The English translation provided is an attempt to represent the sequence of characters as English letters based on their approximate shapes. However, without context or a clear meaning, this translation may not be accurate or meaningful. Last expression e * d, the result is the same as the original expression. Observe carefully, is every operation simple and does not contain nested compound expressions? You can verify it yourself, it indeed yields the same result as the original expression.

Here, we manually did the "compiler's" (compiler) work. Normally, a compiler is a program that translates a piece of code into an equivalent form. Here, we didn't write a compiler, but we did the compiler's work ourselves. We manually compiled a nested compound expression into a series of simple arithmetic statements.

The results of these statements are identical to the original expression. This translation process that preserves the original semantics is called compilation.

Why do we need compilation? There are several reasons. I won't give a comprehensive explanation here, but from this example, we can see that after compilation, we no longer need complex nested expressions. We only need to design a simple machine that performs only single-operation arithmetic, and it can calculate complex nested expressions. In fact, the last piece of code is already quite close to modern CPU assembly code. We just need to add some conversions for it to become machine instructions. We don't write a compiler yet, as you still lack some necessary knowledge. This is not the only content of compiling technology, it includes other things as well. However, from this beginning, you have already had a preliminary understanding of what a compiler is, you just need to deepen this understanding in the future.

### Function

So far, all our calculations have been done on known numbers. However, in real computing, we often have some unknown numbers. For instance, we want to express a "fan controller" where the fan speed is always twice the current temperature. This "current temperature" is an unknown number.

Our "fan controller" must have an "input" (input), used to obtain the current temperature t, which is a temperature sensor reading. It also needs an output, which is the temperature doubled.

Thus, we can express our fan controller in the following way:

function fanController(t) {
 return 2 * t;
} Do not consider this as any programming language, it's just our way of expression. The arrow -> on the left represents input, and the right represents output. Simple enough. You can imagine t as a wire coming from a temperature sensor, connected to a fan controller. The fan controller multiplies its input (t) by 2. This diagram looks like this:

When we talk about the fan controller, we don't care where its input comes from or where its output goes. If we remove the temperature sensor and fan from the diagram, it looks like this:

This diagram is the one you should pay attention to understand the function's computation graph. Do you see it? This diagram corresponds exactly to the symbolic representation of the fan controller: t -> t*2. Seeing the symbol brings up the image, giving you a model behind the symbol.

Constructs like t -> t*2, which have unknowns as inputs, we call functions. The symbol t in this function is called the function's parameter.

### Parameters, variables, and wires
[End of translation]

Imagine t as a wire from a temperature sensor, connected to a fan controller. The fan controller multiplies its input (t) by 2. This diagram represents:

When discussing the fan controller, we don't focus on where its input originates or where its output goes. If we eliminate the temperature sensor and fan from the diagram, it appears as:

This diagram is crucial for understanding the function's computation graph. Notice that it matches the symbolic representation of the fan controller: t -> t*2. Visualizing the symbol creates a mental model.

Function-like constructs, such as t -> t*2, which have unknowns as inputs, we refer to as functions. The symbol t in this function is called the function's parameter. You might have noticed that a function's parameters and the variables we have learned before are similar, they are both symbols. We used a, b, c, d, e before, and now we have a t. These names are arbitrary, as long as they are not repeated. If the names are repeated, it may cause confusion and interference.

In fact, the concepts of parameters and variables are not just similar, but their essence is the same. If you deeply understand their common essence, your brain can save a lot of memory, and it may help you make some interesting and beneficial transformations in the code. In the previous section, I used "wires" as an analogy to help you understand parameters. You can also use the same method to understand variables.

For example, our previous variable a:

{

// variable declaration and assignment
a = 5;

// function call with a as an argument
myFunction(a);

// inside the function, a is a local variable with the same name as the argument
function myFunction(a) {
 a = a * 2;
 console.log(a);
}

// after the function call, the value of the global variable a has been changed
console.log(a); // prints 10 a =
=========

4 + 3 =
=========

seven

So the English translation of the given Chinese text is "seven". The text represents the calculation of the sum of 4 and 3, which equals to 7. What kind of scene can it be imagined as?

The given Chinese text does not contain any numbers or characters that can be directly translated to English as provided. The text consists of special characters that do not have any meaning in Chinese or English context. I deliberately drew the arrow direction as from right to left in this diagram, making it more similar to the code above. From this diagram, you might be able to see the variable 'a' and the fan controller's parameter 't' in the figure. In fact, there is no essential difference between them. They both represent a wire, which enters the multiplier and gets multiplied by 2, then output. If you consider these as circuits, both variable 'a' and parameter 't' represent just a wire.

Furthermore, you also find another phenomenon. You can change the name of 'a' to any other name (like 'b'), but this diagram won't undergo any substantial change.

What does this imply? It implies that the following code (replacing 'a' with 'b') is equivalent to the previous one:

{

// (code with 'a' replaced by 'b')

} b equals 4 plus 3

=

The equal sign represents equality, so this expression means that b is the value that results from adding 4 and 3. Therefore, the answer is:

b = 7 based on similar name changes for the wires, you can draw the same conclusion for the previous function: t -> t*2, u -> u*2, and x -> x*2 are equivalent. I. Importance of Names
Names are important things, but for machines, specifically what they are called has no real significance as long as they don't confuse each other. However, names are crucial for humans because our brains are not as precise as machines. Poor variable and parameter names can make code hard to understand, leading to confusion and errors among programmers. Therefore, it's generally advised to give variables and parameters good names.

II. Named Functions
Since variables can represent "values," a natural thought is to let variables represent functions. Thus, just like we can write:

a = function() { ... }

### 有名字的函数 (continued)

我们也可以写:

function name() { ... }

这种写法被称为“有名字的函数”或“声明函数”。它们有以下优点:

1. 可读性更好: 有名字的函数更易于理解，因为函数名可以描述函数的功能。
2. 调用更方便: 有名字的函数可以直接被调用，而无需记住它们的位置。
3. 重用更容易: 有名字的函数可以被多次使用，并且可以被其他文件或模块引入。

因此，建议使用有名字的函数，而不是使用“函数表达式”或“匿名函数”。

III. Conclusion
In conclusion, names are essential for both humans and machines, but they serve different purposes. For humans, clear and descriptive names help improve code readability and maintainability. For machines, names are used to differentiate between variables and functions. By giving variables, parameters, and functions good names, we can make our code more understandable, maintainable, and reusable. We can apparently also write
4 + 3 =

So the answer to the equation is 7. Therefore, the English translation of the Chinese text without any Chinese characters or punctuation would be:

FOUR PLUS THREE EQUALS SEVEN. f becomes t, then t remains the same.

Therefore, the sequence remains as "t". No translation is needed.: Yes, you can do that. An alternative traditional way for defining f as a function is:

f(t)

(where t is the input) please carefully observe the position of t. We write a pair of parentheses to the right of the function name and put the names of the parameters inside.

Note that you cannot just write:

Therefore, the correct format should be:

functionName(parameter1, parameter2, ...)

So, in your case, it should be:

t(x, y) You must clearly specify the parameters of the function, otherwise you won't understand what t is in the function definition. By clearly stating that t is an "input", you will know that it is the function's input, an unknown value, rather than a variable defined outside the function. This seemingly simple principle, many mathematicians do not understand, hence they often write books in such a way:

There is a function y = 2x

This is incorrect because he has not explicitly stated "x is the parameter of function y". If they have defined x beforehand, you would be confused whether it is the previous x. Many people fail to understand mathematics due to such ambiguous writing. This is not their fault, but that of mathematicians themselves for not being precise in language.

### Function Call

With a function defined, how do we use its value? due to the function containing unknowns (parameters), you must inform it of these unknowns for its code to execute and give you the result. For instance, the fan controller function from before:

function
(
t
)
 =
 t
[

In English:

Because the function contains unknowns (parameters), you must provide it with these unknowns for its code to execute and return the result. For example, the fan controller function:

function (t) = t It requires a temperature as input to give you an output. So you give it an input as follows:

f (2)

[In English, this is a representation of a function call in a programming language, where 'f' is the name of the function, '2' is the argument, and the parentheses '()' denote the function call.] You put the input in the parentheses of the function name. Therefore, you will get the output: 4. This means the value of f(2) is 4.

If you haven't called a function, the function body will not be executed because it doesn't know what the unknown number is, so it can't do anything. So when we define a function, for example:

f(t)
{
}[Function body]

Here is the English translation without any Chinese characters or punctuation:

You put input in function name parentheses. Therefore, you will get output: 4. This means the value of f(2) is 4.

If function not called, body not executed because unknown number not known. So when define function, for example:

f(t)
{
[Function body] When encountering this definition, what should the machine do? It only records: there is a function, with parameter t, it needs to calculate t*2, its name is f. However, the machine does not immediately calculate t*2 because it does not know what t is.

### Branching

So far, our code has been executing from start to finish without questioning anything. We lack a way to "ask questions." For instance, if I want to express this "food selector": if temperature is below 22 degrees, return "hotpot" representing eating hotpot today, otherwise return "ice cream" representing eating ice cream today. We can represent it as follows:

This kind of judgment structure is called a "branch" (branching), which is usually represented by a diamond shape. Why is it called a branch? Imagine that the code is like a small stream, flowing along a certain path. When it encounters a clearly defined large stone, it splits into two streams and flows separately.

Our judgment condition t < 22 is like a large stone. Our "code stream" encounters it and splits into two branches, each doing different things. Unlike the stream, this branching is not random but determined by conditions, and only one branch continues to execute while the other is not.

Now that we're looking at a graphical representation of the model for convenience, we need a symbolic representation to express this model. We need a symbolic representation for branching, which we call "if" (if). Our beverage selector code can be written as follows:

t
if t < 22:
<actions for t < 22>
else:
<actions for t >= 22> if (t < ) {

This appears to be an incomplete if statement in Chinese characters. The English translation of the given characters would be:

if (t < [some condition]) {

Without the complete condition in square brackets, it's impossible to provide an accurate translation. "hot pot" elses

{

if (condition) {
// code for if condition is true
}

} else {
// code for if condition is false
Console.Write("ice cream");
}

}

// In English, the text translates to:

if (condition) {
// code for if condition is true
}

else {
Console.Write("ice cream");
} This is a function that takes in a temperature. The condition in the if parentheses is our judgment condition. After that comes the code block that executes when the condition is met, followed by an else, and then the code block that executes when the condition is not met. It says: if the temperature is below 22 degrees, we eat hot pot, otherwise we eat ice cream.

The else here is a special symbol, it means "otherwise". You might wonder why else is there? Yes, we already have enough expressiveness to distinguish the two branches, but having else makes it look nicer. Many languages have this "else" marker word there, so I put it there as well.

This is just a simple example, in reality, those two code blocks can contain any number of statements, like this: if (t < ) {

This appears to be an incomplete if statement in Chinese characters, likely due to missing characters or formatting issues. The English translation would be:

if (t < [some condition]) {

Without the missing condition, it's impossible to provide an accurate translation. Two and two
=
equals

This text appears to be a fragment of code written in a programming language, likely in a comment or documentation. The English translation is: "Two and two equals". Four
Plus
Three

Beneath "hot pot" Else,
{
 x
} Both this code and the previous one are equivalent. Do you know why?

The Chinese text translates to "ice cream" in English. The code snippet provided does not seem related to the Chinese text.: String

In the previous section, there appeared something new and unfamiliar to us, which I did not introduce for the sake of simplicity. The results of these two branches, that is, "hotpot" and "ice cream" with quotes, are not numbers, nor are they other language constructs, but a type of data called a string (string). A string is the fundamental data type for representing human language in computers.

Regarding strings, I do not want to delve into more detailed content here. I will leave the various operations on it for later, as strings are very important for application programs, but they are not the most essential and fundamental concepts in computer science.

Many computer books start by discussing many operations on strings, resulting in beginners spending a lot of effort on printing string exercises, only to find out several weeks later that they have not yet learned the concept of "functions" and other fundamental concepts. This is a shame.

### Boolean values

However, let's move on to another topic: Boolean values. Boolean values are the simplest and most fundamental data type in computer science. They only have two possible values: true and false. In programming, we often use Boolean values to make decisions and control the flow of a program. For example, we can use an if statement to check if a condition is true or false, and then execute different code based on the result.

Boolean values are named after the English mathematician George Boole, who first proposed the concept of Boolean logic in the 19th century. Boolean logic is a type of logic that deals with Boolean values and their operations, such as AND, OR, and NOT. In programming, we often represent Boolean values using keywords like true, false, or boolean variables.

Let's look at an example of using Boolean values in Python:

```python
# Define a Boolean variable
is_hot = True

# Use an if statement to make a decision based on a Boolean value
if is_hot:
  print("It's hot outside.")
else:
  print("It's not hot outside.")

# Use Boolean operators to combine multiple conditions
if is_hot and not rain:
  print("Let's go to the beach!")
else:
  print("Let's stay home and watch a movie instead.")
```

In this example, we define a Boolean variable `is_hot` and use it to make a decision using an if statement. We also use Boolean operators `and` and `not` to combine multiple conditions.

Boolean values are used extensively in programming, and understanding how to use them is essential for writing effective and efficient code. We have discussed the if statement's condition t < 22 in the past, which is actually an expression called a "boolean expression". You can think of the less than symbol < as an "operator" similar to addition. It takes two numerical inputs and outputs a "boolean value". What is a boolean value? A boolean value only has two possibilities: true and false, or "true" and "false".

For example, if t's value is 15, then t < 22 is true, so its value is true. If t's value is 23, then t < 22 is not true, so its value is false. Is it clear now?

Why do we need "boolean values" then? Because their existence simplifies our thinking. There are also operations for boolean values, which I won't go into detail about in this chapter.

### Computational Elements

Now that you have learned almost all the fundamental elements of computer science. Every programming language includes these constructs: 1. Basic values. For example, integers, strings, boolean values, etc.

2. Expressions. Including basic arithmetic expressions, nested expressions.

3. Variables and assignment statements.

4. Branching statements.

5. Functions and function calls. You may feel that I have arranged these constructs in a "from small to large" order. This may help your understanding.

Now you can recall your impressions of them. Whenever you learn a new language or system, you only need to find the corresponding constructs within it, without having to start from scratch. This is the secret to mastering all programming languages. This is like learning to drive a car. Once you have mastered the functions and uses of the gas pedal, brakes, transmission, steering wheel, and speedometer, you can drive any car, no matter what its model.

In this chapter, not only have we understood these elements, but we have also defined a language of our own for them. Obviously, this language can only run in our minds, as we have not implemented this language's system. In the following chapters, I will gradually map our language to various existing languages, and then you will be able to master these languages.

However, please do not think that mastering a language makes you a programmer or a computer scientist. Mastering a language is like understanding the working principles of various car parts. A beginner can make a car move, turn, and stop within a few minutes. However, after that, you need to learn traffic rules, and you need a lot of practical experience and strategies to handle various complex situations. If you want to be a race car driver, it will take even more effort.

However, please do not be intimidated by my words. Currently, there are not many qualified computer science drivers, let alone those who can drive smoothly like race car drivers. Most "programmers" don't even understand the basic workings of an engine, gas pedal, brakes, and steering wheel, let alone the thinking patterns required to go solo, leading to accidents on the road. Many people blame their cars for their mistakes and think that buying a new car will make them good drivers. This is a failure of computer education on a global scale. In the following sections, I will guide you to become a qualified driver, able to drive any car with ease. But what is calculation? I haven't told you that yet. This is a very philosophical question, and different people may give you different answers. I will try to tell you the answer from the most general perspective.

When you were a child, and you used your fingers to calculate 4+3, that was calculation. If later you learned to use an abacus and calculated 4+3 with it, that was also calculation. Later, when you learned expressions, variables, functions, calls, and branch statements from me, in each new construction you learned, you were learning different kinds of calculation.

So, from the most general perspective, calculation is "mechanized information processing." Mechanized means you can use your fingers, an abacus, a calculator, or a computer. These machines may contain code or not, be made of electronic circuits, or even be biological activities or chemical reactions. Different machines may have different calculation functions, different speeds, and different performances....: You may find it confusing having so many ways to compute, always fearing that you might have missed something. But if you have grasped the "computational elements" from the previous section, then you have acquired almost everything required for various types of computing systems. All you need to do next is to deepen this understanding and apply it to different types of computing machines in reality.

Why can you trust that the essence of computer science is just these things? Because computation is about processing information, and information has its birthplace (input devices, constant values), its transmission methods (assignment, function calls, return values), and its viewing places (branches). You can't think of anything else regarding information, so you feel reassured and believe that these rules are the entirety of the "chess-like game" that is computer science.

(If you find this article inspiring, please click here to pay.)