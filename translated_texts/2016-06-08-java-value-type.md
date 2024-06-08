---
layout: post
title: "Does Java have value types?"
---


Someone read my previous article 'Design Flaws in Swift Language' and asked me: "You said Java only has reference types (reference type), but according to Java's official documentation, Java also has value types and reference types. For example, int, boolean are value types." Now I will explain this issue.

Java does have value types, and original types like int, boolean are value types, but this is a long-standing misunderstanding that confuses implementation and semantics. Don't be fooled by Java's official documentation; it's not the gospel truth that allows you to call Wang Cheng "stupid" :) When you think Wang Cheng doesn't understand a basic question, always think twice, because he might be wise beyond your expectations.... After my explanation, you might find yourself questioning whether Java's designers truly understood this issue :P

Now for the main point. Java, along with Scheme and other languages, has primitive types like char, int, boolean, double, etc., which are indeed passed by value (rather than reference or pointers) in implementation. However, this is just an optimization technique (called inlining). This optimization should be transparent to programmers. Java inherited this from Scheme/Lisp, which in semantics don't actually have value types.

This isn't a mind-bending concept. To understand this, try an interesting mental experiment. Imagine all the primitive types in Java as reference types, meaning all int, boolean, etc., variables don't contain actual data but instead reference (or pointers) to heap-allocated data. You'll find that this "modified" Java still conforms to all observable phenomena in existing Java code. In other words, whether primitive types are treated as value types or reference types makes no difference to programmers. I'll give you a simple example, if we change the implementation of int to be completely a reference, let's look at this code:

int x = 1; // x points to memory address A, containing integer 1
int y = x; // y points to the same memory address A, containing integer 1
x = 2; // x points to another memory address B, containing integer 2. y still points to address A, containing 1.

Since we have transformed Java such that all ints are references, the first line definition of x doesn't hold an integer but a reference, pointing to a heap-allocated memory block, with the content being integer 1. The second line defines int variable y, which is also a reference, and since its value is the same as x, y also points to the same address, with the same content: integer 1. In the third line, we assign a new value to x reference. You will notice an interesting phenomenon: although x points to 2, y still points to 1. Assigning a new value to x doesn't change the content y points to, which is the same as when int was a value type! So, even though int variables are now references, you cannot achieve what reference types can do: modify the content y points to by performing some operation on x.

This phenomenon occurs because, although int has been transformed into a reference type, you cannot perform reference-specific operations (which value types don't have) on it. These operations include:

[1] Reassigning the reference: x = new Int(5);
[2] Creating a new reference with the same content: Int z = x;
[3] Changing the content through the reference: x.setValue(10);

However, since int is now a reference, you can still perform operations like comparing references (==), passing references as function arguments, or using references in collections.1. Dereferencing is similar to the *operator in C language.

2. Member assignment. Like setting x.foo to 2 in C.

In Java, you can't write code like *x = 2 in C as Java doesn't provide a deref operator*. You also can't change part of the memory data (which is 1) that x points to using x.foo = 2 since int is a primitive type. After executing x = 2, the memory space where the number 1 originally was hasn't changed to 2, only x itself now points to a new address with the number 2. Other reference variables like y that point to the original address won't see 2 because of your x = 2 operation; they still see the original 1....

In this kind of Java where int is a reference type, you can only do two things to the int variable x:

1. Read its value.: 1. Perform an assignment to point it towards another location.

These two things are no different from what you can do with value types in your case. That's why you cannot change the value represented by y through the manipulation of x. Regardless of whether int is implemented as a pass-by-value or pass-by-reference in actual implementation, they are semantically equivalent. In other words, whether a primitive type is a value type or a reference type, for a programmer, it makes no difference. You can treat all Java primitive types as reference types, and the things you can do with them, your programming thought process and methods, will not change as a result.

From this perspective, Java, in terms of semantics, does not have value types. If value types and reference types coexist in a language (such as C#, Go, and Swift), a programmer must be able to sense their difference semantically. However, as a programmer, you cannot sense any difference between them, regardless of whether primitive types are value types or reference types. So you can completely treat Java as having only reference types, using them all as reference types, although they are indeed implemented as values.

A language that is semantically value-typed (such as C#, Go, and Swift) must have one or both of the following features for a programmer to feel the presence of value types:

1. deref operation. This allows you to use *x = 2 to change the content pointed to by a reference, causing other shared references to see the new value. You cannot change the value of another value variable to a new value using x = 2, so you feel the presence of value types. 1. Structs, like the ones in C, are "compound value types." You can change part of a referenced data (such as a class object) by using x.foo = 2 for member assignment, making other shared references see the new value. However, you cannot give a new value to another struct variable through member assignment, making you feel the existence of value types.

2. In reality, all data is reference types according to the initial design principles of Scheme and Java. Passing raw types as values is just a performance optimization (called inlining), which should be transparent to the programmer. Those who ask in interviews, "Is Java all data reference types?" and correct you when you answer "yes" by stating "int, boolean are value types," are purists.

### Pondering Question

Some argue that Java's reference types can be null, whereas original types cannot, so reference types and value types are still distinct. However, this does not negate the perspective presented in this article. Can you think of why?