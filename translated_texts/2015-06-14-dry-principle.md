: Principle mistakes of DRY

Many programming people love to advocate various "principles," such as KISS principle, DRY principle.... Some people regard these principles as dogmas or recipes, believing that blindly following these will produce good code. At the same time, they look down on those who do not follow or disregard these principles, labeling them as novices. One of these dogmas is called the "DRY principle" (Don't Repeat Yourself, don't repeat yourself). Blindly believing in the DRY principle has brought about various problems in practical engineering, yet it is often overlooked.

In essence, the DRY principle encourages abstracting code, but it has been over-emphasized. The DRY principle states that if you find repeated code, extract it and make it into a "template" or "framework." I am in favor of abstraction, and many language experts have done extensive research on designing better abstractions. However, I do not blindly follow the so-called DRY principle, and it is not about avoiding "repetition" at all costs. "Avoiding repetition" is not the same as "abstraction." Sometimes, repetitive code is beneficial, so I intentionally engage in repetition.

### Abstract vs. Readability Dilemma

The "abstractness" of code and its "readability" (intuitiveness) are actually in a contradictory relationship. Moderate abstraction and avoiding repetition are beneficial, and it can even improve code readability. However, if you extract templates from the code to an extreme, even extracting insignificant "commonalities" for "sharing," it becomes harmful. This is because templates are not directly visible at the "calling" locations. Extracting templates often makes it difficult to read the code at a glance. If the loss of intuitiveness caused by this outweighs the benefits of the templates, you should consider avoiding abstraction. Remember, the number of times code is read far exceeds the number of times it is written. Many people extract unnecessary templates prematurely for the sake of "writing quickly," but in fact, they have lost readability in the process. If you cannot understand your own code at a glance, you cannot write elegant code. An example: A person following the DRY (Don't Repeat Yourself) principle often extracts "common fields" from a class, puts them in a parent class, and makes the original classes inherit from this parent class. For instance, the initial code might look like:

class A {
 int x;
 int y;
 // some methods using x and y
}

class B {
 int x;
 int y;
 // some methods using x and y
}

// After applying DRY principle:

class Parent {
 int x;
 int y;
}

class A : Parent {
 // some methods using x and y
}

class B : Parent {
 // some methods using x and y
} int
x;

This appears to be a fragment of C or C++ code, likely declaring an integer variable named "x" and initializing it to zero. The semicolon at the end of each line indicates the end of the statement. The first and third lines are empty and do not contribute to the meaning of the code. int // empty line
{
 class // class keyword

} // class closing brace. This code snippet appears to define an empty class in C++. b
{
 int
 a;
} I. int

II. int executing DRY principle people prefer to refactor it as follows:

class
C
{
// code here
}

// DRY stands for "Don't Repeat Yourself" principle in software development. I. int a; // declaration of an integer variable named 'a'

The given Chinese text is actually not valid Chinese code, but rather some random characters mixed with English code. Therefore, it cannot be translated into Chinese from the provided text. Instead, I have assumed you meant to ask for an English translation of the given English code snippet. Class A extends C {

In English, the given Chinese text translates to:

Class A extends C { int

;

int

This text appears to be incomplete and contains no discernible Chinese characters. The given text is written in a programming language syntax, specifically in C or C++, and does not contain any Chinese characters. class B extends A {
// or
// Class B extends Class A {

// code for class B goes here

} C
{
 int u;
}; The following code has issues. The problem is that when you see the definition of class A and class B, you can no longer easily see the int a field. "Visibility", which is important for programmers, is crucial. This unnecessary field actually doesn't need to be declared as a new parent class most of the time. Even though there are similar int a fields in different classes, their meanings can be completely different. Some people add "DRY" (Don't Repeat Yourself) without thinking, but it doesn't bring benefits and instead makes the program harder to understand.: Abstract design issues

People who follow the DRY (Don't Repeat Yourself) principle still face a problem: they constantly try to find "potentially reusable" code instead of waiting until it actually repeats before abstracting. They often extract what seems like a "classic template," only to find out later that it has only been used once in all the code. This is because they abstracted too early.

The idea of abstraction lies in "discovering that two things are the same." However, many times, you may initially think that two things are the same, but later find out that they are only superficially similar, with fundamentally different natures. The same int a can represent many different properties. You see int a and propose making it a parent class, but in reality, this makes the program's concepts more confusing. Sometimes, things that seem similar at first may have different purposes after adding new logic, leading to splitting them apart. Prematurely extracting templates can tie your hands and feet, forcing you to repeat unnecessary things in the name of "consistency." This consistency, however, is not as effective as handling each situation separately.

Preventing premature abstraction is simple: it's called "waiting." Even if you don't reuse code, you won't die from it. Time will tell all. If you feel like you're repeating code you've written before, don't stop; keep writing it out. If you don't write it out, you won't be able to accurately identify repeated code, as they might not be identical in the end.

You should also avoid abstracting without practical effect. If the code is repeated only twice, don't start extracting templates; you might find out later that this template was used only twice in total! Repeating code only twice is usually not worth extracting a template for. The template itself is code, and abstract thinking requires a certain cost. Therefore, the total cost might be less if you just let those two repetitive sections stay. I like a lazy, dumb feeling. Since I'm lazy, I don't think about code reuse prematurely. I wait until it's proven that reuse will bring benefits before extracting templates and abstracting. Experience tells me that every time I actively seek abstraction, the final result is unnecessary templates, making my own code hard to understand. Many people overemphasize DRY, emphasizing code "reuse," and constantly thinking about abstraction, resulting in a jumbled mind, bugs galore, and slow progress. If you can't write "usable" code, what's the point of "reusable" code?

### Cautious approach to so-called principles

I've said a lot, am I for or against DRY then? In fact, it doesn't matter if I'm for or against it, because they all show that I care about it, and the truth is, I don't care about these principles at all, because they are very superficial. It's like you telling me about a major discovery that "1+1=2," should I support or oppose you? I'm too lazy to argue with you. People write programs and naturally abstract and avoid repetition at appropriate times, how is it that after several decades, a novice's approach became known as DRY, and he became a "master"-like figure, I'd rather use "DRY" to describe what I've been doing all along. So I don't want to mention "DRY" at all.

Therefore, I believe that this DRY principle should not even exist, it's a principle that's not worthy of being called a principle. Look at the other low-grade things he advocates (such as Agile, Ruby), you'll find that he is a "software engineering expert" selling weight loss pills. The world has too many shallow principles, I don't want to evaluate them one by one, it's a waste of my time. The world has many deeper software engineering experts who understand the true fundamental principles.