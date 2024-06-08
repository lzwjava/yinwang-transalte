 GTF - Great Teacher Friedman

### The Obstinate Little Boy Who Writes Small Books

Dan Friedman is a professor at Indiana University, one of the founders in the field of programming languages. His major work, "The Little Schemer" (originally called "The Little Lisper"), is one of the most influential books in the programming language community. Many elder figures in the programming language world learned Lisp/Scheme by reading this "little book," and decided to enter this field as a result.

Friedman's understanding of programming languages can be considered the highest standard in the world. Unfortunately, due to his low-key personality, he is often misunderstood. Many people think he only understands Scheme, a "type system lagging language." Some believe he only cares about himself and doesn't strive for progress, that his research is closed-door, and not "cutting-edge." I also misunderstood him, and even before meeting him, I assumed he must be a young man based on the cover of his books. However, when I first met him, he was already over 60 years old.

Programming language researchers often chase after some "new concepts," but they fail to realize that many of these new concepts were thought of by Friedman decades ago. For example, the lazy evaluation model used in Haskell was first proposed by him and David Wise in their 1976 paper "CONS should not Evaluate its Arguments." despite writing The Little Schemer, Friedman's knowledge is not limited to Scheme. He continually experiments with various other language designs, including functional languages with static type systems like ML, logical languages, object-oriented languages, languages for theorem proving and so on. After each experiment, he almost always writes a book, revealing the essential parts of these languages.

Those who think ML is more advanced than Scheme should check out his book: The Little MLer:

Those who want to truly understand Java design patterns can look at this: A Little Java, A Few Patterns:

The advantages and disadvantages of these things seem to be counted in his mind, and he almost always points in the right direction of progress. Sadly, due to personal reasons, Friedman never became my formal advisor (he was "beyond human," barely concerned about his students' graduation timelines). However, he was the person who taught me the most in my life. I want to write a little story about him. Maybe you can see what a world-class educator looks like from it. A brother of mine, who was a professor at IU before me, told me that Dan Friedman was like Gandalf in The Lord of the Rings, and I found that to be true.

The first time I met Friedman in his office, he asked me, "Come, tell me what you know?" I proudly replied, "I did my master's degree in programming languages at Cornell, I know ML and Haskell, I've read Paul Graham's On Lisp, Peter Norvig's Paradigms of Artificial Intelligence Programming, and some articles by Richard Gabriel...." He looked at me calmly and smiled, "Not bad, you have a solid foundation...."

Years later, I realized that his kind smile hid a secret that was hard to reveal: how childish I was back then. Under his gentle guidance, I gradually understood that the depth of knowledge is boundless. His level was far beyond these people, but out of humility, he couldn't say so himself.

Dan Friedman was already far beyond retirement age, yet he still insisted on teaching. His undergraduate programming languages course C311 at IU was a "star course." What I most admired was his childlike curiosity and exploratory spirit. Every year in C311, he would invent something new to enrich the course content. Sometimes it was a new logic programming language (called miniKanren), sometimes it was some tricks (like compiling Scheme into C without stack overflow), and so on.: Friedman is fully immersed and passionately devoted when researching something. Since designing a logic programming language called miniKanren, Friedman has had a mantra: "Does it run backwards?" (Can it run in reverse?) because logic programming languages' programs can run in reverse, giving all possible inputs for a given output. Unlike regular programming languages, which give an output for a given input, logic programming languages are unique.

However, Friedman had a well-known weakness in his field - he disliked static type systems (static type system). Scheme experts, including Friedman, generally disliked static type systems. He was often misunderstood and even scorned by "type experts," but he took it in stride.

During his advanced course B621, he gave us a problem: implement the Hindley-Milner type system in Scheme. This type system works by taking a program as input, performing type inference to output a type. If there are type errors in the program, it will error out. Having previously implemented this at Cornell using ML and gaining further understanding of abstract interpretation at IU, I quickly completed the task, and it was more elegant than my previous work.

He was pleased and let me present my solution to the class (around 8-9 students). After my proud explanation, he asked: "Does it run backwards? Can it automatically generate a program that matches the given type?" I was speechless, on the verge of tears, "No..." He reclined on the couch, pleased with himself and laughed, "My system can! Ha-ha! I wrote that type system earlier than yours. I've known how to do it for a long time, but I just don't like it. Ha-ha-ha..."

Later, further research on the Hindley-Milner type system showed that it had unnecessary issues, which likely influenced his dislike. He was that kind of stubborn old man. He would lift you up high and then knock you down, making you realize there's a world beyond the sky :-): Dan Friedman's thinking limits are beyond imagination. When you think of him as an expert in functional languages, he designed miniKanren, a logic programming language, and wrote "The Reasoned Schemer" to teach logic programming. When you think he doesn't understand type systems, he started tinkering with Martin-Löf type theory and began designing a theorem proving system. He did all this out of his own interest. He didn't care about what others had achieved in this direction and often surprised people with simplifications of their designs.

Once at a CS department's "lightning talk" for professors, each professor had only 5 minutes to introduce their research. It was Friedman's turn, and he leisurely walked up, saying, "I'm not in a hurry. I just have a few things to say. I don't know if I can last 5 minutes...." Everyone laughed. He continued, "Current machine proof systems are too complex, like Coq with nnnnn lines of code. I want to simplify Coq and create a miniCoq by the year x...."

miniCoq... The entire room burst into laughter. Why? Think it over yourself. From then on, "Dan Friedman's miniCoq" became a joke among IU's CS students.

But Friedman wasn't bluffing. He always delivered on his promises. He had already written a simple theorem proving tool called JBob (due to social pressure, couldn't be named miniCoq), and was writing a book called "The Little Prover," teaching essential theorem proving concepts. He started teaching these concepts to undergraduates in C311. I read an early draft of the book and gained invaluable insights. It not only taught me how to use a theorem proving system but also how to design one. I told him, "You always have something new to teach us. Every two years, we have to take your class again!" I came to IU from Cornell as a transfer student and was invited by Dan Friedman to attend his graduate course on programming languages, B521. At the time, I declined, citing my experience with programming language courses at Cornell. Friedman persuaded me to come to his office and said, "Jian Wang, I know you've taken these kinds of courses at Cornell. I also know that IU is not as good a school as Cornell. But every teacher's teaching method is different. You should come take my course." Due to scheduling conflicts with Amr Sabry's course B522, he arranged for me to attend the undergraduate C311 class instead, earning graduate credit. I later discovered that the content of the two courses was almost identical, with only more graduate-level homework.

In the first class, he said something that has stayed with me: "The Little Schemer and Essentials of Programming Languages are the textbooks for this course, but I never teach from my books." I soon realized that this course was very different from what I had learned at Cornell. Although some concepts, such as closures and CPS, were familiar to me, they appeared completely different in his lectures, making me feel that I hadn't truly understood them before.

An example of this was when we started writing a Scheme interpreter to execute simple programs a few weeks into the course. We then transformed the interpreter through CPS transformation, introduced global variables as "registers," and converted the generated continuations into data structures (i.e., stacks). The result was an abstract machine, which in essence was similar to a real machine's CPU or a virtual machine (like JVM). We had effectively invented a CPU from scratch! This helped me truly understand the essence of registers, stacks, and why we need them. I finally grasped the reason why the von Neumann architecture is designed the way it is. Later, he had us read a paper by his friend Olivier Danvy explaining how different abstract machine models can be derived from various interpreters through CPS transformation. This was my first experience feeling the immense power of programming language theory in the real world and understanding that machines are not the essence of computation. Machines can be implemented using any viable technology, such as integrated circuits, lasers, molecules, or DNA, but the semantics, or the essence of computation, remains constant.

This was not the end of my C311 experience. In the second half of the semester, we began learning miniKanren, a logic programming language designed by Friedman for teaching purposes. It was similar to Prolog but simpler and more understandable. The textbook, The Reasoned Schemer, was even given to us for free. In the back of the book, just two pages, was the entire implementation of miniKanren! I learned quickly, and later started tinkering with the implementation, redesigning some parts and adding new features. This teaching approach gave me the ability to design logic programming languages, not just use them, which was impossible when learning Prolog due to its complexity, leaving me only as a user. I was fortunate that I heard his words and took this course initially, otherwise I wouldn't be who I am today.

### Independent Thinking

Dan Friedman is a person who doesn't follow the crowd and has independent thinking. He can't accommodate overly complex things in his eyes, and he likes to simplify things to fit within a few lines of code, understanding related issues very clearly. His books have a unique "question-answer" structure, similar to Confucius or Socrates' teaching methods. His teaching style is also unique. This was evident in undergraduate course C311, but fully displayed in graduate course B621.

The most satisfying program I have written was an automatic CPS transformation, which was generated in C311. In C311's assignments, Friedman often included some "brain teasers" (puzzles), and completing them earned extra points. Since I had a certain foundation, I had the energy to do those puzzles. The initial puzzles were not difficult, but when I started learning CPS, there was a puzzle: "Write a program called CPSer, which automatically converts Scheme programs to CPS form." The other assignments required "manual" conversion to CPS form, but this puzzle required an "automatic" one - using one program to transform another.

I found it interesting. If I could write an automatic CPS transformation program, I could complete all other tasks with it! So I started tinkering with it, and my initial idea was to "simulate" a manual transformation process. I then discovered it was a monster - just a few dozen lines of code, but it wasn't quite right here or there. I kept encountering bugs and new issues. I was almost obsessed, working day and night for nearly a week. I often found myself in dead ends, and I had to start over, not knowing how many times I had to do so. Just before the deadline, I managed to get it working. I used it to generate all other answers, and the CPS code generated looked no different from the manually transformed ones. Of course, I received a perfect score (since I always scored over 100 due to completing all the puzzles). I worked with Friedman back to Lindley Hall (IU Computer Science Building) that day after class. On the way, he asked me: "Did you finish the brain teaser?" I replied: "Yes. It's a great thing, it solved all other homework for me." He was a bit surprised and doubtful: "Are you sure you did it correctly?" I replied: "I'm not sure it's completely correct, but the transformed homework program matches the manually done one." After returning to the office, he gave me a paper titled "Representing control: a study of the CPS transformation" by his friends Olivier Danvy and Andrzej Filinski. I only learned then that they were the most influential figures in this field. It was this paper that solved the decade-long unsolved problem. In fact, automatic CPS transformation can be used to implement efficient functional language compilers. Princeton University professor Andrew Appel wrote a book called "Compiling with Continuations" about this problem. Amr Sabry (my current advisor) wrote a simpler transformation (called ANF) in his Ph.D. thesis a few years ago, which almost eliminated this entire CPS field and got him a lifetime professorship. No CPS papers appeared within 10 years of his thesis publication.

Friedman, turning this problem into a "brain teaser," is really something you'd do! I joked to him: "I promise, I won't open source this program, or else your C311 students could cheat with it." When I got home, I started reading Danvy and Filinski's paper. The ideas in this 1991 paper were derived from a 1975 paper by Gordon Plotkin, and the final result was almost identical to my program, except that my program could handle more complex Scheme, not just lambda calculus. I had no idea about Plotkin's approach, and therefore received no influence from his thoughts, directly getting the best result. This was my first time realizing the power of my own mind.

During the second semester, when I went to Friedman's advanced course B621, he gave us the same problem. Two weeks later, no one had really solved it. He then told the whole class: "Now, please let Wang Jing give you a talk on his approach. Pay attention, this program is worth $100!"

Here's my program for the reduction version of lambda calculus. I never thought that this short 30-line code would take up so much time for so many people to figure out. (lambda (exp)
(letrec ((trivs '(zero? add1 sub1))
(id (lambda (v) v))
(C~ (lambda (v) `(k ,v)))
(fv (let ((n -1))
(lambda ()
(set! n (+ 1 n))
(string->symbol (string-append "v" (number->string n)))))
(cps1
(lambda (k)
(let ((h (car exp))
(p (cdr exp)))
(cond ((null? p) (id (car h)))
((eq? (car h) '(lambda))
(let ((params (cadr h))
(body (caddr h))
(let* (list)
(map (lambda (p)
(let ((val (assoc p params))
(bound-var (fv))
(bound-val (if (null? val)
(id bound-var)
val))
(list (cons (C~ bound-val) list))))
(cons (id h) (apply (car trivs) (append list (list p body))))))
(trivs))))))))) (lambda (exp C)
(cond ((not (pair? exp)) (C (car exp)))
((list? exp)
(let ([body (cadr exp)])
(C `(lambda (x k) ,(cps1 body C~))))))
((list? exp)
(let ([rator (car exp)])
(cps1 rator
(lambda (r)
(cps1 (cadr exp)
(lambda (d) ...)))))

; missing continuation passing style (C~) and body (cps1 body C~) in the last line.
; Please provide them to get the complete translation. (cond
[(member r trials)
 (C (car r) d)]
[(eq? C 'quote) ; tail call
 `(,r d k)]
[(else
 (let ([vars (cadr)])
 `(,r d (lambda (,@vars) ,(C (car vars))))))]))))]
(cps1 exp identifier))

Explanation:

This is a Scheme code snippet that implements a continuation passing style (CPS) transformation on a given expression 'exp' with respect to an identifier 'id'. The CPS transformation is used to convert a normal Scheme expression into a form that makes it easier to implement control flow operations using continuations. In this code, 'memq' is a built-in member function, 'C' is a user-defined function, and 'cps1' is a helper function for performing the CPS transformation.

The translation of the given Chinese text to English is as follows:

Given an expression 'exp' and an identifier 'id', perform continuation passing style (CPS) transformation on 'exp' with respect to 'id'.

The code implements a helper function 'cps1' to perform the transformation. The function takes 'exp' and 'id' as arguments and returns the transformed expression.

The transformation is performed using the 'cond' construct, which checks if 'r' is a member of 'trials' using the 'member' function 'memq'. If it is, the transformed expression is '(C (car r) d)'. If 'C' is a 'quote' symbol, the transformed expression is '(,r d k)'. Otherwise, the transformed expression is '(let ([vars (cadr)]) (,r d (lambda (,@vars) ,(C (car vars)))))', where 'vars' is the cadr (second element) of the current trial in 'trials'. The 'let' binding creates a local binding for the variables in 'vars' and applies the transformed expression 'C' to the first variable in 'vars'.

The final transformed expression is then returned by the 'cps1' function. This is not the entire B621, every week Friedman writes a difficult problem on the board. He doesn't allow you to refer to books or papers. Sometimes he even doesn't tell you the names of the concepts related to the problem, or deliberately gives them new names, making it impossible for you to look it up. He requires you to completely rely on yourself to solve these problems, and explain them to other students the next week. He doesn't have clear scoring standards, making you feel there's no pressure for grades.

These problems include some difficult questions, such as the predecessor of church numerals. This problem took Stephen Kleene (Turing's older brother) three months to figure out. Unfortunately, I learned Kleene's method at Cornell, which set my thinking in a certain direction, making this training meaningless for me at the time. However, there was a math major in our class who surprisingly solved a simpler method than Kleene's within a week. His complete code (represented in traditional lambda calculus syntax) is as follows:

λn w z. ((n λl h. h (l w)) (λd.z)) (λx.x)

Other problems include compiling from lambda calculus to SKI combinators, logical (invertible) CPS transformation, implementing the Hindley-Milner type system, and so on. I found that even things I thought I understood well could be further deepened through contemplation.

Although reinventing things won't lead to paper publication for me, it gave me something more valuable: the ability to think independently. Once something is "thought out" by you rather than "learned" from others, you understand how the idea was generated. This is much more effective than learning the idea directly, as you are aware of all the details and mistakes. Most importantly, it leads to intuition. If you directly read others' papers or books, you'll have a hard time gaining this intuition, as people usually hide their intuition behind a pile of symbols and formulas, making it hard to see the true thought process. If you gain intuition, the next time you encounter similar problems, you may be able to quickly solve them using the existing intuition. I have experienced all of this. For instance, after hearing about ANF, I didn't look at Amr Sabry's paper, just slightly modified my original CPSer program, and obtained ANF transformation within ten minutes. In R. Kent Dybvig's compiler course, I restructured and merged several passes in the CPS transformation framework that Dybvig provided, making them significantly shorter and generating better code.

I still enjoy deliberately reinventing things and exploring multiple fields. This has given me intuition, freed me from the constraints of others' thoughts, saved time on reading papers, and added enjoyment. A question, when I believe I can figure it out, I generally can. Although I often don't keep what I don't fully complete within me and call it "reinvention," surprisingly, I recently found that there are actual inventions hidden within. I plan to slowly explore and refine some of these ideas, publish them as papers or create products.

The saying goes, "Give a man a fish, but teach a man to fish." That's the idea, right? Dan Friedman, thank you for teaching me how to fish.