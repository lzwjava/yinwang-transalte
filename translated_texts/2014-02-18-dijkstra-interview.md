---
layout: post
title: "A interview video about Dijkstra"
---


(You can also visit YouTube or download MPEG1 from the source address, 300M)

I previously recommended on Weibo a video interview with Dijkstra, and after watching it twice, I really think it's great, so I'm formally recommending it again. Most people are probably familiar with his contributions to graph algorithms and operating systems, but in fact Dijkstra's influence on programming languages is also profound. The common programming languages we use today have "recursive functions" which were pushed through Algol 60 despite opposition and doubts from the committee, leading to their inclusion in Pascal, C, Java, and so on. McCarthy was absent at the time, which would have resulted in three people supporting it instead.

Now it's hard to imagine any language without recursive functions, but during the 1950s and 1960s, it was actually quite rare for people to know what use it had! So you'll find that so-called "mainstream" and "majority" are often quite foolish. The same thing is happening to lambda now. In the future, a language without lambda will be unacceptable.

Here I'll just quote a few points he mentioned. Some opinions may not be the best approach, but I believe there are valuable learning opportunities in them. 1. The software's version numbers 2.6, 2.7, and so on are nonsense. Initially, the first version should have been the final product. However, software companies always release incomplete versions first, tricking people into buying, then gradually "upgrading." Each upgrade requires users to pay again.

2. There are various programming styles, and I categorize them as "Mozart vs Beethoven." When Mozart began composing music, the work was already complete. His manuscripts were well-written and neat. Beethoven was different; he constantly doubted and struggled. His compositions were generally not well thought out before starting, and he would add sticky notes to modify them. Once Beethoven revised a manuscript nine times, and someone later peeled back the layers to find that the first and last versions were identical. This "revise and revise" approach is a tradition of the Anglo-Saxon race, permeating British education.

3. A composer's job is not to write sheet music, but to conceive music. In the early days, people programmed using assembly language, which was similar to writing sheet music. Later, they invented high-level languages, thinking they had solved the problems of programming. But upon closer inspection, you find that they only solved the most insignificant problems. The difficult problems still remained. These high-level languages, combined with increasingly grandiose ambitions, ended up making programmers' mental burden even heavier.

4. Professional programmers know that their heads' size is limited, so they approach their work humbly, avoiding small cleverness like avoiding a plague.

5. When I gave a lecture on how to program in Paris, France, in 1970, it was very successful, with an eager audience. However, my lecture in a large software company in Brussels, Belgium, was a complete failure. It was probably the most failed lecture of my life. Later, I realized why: the management didn't like persistent programming because the company survived on software maintenance contracts. Programmers were uninterested because the most exciting thing for them was not knowing what they were doing. They felt that if they clearly knew what they were doing, it would no longer be a challenge, making it a boring job. 1. People who study physics and encounter things they don't understand can always blame God, the world is complex, not your fault. But if there's a problem with your program, there's no scapegoat. 0 is 0, 1 is 1, it's you who messed it up.

2. In 1969, not long after the Apollo spacecraft landed on the moon, I met Joel Aron, the software manager of the Apollo project, at a software engineering conference in Rome. I knew that each Apollo spacecraft had more than 40,000 lines of code than the previous one. I didn't know what "line" meant for code, but 40,000 lines was definitely a lot. I was amazed that they could get this much code right, so I asked Joel: How did you do it? He said: What? I said: How did you get so much code correct? Joel said: “Correct?!” In fact, I found an error in the code for calculating the lunar trajectory of the lunar module just five days before launch. The code calculated the lunar gravity direction in reverse. It was supposed to attract, but it was written to repel. It was a fluke that I found this error. I was shocked, and I said: These guys are lucky? Joel said: “Yes.”

3. Software testing can determine that there are bugs in the software, but it cannot prove that there are no bugs.

4. A program's elegance is not an optional luxury, but a crucial factor in success or failure. Elegance is not an aesthetic or fashion issue, but can be translated into practical technology. The Oxford Dictionary defines elegant as "pleasingly ingenious and simple." If your program is truly elegant, it will be easy to manage. The first reason is that it is shorter than other solutions, and the second reason is that its components can be replaced with other solutions without affecting other parts. It's strange that the most elegant programs are often the most efficient.

5. Before computers, programming was not a problem. With weaker computers, programming became a moderate problem. Now that we have huge computers, programming has become a major problem. 1. My early days of programming were very different from now, as I was writing programs for a computer that hadn't been built yet. The person building that machine wasn't finished, so I couldn't test my code. Therefore, I found that whatever I made had to fit in my mind.

12. My mother is an excellent mathematician. Once I asked her if geometry was difficult, and she said it wasn't, only if you use "heart" to understand all the formulas. If you need more than five lines of formulas, then you're on the wrong track.

13. Why are so few people pursuing elegance? That's reality. If we say elegance has its drawbacks, then it's that you need to put in immense effort to attain it, and you need a good education to appreciate it.