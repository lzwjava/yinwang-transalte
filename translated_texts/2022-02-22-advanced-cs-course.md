---
layout: post
title: "advanced-cs-course"
---

I've been pleased with the positive feedback received since the establishment of the computer science fundamental class (group class, one-on-one, reading class). I've seen many students with no prior knowledge learn the essential parts of computer science from scratch. This has greatly inspired me. Based on my own exploration and the various social issues I've encountered, I've realized the value and significance of education once again.

Given this background, I've had the idea to set up an advanced computer science class for some time. A 13-year-old student, the "little mouse," tried a lesson and was able to learn some things that were once only accessible to PhD students in a short time. I've also tried impromptu teaching a friend the cello. Although she had never touched a cello before, she was able to play the first part of Bach's Prelude after only an hour. Of course, it was still not smooth, but the principles had been grasped, and continuous practice would lead to further improvement. Master the fundamentals, improve continuously. The master opens the door, practice in seclusion. I feel this is the true meaning of education that I have understood.

Regarding the computer science advanced class, I don't have a very specific content and plan yet, but the situation was similar when I first set up the fundamental class. Besides the content of the first two lessons, the rest was mostly improvised based on the teaching situation. However, I think it's best to roughly outline some content to give students a sense of direction.: Course Outline:

Approximate content scope as follows, which may be temporarily updated or deleted based on the situation:

1. Basics of CPS (continuation-passing style) transformation. Understand from scratch what CPS is.
2. Implementing concurrent program execution using CPS. Understand processes, threads, and the so-called "big concurrency" in operating systems based on the unified concept of continuation. Use Scheme language for later content as it has a clean design. Students will implement recursive functions in Scheme and then write a simple interpreter using it. 1. Understand and implement call/cc operator. Understand what call/cc is and personally implement the call/cc operator in Scheme language, not just using it. Then use call/cc to do something interesting, like implementing concurrency.

2. Understand and implement "automatic CPS transformation". This is what people often refer to as "Wadler's 40 lines of code", which automatically converts a normal program into CPS form. Students will understand its principle and implement automatic CPS transformation themselves.

3. Use the idea of "automatic CPS transformation" to implement a micro-compiler. This area is called "compiling with continuation". It uses CPS transformation, ANF, etc. as theoretical foundations to design compilers, instead of the traditional way. Although the language of this compiler is very simple, it reveals the essence of compilers, understanding it will help students write complex compilers in the future. If interested, students can extend this language by themselves.

4. Logic programming (logic programming) fundamentals. Understand and implement a simple logic programming language similar to Prolog. From the root, understand logic programming. Use logic programming thinking to implement Hindley-Milner type system in OCaml and Haskell.

5. Program formal verification. Learn to use Coq formal proof system. Different from program testing, through formal verification, we can completely ensure the correctness of the program. Through simple examples, I will explain the fundamental ideas and principles of formal verification. To some extent, these ideas are the essence of mathematical proofs. Course outline, should have at least 8 sessions. There will be a dedicated communication group for the course. Students can discuss their understanding and findings in the group after each session. I may come up with some exercises for everyone, but this course is more like a graduate level in a university, so the main focus after class is open research methods for thinking and exploration rather than fixed exercises. I might suggest some papers for everyone to read, or try something new myself, or explore students' interested directions, or do some small engineering practice.

### Fee standard

Due to the difficulty of the content, I'm not very sure if 8 sessions can fully cover these topics and might exceed. I plan to charge 1024 RMB per session. The unit cost of course time fees is lower than the basic class. The initial fee is 8192 RMB, including 8 sessions, each session 2 hours long. Although I will try to condense it, if unable to complete in 8 sessions, I might continue for 1-2 sessions without additional fees.

### Enrollment method

[The text does not provide information on the enrollment method.] only students who have graduated from the basic course are eligible for this program. Students who have graduated from the basic course can register by sending a WeChat message to me. Please note, do not use WeChat for payment. Advanced course has high requirements for the foundation, and the program does not accept students who have not attended the basic course or have not completed it.