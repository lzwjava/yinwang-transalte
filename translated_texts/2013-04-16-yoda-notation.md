---
layout: post
title: "yoda-notation"
---

 In the last blog post, I mentioned Yoda notation.

### Yoda Notation (Yoda style)

It means using this expression order in C/C++:

if (theSky == "blue") ... this is written as:

if (theSky == "blue") ...

The name of "Yoda style" comes from the "Star Wars" character Yoda. He speaks in a peculiar order of words, such as: "Backwards it is, yes!"

### In general,

Using this style is considered a "workaround" (workaround) for one of C/C++'s design choices: using = to assign values, and using == to compare. This design fully embodies the essence of "Sins of our Forefathers" (Sins of our Forefathers). I believe that

using = for assignment is not the real error. The real error lies in the fact that C/C++ assignment statements should not return a value.

Therefore, theSky = "blue"'s entire functionality should only be "assignment" with the "side effect," and the side effect should not have a "value." Even if you forcefully associate it with a value, its "value" should be void (and this void will be rejected by type checking since it is not the boolean expected by if). So, a good language should not allow you to put theSky = "blue" in the "condition" of if (...). If you really need to assign and judge, it will force you to split it into two lines:

theSky = "blue";
if (theSky) ...:

Step closer. This writing style of "if (theSky)" is actually an error of an elder. theSky's type is string, it shouldn't be able to be used directly as a bool. The condition of if (...) should necessarily be a bool. So here, it should actually be written as:

theSky = "blue";
if (theSky != NULL) ...

Since an assignment statement can never appear in the position of a condition, the error in the previous way, even if we use = as an assignment operator, is completely impossible. Therefore, we also no longer need to use Yoda style.

On the contrary, if we only change = to a Pascal-style := assignment operator while keeping other features (assignment operation returns a value), we will still encounter the same problem:

if (theSky := "blue") ... In this scenario, if you meant to type "=", but accidentally typed ":=" instead. The chances may be small, but there's still a possibility. My recommended solution, however, would prevent you from making such mistakes intentionally, as the compiler would reject your program.

Thus, you see that the problem doesn't lie in the name of the assignment operation, but rather has deeper reasons.