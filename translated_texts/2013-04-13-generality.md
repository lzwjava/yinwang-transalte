---
layout: post
title: "Speaking of a Program's 'Generality'"
---


In real software engineering, I often encounter such a phenomenon. A problem that could be solved with simple code is made complicated because the designer excessively focused on "generality," "maintainability," and "scalability."

These people's thought process is as follows: "This code segment might be used in more situations in the future, so I will consider extension issues now." Thus, they added various "framework structures" in the code to enable it to be used in new places "without modification" in the future.

I don't deny the value of "generality," in fact, some of my programs have very strong generality. However, many people's notion of "generality" often results in an opposite effect. This phenomenon is commonly referred to as "over-engineering." Regarding over-engineering, there is an interesting story:

http://www.snopes.com/business/genius/spacepen.asp I. Legend has it that during the 1960s space race between the US and Russia, NASA faced a serious technical issue: astronauts required a pen that could write in the vacuum of outer space. Eventually, NASA spent 150 million dollars to develop such a pen. Unfortunately, this type of pen did not sell well in the market.

The Russians encountered the same problem and used pencils instead.

Although this story is false, it possesses the power of Aesop's fables. Now let's take a look at our software industry:

1. In cases where code needs to be "reused," you might find that it's less common than you imagine. Many programmers do not prepare for edge cases beforehand and instead focus on envisioning others using their code. However, due to their complex designs, the mental effort required to understand these designs exceeds the cost of starting from scratch. Consequently, most people don't end up using their code and instead write new code themselves. Some even discover that their previous code is unreadable and wish they had started anew.

2. The work required to modify code is often less than you might imagine, especially when it comes to code designed to be "shared." In many cases, these codes are not used extensively, so even if you manually modify them, it won't take much time. With the advancement of IDE technology and various refactor tools, mass-modifying code is no longer a daunting task. Designing for maintainability used to require changes at the logical level, but now it might only require a few clicks in an IDE. Therefore, when considering designing a framework, you should also consider these factors. 1. Considering universality, it does not necessarily mean that you have accurately "grasped" its universality. Many people have considered universality but have not accurately identified which part may need modification in the future, so their designs often miss the mark. When new requirements emerge, they discover that what they had imagined as potentially changeable parts were actually unchanged, while what they thought would not change had in fact changed. Predicting future requirements and abstracting out authentic frameworks from the code is a challenging task. It requires not only programming skills but also a powerful observational ability. Many frameworks designed by people are in fact just imitations of others' experiences and cannot adapt to real-world needs. Many design patterns in the Java world fall into this category.

2. The complexity of initial design, if the consideration for future changes is prematurely introduced in the initial design, may result in unnecessary complexity and potentially lead to issues with the initial design. This consideration for future changes, in reality, has hindered progress. Instead, focusing on solving the current problem could yield excellent results. However, due to the complexity introduced by "universality," the designer's mind must constantly make detours, preventing the creation of elegant programs.

3. The cost of understanding and maintaining framework code if you design framework code, each programmer must understand the construction of this framework to write code within it, resulting in a learning overhead. Once a design issue is discovered in the framework, the code dependent on it may require modification, leading to additional modification costs. Therefore, the overhead introduced by "universality" can be significant. Whether this overhead can be recouped depends on various factors.

So, when designing software, it is best to first address the issues at hand. If it turns out that this code can be used in other places, the framework can be abstracted out at a later time.