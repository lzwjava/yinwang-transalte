---
layout: post
title: "machine-vs-human-2"
---

2. The Gap Between Machine and Human Visual Ability (2)

This article represents my personal opinion and is not related to my current company's stance. Due to the recent slowdown in access speed to GitHub servers in China, the images in this article may still take a considerable amount of time to load, despite being significantly compressed. This article exposes misconceptions and misleading marketing in the AI field to prevent their spread. I encourage everyone to share this article and its subsequent parts, just remember to mention the author and source.

This is the second installment of this series of articles. In this article, I will delve deeper into how much the AI field truly understands the construction of the human neural system.

### Why Neural Networks are Easy to Deceive

The relationship between "neural networks" and the human neural system is very superficial. Once you understand what a "neural network" is, you will realize that it has almost no relation to the neural system. "Neural network" is a misleading marketing term. Its purpose is to create an impression that it is similar to the human neural system, leading people to believe in the so-called "artificial intelligence." In essence, "neural networks" should be called "gradient programming." Stripped down, what we call "neural networks," "machine learning," and "deep learning" are using calculus, gradient descent, to fit out a function using vast amounts of data. Therefore, it can only do what a fitting function can do.

Even with a million images and several weeks of computation, the fitted function is not very reliable. People have found ways to generate strange images that make the most advanced deep neural networks output completely incorrect results.

Why does a neural network have this flaw? Because it only fits a "pixel=>label" function. This function happens to distinguish images in the training set but fails to grasp the structure and essence of objects. It is only pixel-level fitting, leaving plenty of room for holes.

Deep neural networks often mistake objects in images due to pixel or color matching. They cannot understand the structure and topological relationships of objects like humans, making them susceptible to shallow pixel-level deceptions.: The following two strange images are identified as a pineapple honey and a remote control, just because they have similar textures in the middle.

Furthermore, neural networks cannot distinguish position relationships, so they identify misaligned position images as certain objects. For instance, the one below is identified as a face, but the features are all misaligned.

Neural networks make such mistakes because their goal is only to correctly classify the images in the training set and increase the "recognition rate." The method of classification is arbitrary, and it doesn't understand the structure of objects. It doesn't see "leaves," "rind," "box," or "buttons," it only sees a pile of pixel textures. Since the training set contains images with similar textures labeled as "pineapple honey" and "remote control," and those without this texture labeled as other objects, the neural network finds the "separating boundary" to distinguish them.

I tried to explain this problem from the essence of neural networks, from a statistical perspective. Neural networks actually fit a function, trying to separate labeled samples. The fitted function attempts to approach a "real boundary line." A "real boundary line" is a function that never makes mistakes - the "truth."

When the data volume is small, the function is very rough. When the data volume increases, it gradually approaches the real boundary line. However, no matter how large the data volume is, it cannot obtain a completely accurate "analytical solution," and it cannot exactly grasp the "truth." if the real-world function is not particularly simple and luck is not on our side, the functions obtained by data fitting will have many "gaps." The above pixel attack methods are about finding samples in the "gaps" where they cause the fitting function to make misclassifications.

A human visual system is completely different. Humans directly perceive what things are, they see the "solution," they see "reality," without the process of approaching it with data. Therefore, unless a person is extremely tired or drunk, it is almost impossible for them to make a mistake in judgment.

Taking a step back, the so-called "correct classification" in image recognition is defined by people. These things were given names by people, and many people collectively labeled the training images. So the so-called "solution," "reality," are all defined by people. Someone saw a certain object, understood its structure and properties, and gave it a name. So other people can also identify the same object by understanding its structure.

Neural networks cannot see the structure of things, so they have difficulty obtaining precise classifications. Therefore, machines are hardly able to surpass humans in image recognition. The so-called "superhuman vision" deep learning models are mostly deceit and deception to the masses. They use non-universal datasets and unfair accuracy comparison standards to make machines seem more capable. This is a serious problem, which I will analyze in detail later.

Neural network training is similar to competitive education. Neural networks are like students trained in exam-oriented education, their goal function is "scoring high," and they employ any means to achieve it. However, when they encounter real-world problems upon graduation, they are clueless, realizing they have learned nothing of substance. They were only trained to distinguish the correct answer from ABCD. When faced with reality without ABCD, they don't know how to proceed.

The parameters trained in deep learning are incomprehensible, as their purpose is merely to fit data and separate different types of images, lacking any significance. AI experts often justify this "incomprehensibility," with some even claiming: "The neural network learns data that is incomprehensible, but it surprisingly works effectively. These learned model parameters are knowledge!"

Are these models truly effective? Then why can they be so easily fooled by bizarre images? Labeling them as "knowledge" is absurd, seriously undermining the meaning of "knowledge." These "learned" parameters are not the essence of things, not knowledge, but merely a pile of incomprehensible numbers, only to minimize "error" and separate images in the feature space.

Labeling these parameters as knowledge is as laughable as claiming that guessing answers in a test is knowledge. "Answer B for the tenth question in the other sets, so answer B for this set's tenth question".... Deep learning fitting functions are like fitting functions based on past exam questions and their answers, aiming to answer without attending classes or understanding the subject matter. Sometimes they can deceive the answer, but when faced with new or rearranged questions, they are clueless.

Humans are not fooled by this deception because they have extracted high-level topological structures, making their judgments not influenced by pixels. Since they have extracted structural information, human observation is interpretable. If you ask a child why you say this is a cat instead of a dog, she will tell you: "Because its ears are shaped this way, its teeth are like that, it walks like this, it often grooms itself...." "Let's try an experiment. You can ask your child which one is a cat and which one is a dog. If it's a cat, why do they think this is a cat and not a dog?

A neural network sees a pile of pixels, and after many layers of processing, it doesn't know what structure it's looking at, let alone "eyes," "ears," or "mouths," not to mention "walking" or other dynamic concepts. So it can't tell you why it thinks this is a cat. The fitting function happened to classify this as a cat, and if you want to know the reason, it's likely to be shallow: there's a pixel in the image that matches the fur texture of a cat in the image library.

Some researchers have extracted the parameters of the depth neural network's layers and found the corresponding pixels and textures in the images to prove that the neural network's parameters have meaning. It looks reasonable at first, it seems like learning can get so many well-designed filters! But upon closer inspection, there's not much meaningful content inside, because the learned parameters only separate the image categories.

Therefore, it's very likely that the human visual system is fundamentally different from the principles of deep neural networks, or only the lowest level parts have similarities."

The relationship between "neural networks" and human neurons is superficial.1. Why do AI experts always assume that advanced functions of visual systems can be obtained through "learning"? It's quite possible that the "structural understanding" and "3D modeling" functions of human and animal visual systems are not learned but are hard-wired in genes. Have you ever seen a world that is flat and unrelated pixelated images since you were born?

2. I believe that humans and animals are different from existing machines when they are born. The hardware for structural understanding is already present in the fetus and only needs to develop and activate. Humans have learning abilities, but human learning is built on structural understanding rather than unstructured pixels. Moreover, human "learning" is likely to be at a much higher level than neurons, which are not like machine learning's back-propagation.

3. Even if you have more data and computational power, can you surpass the evolution and selection process that has been going on for billions of years on Earth? Instead of training or learning yourself, why not just copy it directly from humans? But the problem is, do we really understand how the human visual system works?

4. Neuroscientists have not fully grasped the workings of the human visual system. Just like all fields of biology, our understanding is still quite shallow. The relationship between neural networks and the human visual system is superficial. Every time you question the relationship between neural networks and the human visual system, AI researchers will cite the experiment conducted by Hubel & Wiesel on cats in 1959: "It has been proven that the human visual system works this way!" Such confidence is undeniable.

5. I ask you, if we had known the detailed workings of the human visual system in 1959, why are there still so many models being changed and trained now? Why not just copy it directly? Therefore, their statements are contradictory.1. You wondered why, in 2019, AI experts still used a 60-year-old experiment to illustrate problems, hadn't there been any new discoveries since then? The experiment by H&W only demonstrated the basic function of cat's visual neural bottom layer (capable of "line detection"), but it didn't reveal how signals from these bottom-layer neurons were combined at higher levels. "Line detection" is a fundamental image processing operation. A visual system that recognizes topological structures in animals should naturally be able to perform "line detection," but it should not be limited to this low-level function.

2. The visual system should have higher-level structures, but H&W's experiment failed to answer this question, remaining a black box. AI researchers, however, waved the results around, confidently proclaiming they had unraveled all the mysteries of the animal visual system.

3. Those who claim "we have completely figured out how human vision works" among AI experts should take a look at the 2005 analysis of the Herman grid illusion phenomenon's slide show from Schiller Lab, MIT's neuroscience and cognitive science research lab. Through a series of experiments on the Herman grid illusion pattern, they found that the long-held understanding of the causes of this phenomenon was incorrect: the dark spots were not due to the "edge enhancement" function of the retina. They hypothesized that this was due to the S1 "direction selection" cells in the V1 visual cortex layer. Later, in a 2008 paper, they found Schiller's results to be incorrect, as this illusion was related to the straightness of the lines, and the illusion disappeared when the white lines were bent. They then proposed their own new "guess."

4. From this research method, we can see that even an institution like MIT, which is advanced in visual research, is still in the "guessing" stage, treating the brain as a black box and conducting experiments at the "behavioral" level with images. They have not fully cracked the visual system, revealing its specific "routes" and "algorithms" in action, but rather give it inputs and test its outputs. This is the "black box" experimental method. Consequently, many theories about human vision are not definitive and may be incorrect guesses. I. Neuroscience Lags Behind AI Research Methods
The development of neuroscience up to today still lags behind that of AI in research methods. In 2019, we still bring up the results of neuroscientists from 1959 to argue. Closed-door research, paying no attention whatsoever to others' latest findings. The current deep neural network models are essentially clueless. They stack together pixel manipulations and then train on vast amounts of data, believing this will yield all visual functions.

II. No "Backpropagation" in Animal Visual Systems?
There isn't "backpropagation" in the animal visual system as some might claim. H&W's experiments didn't find backpropagation. In fact, neuroscientists have yet to discover backpropagation in the nervous system, as neuronal signaling mechanisms cannot support "reverse" communication. Many neuroscientific conclusions suggest that backpropagation is unlikely in the human brain.

III. Neural Network Approaches Likely Not Inspired by H&W Experiment
Therefore, various neural network approaches are unlikely to have been significantly influenced by the H&W experiment. They merely appear closer to "human neural systems" due to a superficial resemblance. Today's so-called "neural networks" are merely a mathematical function expression, with the only active component being calculus. Backpropagation, as the name suggests, is a calculus derivative operation. Neural network training involves repeatedly calculating derivatives and minimizing error using gradient descent methods to fit a function. This entire process has no relation to the working principles of neurons, it's purely mathematical.

IV. Eliminate the Confusion Caused by Ignorance
To clear up the confusion caused by ignorance, you can educate yourself about the working principles of the human nervous system. I recommend checking out the YouTube video series called "Interactive Biology." From there, you can easily understand some details of the human nervous system, such as neuron function, the principles of the visual system, the structure of the eye and retina, the working principles of the auditory system, and so on. Neuroscientists have delved into such detailed research, revealing every detail of the neural signaling process.

V. AI Researchers Are Unaware of How the Human Brain Works

[End of Translation] I. Introduction

The question of whether the brain truly understands how it works in the field of AI is debated. You may refer to this speech: "Can the brain do back-propagation?" (Can the brain do back-propagation?). The speaker is Geoffrey Hinton, one of the pioneers in deep learning. He, along with Yoshua Bengio and Yann LeCun, received the Turing Award in 2018 for their contributions to deep learning. In the beginning of the speech, Hinton mentions that neuroscientists claim the brain cannot do back-propagation, and he proceeds to prove it is possible based on the working principle of neurons and how back-propagation can be implemented using brain neurons.

Yes, if you had the ability to make the brain work according to your "algorithm," the system of neurons might be able to do back-propagation. But, is the brain yours to design? Unfortunately, we cannot change the brain; we can only discover how it actually works. This is not a question of "whether the brain can" but rather "whether the brain will." Researching the brain is a scientific discovery process, not an engineering design process.

After watching this speech, I felt that AI researchers had entered a "god-like" state of mind. They firmly believe their models, called "neural networks," are the ultimate answer, even attempting to fit the brain into this model and imagining how brain neurons could implement their "neural networks." However, they have not discovered that the brain's methods might be much more clever and fundamentally different from their "neural networks."

From this video, we can also see that the neuroscience community does not support the claims made in the AI field. The AI field is essentially guessing in the dark. There is a comment below the video that I appreciate, as it speaks sarcastically: "Geoff Hinton precisely knows how the brain works because this is his 52nd discovery of a new way the brain operates."

II. Blind Faith in AI

The blind faith in AI has been a topic of concern for many years. AI researchers, driven by their belief in the superiority of their models, often overlook the complexities and nuances of the human brain. They assume that the brain functions like their neural networks, failing to consider the unique characteristics and mechanisms of the brain.

The human brain is an incredibly complex organ, and understanding its workings is a challenging task. Neuroscientists have made significant strides in unraveling the mysteries of the brain, but there is still much to learn. The brain's neural networks are vastly different from the artificial neural networks used in AI. The brain's neurons are not passive computing units like those in artificial neural networks; they are dynamic, adaptive, and capable of learning and adapting to new information.

Moreover, the brain's neural connections are not fixed but can change and strengthen or weaken based on experience. This ability, called synaptic plasticity, is a crucial aspect of learning and memory in the brain. In contrast, artificial neural networks have fixed connections, and their learning is based on predefined algorithms.

III. The Importance of Interdisciplinary Collaboration

To bridge the gap between AI and neuroscience, it is essential to foster interdisciplinary collaboration between researchers in these fields. By combining the expertise and insights from both domains, we can gain a more comprehensive understanding of the brain and develop AI systems that are more human-like and effective.

Neuroscientists can provide AI researchers with a deeper understanding of the brain's structure, function, and mechanisms, while AI researchers can develop computational models and techniques to help neuroscientists analyze and interpret complex neural data. This collaboration can lead to new discoveries and innovations in both fields.

IV. Conclusion

In conclusion, the question of whether the brain can do back-propagation is a fascinating topic that highlights the importance of interdisciplinary collaboration between neuroscience and AI. While AI researchers may believe their models are the ultimate answer, it is crucial to remember that the human brain is a complex and dynamic organ that functions differently from artificial neural networks. By working together, we can gain a more accurate and nuanced understanding of the brain and develop AI systems that are more effective and human-like.: AI people seem to have an unrealistic "belief" or "faith" in them, they firmly believe that machines will definitely possess human-like intelligence and will eventually surpass humans in all aspects. They often display an attitude that humans are not remarkable, speaking of "humans" as if they were another species, believing they know all human abilities and are qualified to judge everyone's intelligence.

I don't know what causes this "AI faith." A saying goes, "All my arrogance comes from my insecurity, all my heroic swagger from the weakness in my heart, all my loquaciousness from the doubts in my mind." It seems there's a deep-rooted insecurity and resentment that leads them to be so steadfast and arrogant. They want to create a super-intelligent machine and then rest on their laurels, yet they fail to see the vast intelligence of human abilities revealed in everyday life's mundane things.

They can't see the various, diverse human activities in the world, each one displaying extraordinary intelligence. Even the simple act of pouring tea or pouring water contains machine-unreachable intelligence, let alone various sports, music performances, research, and creative activities. Animals, pets, livestock, birds, and even insects display intelligence that is awe-inspiring. They turn a blind eye to all these wonders, not to appreciate their intricate design and outstanding performance, but to sit and mull over "machines will surpass humans."

They have come to see machines as a species, like protecting a "vulnerable group," maintaining their "rights" and "dignity." They don't allow others to question these machines, and they don't allow you to say that they might not be able to achieve human-like intelligence. In short, machines have become more than just a tool in their psychology, but a living being, even a more advanced life form than humans.

You can refer to another interview with Geoffrey Hinton recorded at the Google Developers Conference (Google I/O '19) in May for more information. I observed numerous AI enthusiasts blindly believing and making unfounded statements in this video, as all these statements were intensely presented in Hinton's speech. He confidently uttered these unfounded statements without any evidence, leaving no room for doubt. At times, the interviewer had to adopt a somewhat skeptical tone.

In the interview, Hinton made the following statements:

1. "Neural networks were designed to work like the human brain."
2. "Once neural networks can carry on conversations with us, we will be able to use them for educational purposes."
3. "Neural networks will ultimately surpass human abilities in all aspects.": "Are we not all neural networks then?" (Emphasized twice)

...... So neural networks can accomplish all functions of human intelligence. This includes emotions, consciousness, etc.

People used to think that life is a special kind of force, but biology has explained all of life. People still think consciousness is special, but neural networks will show that consciousness is nothing special.

His statements are all incorrect, unscientific, and without basis.

I've noticed that whenever the host asks with a slightly questioning tone: "Can this really be achieved?" Hinton will answer: "Of course it can. We're all neural networks, aren't we?" There's a serious issue here. The "neural networks" he refers to are not actual neural networks in the brain. The "neural networks" in the AI field are just their own mathematical models, which they named "neural networks" themselves. So his "proof" is just a word game: "Because we're all neural networks, neural networks can accomplish all functions of human intelligence, emotions, and even consciousness itself!": The "neuronal networks" in front and behind are completely different things. Are we neuronal networks? Our brains have neurons, which seem to have formed a network, but its structure is completely different from that of the "neuronal networks" in the AI field, and their working principles are also very different. Hinton's answer to this problem was unscientific and irresponsible.

Regarding the statements about life, feelings, and consciousness at the end, I also strongly disagree. Although biology explains the construction and principles of living organisms, why people have not been able to create a living organism from non-living material is still a mystery. Although people understand so much biology, biochemistry, organic chemistry, and even synthesize various proteins, why have they not been able to assemble these things together to make it "alive"? It's like building some machine parts, but finding that the machine doesn't work after assembly. Don't you think there's something missing? Biology has developed for so long, and we haven't even made a simple, living thing before, let alone say "life is nothing special."

This shows that biologists, despite knowing some of the working principles of living organisms (how), have not fundamentally understood what life is (what) and why it exists (why). People have solved some of the "how" problems (how living organisms work), but the "what" and "why" questions of life are still unsolved mysteries, unlike what Hinton said, that they have all been figured out and there's nothing special about it.

Perhaps life is a special kind of thing? Perhaps only living things can produce living things? Perhaps life is from outer space? Perhaps it was designed by some higher level of intelligence? These are all possibilities. Real scientists should maintain an open mindset and not have beliefs like "man is superior to God." All our conclusions should be based on evidence, and we should not say "definitely" or "inevitably" without evidence, as if all secrets have been unlocked. I hold the same attitude towards intelligence and consciousness. Before we have manufactured genuine intelligence and consciousness from ordinary matter, we should not speak presumptuously about everything related to them. Life, intelligence, and consciousness are more marvelous than some people imagine. Can 46 billion years of time really produce such intelligent beings?

Please don't misunderstand me. I don't believe in religion. I think religious scriptures are all made by humans. But if you firmly believe that the intricate structures of humans and animals are all "evolution," and that they are not created by some higher level of intelligence, isn't that another kind of religion? You have no evidence. Anything without evidence is just speculation, not something to be believed in.

It seems I've strayed off topic....

In short, the founder of depth learning made so many faith-based statements, which shows how chaotic this field is. Moreover, from his speech, you can see that his "AI" is mainly about solving relatively easy recognition problems (speech recognition, image recognition). He didn't realize how difficult it is for machines to achieve "understanding." The difference between "recognition" and "understanding" is what I want to clarify in this article.: The working style of a "dan-tian shi" (alchemist) in the field of neural network design is similar to that of algorithm engineers and data scientists. They make adjustments to a model here and there, train it with vast amounts of images, and the accuracy rate improves, resulting in a paper. The reasons for the better performance and the principles revealed are unclear, as is whether certain nodes are essential or not. Many paper results cannot be reproduced by other researchers, raising the possibility of fraud.

I am skeptical about the research methods in this field bringing about any real breakthroughs, as this is not a scientific approach. If you view neural networks as code written in a differentiable programming language, then the current model design methods are akin to "a million monkeys typing on keyboards," with one monkey eventually producing "Hello World!"

Many mathematicians and statisticians do not agree with the research methods in the AI field and express doubts and confusion about many of its practices. Stanford University's Statistics Department even offers a course, Stats 385, specifically to discuss this issue. In class, they invited some veteran mathematicians to analyze the purposes of various operations in deep learning models. Some operations are easily understandable, but others are a mystery, even to the alchemists who designed these models themselves.

Therefore, you may have noticed that AI researchers have not truly understood the working principles of the human visual system, and much machine vision research is done in the dark. In the next installment, we will see how their so-called "superhuman recognition rates" are achieved. Look at the next one: The Gap Between Machine and Human Visual Ability (3)