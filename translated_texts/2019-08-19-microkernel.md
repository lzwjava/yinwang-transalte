---
layout: post
title: "About microkernel dialogue"
---


Somehow, the topic of "microkernel vs monolithic kernel" has become popular again. This debate started in 1992....

### Preface

To be honest, I haven't cared about operating systems for a long time. In my mind, an "operating system" is just a C language runtime system, like JVM is for Java. Due to the design flaws of C language, these systems introduced unnecessary concepts (processes, threads, virtual memory....) and the complexity and overhead that came with them.

The microkernel vs monolithic kernel debate is part of this, in my opinion, along with all the other unnecessary concepts and arguments in the field of operating systems. There are many "religious wars" in the operating system domain, such as "Linux vs Windows", "free software vs proprietary software", "RISC vs CISC", and even "VIM vs Emacs".... People fight to prove that their system or tool is the best in the world. They may shoot down anyone who points out the flaws of their tool. These are called "flame wars". I was once an active member in certain religious disputes, those unfamiliar with my history can look it up. You only realize this after experiencing many things, that these religious emotions and disputes are so childish and ignorant.

This kind of "technical religious emotion" often reveals the lowly psychological position of the participants. Because they lack confidence, so their psychology relies on something. This something could be a certain operating system (like Linux), a certain programming language (like C++), or a certain tool (like VIM). These people consider themselves superior because they are proficient in using these tools, looking down on "heretics."

People with technical religious emotion seem to be doing it for "technology" and "ideals," but they are actually on the same low level as those who think that driving a fancy car and wearing labels make them "high society." Because they rely on these objects, their position is beneath these objects.

A person should fundamentally regard these things as "things," without any worship or disdain emotions in their psychology.

In my view, an operating system should be roughly like this. It's very simple, and there aren't that many problems with it. I can use these thoughts to see through most of the current operating systems' ideas, whether it's a microkernel or a monolithic kernel. I can view existing operating systems as their "degraded versions." Operating systems are a domain of knowledge that is dead and prevalent. Many people find operating system courses difficult to learn and understand. There are some concepts in it, such as various synchronization mechanisms, which even after completing the course and working for many years, some people still don't understand why they exist or where they are used. Similar things include virtual memory, differences between processes and threads, etc.

Through a lot of experience and reflection, along with inspiration from other fields, I finally understood. It turns out that many of these concepts are unnecessary and dead knowledge.

Concepts in operating system courses are often formed in this way:

1. A long time ago, someone solved a specific problem and proposed a concept (like semaphore). This concept initially had only one use, which was to solve the problem they faced.

2. Because this person was famous, this concept was written into textbooks. Sometimes even the specific implementation details of that time were included. For example, the two operations of semaphore were called P and V, and these two names were also recorded as "legends".: Professors rigidly adhere to the textbook, nitpicking, requiring you to use this concept to solve many other problems. Many are artificially created abnormal problems that don't exist in reality or shouldn't be solved with this concept.

This is why studying operating systems is so difficult—it's full of irrational challenges.

Moreover, in the Unix system, there are numerous poorly designed, ineffective tools that can't be combined properly. The operating system thus exerts a terrifying influence on students. Those who enjoy memorizing, tinkering, and discovering clever tricks thrive in this field and gradually develop a sense of confidence. They don't understand where these concepts came from, they just remember them, and their code is hard to understand. Then they begin to psychologically suppress those who can't remember these concepts or understand their code.

Over time, these people become revered as "gods" by everyone.

Discussing operating systems with some people is a frustrating experience for me because I often abandon some terms and concepts and start from scratch. I try to understand these things from the perspective of "what this thing should be," "what it could be (maybe even better)," rather than "what it is." People who don't understand my unique trait often assume I don't even grasp the basics of the terminology. So the conversation just goes on and on. I'm fortunate to have a few friends I can talk to, who aren't too dogmatic. Today, I had a conversation with a friend about "microkernel vs monolithic kernel" on WeChat. I thought I had a clear understanding of this issue, but through these conversations, I learned new things. These things were probably not fully understood by us before, and maybe many others as well. I think it's worth recording these valuable discussions.

I don't want to explain this from scratch since you can find the principles of "microkernel" and "monolithic kernel" online. I just want to show our dialogue here, which includes both correct and incorrect arguments, a back-and-forth intellectual debate. I find dialogues to be an interesting thing, more effective than plain and straightforward articles.

### Dialogue

Alright, let's begin. The interlocutor "WY" is me, and "LD" is one of my friends.

(August 19)
WY: Hey LD, have you ever thought about the differences between a microkernel and a monolithic kernel?

LD: Not really, WY. What's the difference?

WY: Well, a microkernel is a minimalist operating system design where only the most essential services are included in the kernel. The rest of the system services are provided by separate processes or user-level servers.

LD: Oh, I see. So it's like a more modular design, right?

WY: Exactly. It allows for better separation of concerns and easier maintenance.

LD: But doesn't that make the system more complex? I mean, having all those separate processes communicating with each other could be a headache.

WY: That's true, but the benefits outweigh the complexity. For example, it allows for better fault isolation and easier upgrades.

LD: Hmm, I see your point. But what about performance? Isn't a monolithic kernel faster since everything is integrated into the kernel?

WY: Not necessarily. Modern microkernels use message passing for inter-process communication, which is quite efficient. And, the overhead of the additional processes is often outweighed by the benefits.

LD: Alright, I get it. But what about device drivers? Don't they need to be part of the kernel for low-level access?

WY: That's a common misconception. In a microkernel, device drivers are typically implemented as user-level servers. They communicate with the kernel through well-defined interfaces, allowing for better modularity and easier updates.

LD: Wow, I didn't know that. I always thought microkernels were less capable than monolithic kernels.

WY: That's a common misunderstanding. Microkernels can be just as capable as monolithic kernels, and in some cases, even more so. The key difference is in their design philosophy and the trade-offs they make.

LD: I see. Thanks for the enlightening conversation, WY. I've learned a lot.

WY: My pleasure, LD. It's always great to learn new things together.: I haven't tinkered with an OS for many years, and there should be new discoveries now. This [paper](https://pdfs.semanticscholar.org/983f/f3bf3adf07c9679f4a4e49cd5a8db2e68c5a.pdf) states that Minix 3 is 510% slower than Linux.

 Jordon:

Yes.

（I downloaded the Minix 3 source code and searched for information about microkernels online…）

Interpretation:
WY: It's been a long time since I last worked on an operating system. I suppose there will be new discoveries now. This paper claims that Minix 3 is 510% slower than Linux.

Jordan:

Yes. (After downloading the Minix 3 source code and researching microkernels online): A device generates an interrupt, the interrupt management process receives the interrupt and sends a message to the corresponding device driver process. This process handles the interrupt request, and if the device driver has a bug and crashes, it won't affect the OS. This is the microkernel logic.

WY: The microkernel seems to have had performance issues all along. The separation of servers in different address spaces in L4, QNX... seems to be the biggest problem.

LD: This results in high communication costs. Originally, just passing an address would suffice. Now, the entire thing needs to be copied over.

WY: The address spaces shouldn't be separated. Or perhaps we could do something on the MMU level, map that memory over during transmission. But context switching is another overhead... Function calls are made so complicated, the microkernel indeed seems to be a failure. By the way, does a microkernel service call result in a process switch?

LD: Yes, according to the microkernel definition, every basic unit is a process.: I've messed up.

LD: Memory management is a process, I/O management is a process, every device driver is a process, interrupt management is a process.

WY: The cost of process switching...

LD: To reduce the communication cost between processes, L4 was defined. I don't quite understand what's the point of that.

WY: It improves communication costs, but there's still process switching overhead. I just checked out L4, it passes values from registers, but won't process switching put all registers into memory?: Indeed, the meaning of L4 seems insignificant.

LD: Apart from Microsoft and WeChat, none of the "micro" ones have been successful.

LD: The so-called popular microservices lately.

WY: There should be other ways to deal with the bugs driven by it.

LD: The problems with current OSes are that even small errors in the kernel can cause the entire system to crash. This is similar to the question of whether we should write software using multiple processes or threads.: It should completely abandon the current process switching method from the hardware bottom layer. The saved context is too much.

LD: Isn't the OS now divided into user and kernel protection levels? I think adding another two protection levels specifically for device driver programs would be a better choice.

WY: I once thought of a way to completely do without protection levels, and also without virtual memory.

LD: How about compiler static analysis? Rust?

WY: Completely use real addresses, but the code cannot access memory outside of objects.: Rely on the compiler?

WY: No need for advanced compilers. The language itself doesn't have pointers or such, so you can't access objects that aren't yours. Hmm, we need to abandon C language....

LD: Rust!

WY: No need for Rust. In fact, JVM has been like that for a long time. It's just that we usually don't consider JVM an operating system, but an operating system can certainly be made like that.

LD: So-called objects, are they each with an address and a size? Over the size is not allowed? Or is the compiler ensuring that it will never exceed the size?: You cannot access memory outside of objects in Java or other advanced languages like Python... Only C can, because C has pointers and can point to anything.

LD: Yes. Walking on a bridge without railings like that in C is quite risky. Besides overwriting memory, there's another issue: multiple tasks changing the same memory block at the same time.

WY: To prevent overwriting, we came up with "processes" and "virtual addresses" concepts.

LD: Virtual addresses, for using virtual memory.

WY: Virtual addresses, virtual memory is for isolation. Each process believes its address starts at 0, and functions that were once easily called are now isolated. If this changes, the microkernel would indeed become very fast... Oh, it still exists. Only the scheduler, memory management remains. IPC (Inter-Process Communication) is gone, replaced by function calls.: Let's try a different approach. In fact, the OS has the most issues with hardware drivers, so try to make hardware as standardized as possible, and avoid each hardware having its own driver. Let one driver support multiple hardware types, and the problem will be solved. For example, USB drivers. Completely achievable for one type of hardware to use one device driver.

WY: I still think that driver program bugs don't necessarily cause a system to crash. Can't we use kernel threads? Sharing address space but asynchronously executing.

LD: Linux seems to be doing this. tasklet, can be scheduled.

WY: So if a driver crashes, it doesn't have to crash the system? I'll go check.

LD: What error did you encounter? Accidentally modifying another module's memory will ruin it. Other errors are mostly that the hardware itself can no longer be used.: So that's why you mean another protection level.

LD: Yeah, don't touch the core critical code. But drivers can still interfere with each other.

WY: It's a decent compromise. So microkernel solved a less critical problem.

LD: Yes. That's not important. Oh, by the way, Windows is a microkernel since 2000. I think.

WY: Only claimed to be so. Isn't Mac OS X claimed to be Mach microkernel with BSD?: Yes. MacOS is also a microkernel.

WY: Then how did they solve the performance issues?

LD: I don't know. Windows has a lot of blue screens, obviously they haven't fully achieved isolation. As for Mac, I'm not sure why it's so stable.

WY: Based on our previous discussion, Mac's microkernel might be a myth. Mac's stability is mainly due to the fact that it has fewer drivers, and the hardware is all pre-selected.

LD: Yeah, that's a major reason for its stability.: This is clear enough...... And it seems that microkernel has little use in clusters.

LD: Cluster, each computer is a node. No need to fear if one hangs.

(Continue discussing on 8th of August)

WY: I found this [paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.361.4009&rep=rep1&type=pdf)......: This thing is called L4Linux, which is Linux running on the L4 microkernel. Compared to pure Linux, the overhead is only 5%.

Links to code: <http://os.inf.tu-dresden.de/L4/LinuxOnL4

WY: L4's approach is 1) small parameters are passed through registers without switching some registers. 2) large parameters map the memory to the receiving process, as I imagined before. This avoids copying. Then, they adopted "direct process switch" and "lazy scheduling" to reduce scheduling overhead. Modern processors' tagged TLBs also greatly reduce process switching overhead.

WY: The diagram above is direct message copy. First, map the receiving process's destination address to the sending process's address space, and then copy from the sending process. So, there is still one copy, and it's not like the OS I imagined that can directly transfer object references without copying. Pass-by-value vs pass-by-reference. However, it seems that the overhead is the same as Linux.

LD: Is the advantage of microkernel really that big? WY: The advantage is that of a microkernel, isolation. It may depend on individual requirements. What's the difference between a 99.99% reliable system and a 99.999999% reliable system?

WY: But it seems that high reliability requirements are all going to use vxworks or similar ones.

(Searching online for vxworks...)

WY: It turns out that vxworks is also a microkernel.

WY: Five percent overhead is acceptable... It seems the process switching overhead hasn't been mentioned, using address mapping method.: cross address space

WY: Recently bought a TP-Link AC1900 router, runs on VxWorks.

LD: Isn't TP-Link Linux?

WY: New TP-Link AC1900 changed to VxWorks. Airport Extreme also uses VxWorks.

LD: Why?: Real-time, reliability should be one of the highest. Satellites, weapons all use it.

LD: Reliability should be the highest among them. Boeing 787 also uses it, various Mars rovers... It seems to indicate some issues.

WY: There's also a real-time operating system called [GreenHills Integrity DO-178B](https://www.ghs.com/products/safety_critical/integrity-do-178b.html). F-35 uses it.: Much of the F-35's software is written in C and C++ due to programmer availability; Ada83 code is also reused from the F-22. The Integrity DO-178B real-time operating system (RTOS) from Green Hills Software runs on Commercial Off-The-Shelf (COTS) Freescale PowerPC processors.

LD: One of our MCUs is Freescale's PowerPC...

LD: There's a RTOS called "RTEMs" that I've been paying attention to.

WY: Excerpt from Integrity DO-178B RTOS:

Translation: Much of the F-35's software is written in C and C++ due to programmer availability; Ada83 code is also reused from the F-22. The Integrity DO-178B real-time operating system (RTOS) from Green Hills Software runs on Commercial Off-The-Shelf (COTS) Freescale PowerPC processors. One of our MCUs is Freescale's PowerPC. I've been paying attention to the RTEMs RTOS.: Integrity is also a microkernel. It seems microkernel is reliable, suitable for use in mission critical, safety critical and secure (MILS & MLS) applications.
...

Safe and secure by design:
- RTOS designed for use in reliable, mission critical, safety critical and secure applications
- Based on modern microkernel RTOS design
- Fast, deterministic behavior with absolute minimum interrupt latencies

Translation:
A microkernel RTOS designed for use in reliable, mission critical, safety critical and secure applications. Based on modern microkernel design, it ensures fast, deterministic behavior with absolute minimum interrupt latencies. if you have any objections, please feel free to contact me. if you find it helpful, consider paying for it.