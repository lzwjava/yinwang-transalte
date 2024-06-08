---
layout: post
title: "Standard Exam Language"
---

I designed a "standardized exam markup language" for my dad during my undergraduate studies (he was a high school English teacher at that time). I wrote a Perl script with around 1000 lines, which could convert this simple markup language into an attractive LaTeX format document with a user-friendly Tk graphical user interface. The exam could include multiple choice questions, fill-in-the-blank questions, error correction questions, and so on. The unique feature of this language was that the question and answer were placed together, making it very intuitive for creating questions. After processing, the answer was separated from the question and placed in the correct position in the answer key. This way, the question creator would not accidentally place the answer in the wrong position and would not have to worry about formatting.

For example, the format for multiple choice questions is as follows:

# Our teacher told us that there \underline{-----} no end to learning.
[A] There is an end to learning.
[B] There are no ends to learning.
[C] There was an end to learning.
[D] There will be an end to learning. I. This is an extraordinary sentence...
II. This is an extraordinary sentence...

A. was
B. is
C. has
D. had

Answer: B. is (for the correct sentence)

In the given text, there is no error for the English words provided in options A, B, C, and D. However, based on the context given, the correct answer for the blank in the text is "is". Therefore, the answer key for this question would be B. is.

For the given text, the correct sentence is: "This is an extraordinary sentence..."

The text provided is a design for creating error questions in English. The # symbols in the text will be replaced with question numbers, and the * marked options will be placed in the answer key. The most interesting part is the error questions. Since error questions are a English paragraph with some lines containing errors, but each line can only have one error, the design is to insert error symbols like:

This is an |extraordinary|extrordinary| sentence...

The left side is the correct version, and the right side is the incorrect version. The | symbol is used because it will not appear in normal English articles. The left and right sides of the | symbol can be blank, used to indicate "insertion" and "deletion". For example:

[1] I. This is an extraordinary sentence...
[2] I. This is an extraordinary sentence...

A. was
B. is
C. has
D. had

Answer: B. is (for the correct sentence)

Answer key:
[1] I. This is an extraordinary sentence...
[2] I. This is an extraordinary sentence...

A. was
B. is (correct answer)
C. has
D. had (incorrect answer) I don't know how to play the piano.

The answer will show:

Add "the" between "play" and "piano".: If both are not blank, it is "edit", like the example above. I will arrange the paragraphs based on these markers' positions later, making each line have at most one error above. To make the lines of the paragraph look uniform, I used a dynamic programming line breaking algorithm similar to TeX. It first calculates the "ugliness" of multiple line breaking schemes, then chooses the best-looking one from them.

Now I recall that my design back then was quite advanced. I wonder why I didn't think of turning it into a product and selling it to the Education Department? Maybe because I thought this technology would create more "oceans" of questions, causing more trouble for middle school students :-P Compared to my language, the markup languages used by some blog systems nowadays (like markdown) are truly "grandmasters" to me.