---
layout: post
title: "A Ruby static analyzer named RubySonar"
---


For the past few months, I've spent most of my time working on a Ruby static analyzer called RubySonar. It uses similar technology as PySonar2 but with significant adjustments for Ruby semantics. Now, this analyzer supports Sourcegraph's Ruby code search and browsing, which is a significant improvement over the previous results.

With RubySonar's assistance, Sourcegraph can find several tenfold to over a hundredfold more symbols in many repositories compared to before, along with increased usage examples. The code location accuracy has greatly improved, and there are hardly any misalignments. Additionally, it now supports highlighting local variables, giving it a "static IDE" feel.

Due to RubySonar's speed improvement over Sourcegraph's previous YARD-based analysis, we can now process the entire Ruby standard library instead of just a small part. Ruby on Rails results have also seen considerable improvement. Furthermore, independent applications like Homebrew can now be analyzed.

RubySonar's static analysis uses the same interprocedural, data flow+control flow analysis, and the same type inference system as PySonar2, ensuring high analysis precision. I haven't compared it to Ruby IDEs yet, but given its advanced architecture, it should handle things that even the best Ruby IDEs can't, although there may be some deficiencies in the details. Although Ruby and Python look similar, a lot of work was done to port PySonar2 to Ruby. Initially, I tried to reuse most of the code with some conditional branches for special handling in different places. However, I later found that this was becoming increasingly complex and risky. In order to accommodate one language's features, it was easy to break the code that had already been debugged for another language. Eventually, I decided to completely separate them, sharing only the code through manual copying and modifying. It turned out to be the right decision, or I might still be dealing with some inexplicable errors. This experience taught me that the DRY (Don't Repeat Yourself) principle has its limitations. Sometimes, it's better to copy and paste code than to share it.

Currently, RubySonar is lacking support for native library code, but due to the code's consistent principles (RubySonar having only around 7000 lines of code), these things will be relatively easy to add. Interested Ruby users are encouraged to check their own repositories to see if they have been processed, and if not, they can contact me and welcome to point out any issues.