---
layout: post
title: "The essence of relational models"
---


When I make fun of relational databases, there's always someone saying that SQL and the design of relational databases have deviated from E.F. Codd's original relational theory. The relational theory and relational model itself are still quite advanced, it's just that it was messed up during implementation.

I'm sad because if you understand the essence of relational theory (theory/algebra), you'll find that the problems with relational databases are fundamental: relational theory itself is empty and hollow, it's a charlatan disguised in a "mathematics" cloak, a long-standing nonsensical talk that has been propagated in computer science departments of universities for decades.

People always like to construct conceptual barriers to prevent their theories from being attacked. Blaming SQL for not faithfully implementing the essence of relational theory, saying SQL lacks the heart of relational databases, is a common dodge in the relational database field. In the following discussion, I will use a little SQL to represent the corresponding concepts in the relational model, but this does not detract from my criticism of the relational model, because they represent the core concepts of the relational model.

### Relational model vs data structures

The relational model is not a data structure, but rather a logical data model. It describes how data is related and organized, not how it is physically stored. In contrast, data structures such as arrays, linked lists, and trees describe how data is physically stored and accessed.

The relational model provides a way to describe relationships between data, while data structures provide a way to access and manipulate data efficiently. Both are important in computer science, and they serve different purposes.

However, the relational model has been criticized for its lack of performance compared to other data structures, particularly in certain types of applications such as scientific simulations and real-time systems. These criticisms are often used to justify the use of other data structures instead of relational databases.

Despite these criticisms, the relational model remains widely used in many applications due to its ability to handle complex relationships between data and its support for data integrity and consistency. It is also well-suited for applications where data is accessed and manipulated through a user interface, such as business applications and web applications.

In conclusion, the relational model and data structures serve different purposes in computer science, and each has its strengths and weaknesses. The choice between the two depends on the specific requirements of the application. Many people treat relational theory and data structures (data structure) as separate domains, regarding them as completely different. However, the theory of data structures can easily explain all the operations in relational databases.

In the relational model, each "relation" or "row" (row) represents nothing more than a "structure" in common language, just like a struct in C language or a class in Java. A table is simply an array of some structure (for example, Student[]). For instance, the following SQL statement creates a table:

CREATE TABLE Students {
[ID INT PRIMARY KEY,
Name VARCHAR(50),
Age INT,
Gender CHAR(1)]
}sid
CHAR(
20
)

This is likely a SQL statement, where "sid" is a variable name, "CHAR" is a data type, and "(20)" represents the length of the character string. The translation in English would be:

sid CHAR(20) name
(CHAR, 20),

login Chara's age is:

(20)

An integer type variable named "Chara" with a value of:

20. In fact, it is similar to the following structure array in C language:

struct {
 float gpa;
 char name[20];
} STUDENT_RECORD; struct student {
// empty
};

// The given Chinese text does not contain any meaningful information as it is written in a programming language syntax (C/C++), not in Chinese characters. The text seems to be defining an empty struct named "student". name;
char *sid;1. char pointer
2. login;
3. int [

This is a rough translation of the given Chinese text. It appears to be describing a variable declaration in C or C++ programming language. The first line is a declaration of a char pointer variable, and the second line is a statement for logging in. The third line is an incomplete declaration of an integer array or vector. age
;

double GPA Every database key is essentially the same as a pointer in C language, such as char* p. So-called "join" operation is accessing (dereferencing) the pointer, obtaining the object pointed to, just like in C language with *p. In implementation, join and pointer access have some differences, as join requires using software to query "indexes" (indices), so it is much slower than pointer access.

In essence, a database's query (query) is functional programming language operations like filter and map. The only difference is that relational algebra is more primitive and less flexible. For instance, the following SQL statement

SELECT
Book
. Title from Book; This Chinese text translates to 'price' in English.

100

Expresses the same thing as the following Lisp code:

(map \
#'identity \
'(price)) title (filter (lambda [x] x))

This is likely a Lisp-style code snippet in Chinese characters. The English translation would be:

title (filter (lambda (x) x)) book price

This text appears to contain a simplified Chinese representation of the English phrase "book price." The brackets and other symbols are likely not relevant to the translation. However, SQL's ability to nest and combine is much weaker than Lisp's, and many queries that you might think should be able to express naturally cannot be expressed in SQL. Nested queries are often a problem and require extending SQL syntax to implement, while Lisp naturally and elegantly expresses any nesting and combination.: Not deniable, some SQL lower implementations for basic queries might be more efficient, but the same can be said for the underlying running system of Lisp. We should not confuse "bottom layer implementation" with "higher level concepts."

A bad concept can be implemented quickly, but the concept itself is still bad, painful and confusing to use. A elegant design might be implemented inefficiently and slowly, but smart people can see the advantages in its concept and change the bottom layer implementation to create an efficient system. In fact, such a database system already exists, it expresses queries in a way similar to this text's Lisp style.

### Limitations of Relational Model

However, what the relational model can express is not beyond ordinary data structures, yet it has more limitations. Due to "rows" only having a fixed width, it causes the problem that you cannot put any "variable length" objects inside. For instance, if you have a dynamic length array, you cannot put it in one row. You need to take it out, rotate 90 degrees, and make it another table B. From table A, use a "foreign key" to point to B. It's even dumber that on each row of table B, this key needs to be repeated. The length of the array determines how many times this key needs to be repeated, occupying unnecessary large amounts of space. This foolish way of handling data from a data structure perspective, in the database field, has been given a profound and mysterious name, called "normalization" ;)

Operations like this, combined together, lead to the complexity of relational databases. To put it bluntly, normalization is just doing some manual work that is even lower level than C's manual memory management. Even C, this low level language, allows you to nest arrays in structures, but in the relational model, you cannot. Valuable human resources are spent on constructing, releasing, and connecting these "intermediate tables.": Some people (like this article) use a fifty-step approach, comparing relational models with other data models (Data Model, such as network models and so on) to support the necessity of relational models. You say I'm not good at relational models, try looking at something worse! If you understand all the details of this section, you'll find that you can represent relational models and those supposedly "superior" data models with basic data structures. These so-called "data models" are all empty talk, self-contained and self-generated.

Data models can be fully represented by ordinary data structures, yet they cannot simply and completely express the information that data structures carry. These data models are popular because they make people believe they understand concepts like "one-to-one," "one-to-many," and so on, and can replace the skills required to design data structures. So I believe that data models themselves are a "technical weight loss pill," telling you that you need to take several courses to see results, but in the end, it won't work, and it's your own fault if you messed up somewhere.

Instead of pinning your hopes on these "miraculous" weight loss pills labeled "mathematics," why not go to the nearby mediocre university and attend a fundamental data structures course?

### NoSQL

So E.F. Codd's relational theory (relational model, relational algebra) is the root cause of all this trouble, and SQL is just its sidekick. When people encounter problems with databases, they usually take out their anger on SQL, blaming it instead of the relational theory, which they fear due to the term "algebra." Once a concept is labeled as "relational algebra," you're not brave enough to criticize it, or people will say you don't understand, have insufficient knowledge, or can't grasp the "mathematics." The relationship-based theory and the SQL it engendered gave rise to a series of unnecessary issues, ultimately leading to the so-called "NoSQL movement." Many people consider NoSQL to be a revolutionary breakthrough, but in my opinion, it can at most be called "not foolish." Most NoSQL database designers did not see the problems mentioned above, or they deliberately created illusions, so the design of NoSQL databases did not completely free itself from the constraints of the relational model and SQL.

The earliest attempt to break through the limitations of the relational model and SQL was a technology called "column-based databases" (column-family databases), such as Vertica and HBase. These databases actually addressed the issue I mentioned earlier, that the relational model cannot store variable-length structures. Their so-called "column compression" is not more than adding representation and implementation of "arrays" in "row structures." A single key can be used to find all elements in an array, without normalization and repeating the key N times.

This is the way every beginner in programming would store an array, but it was excluded by the relational model. Column-based databases only corrected a historical stupid mistake and called it a major breakthrough. In fact, many column-based databases still have unnecessary limitations, such as limiting the nesting depth of variable-length arrays, and so on. Therefore, column-based databases have not been able to completely escape the thought shackles of relational databases. This obvious fact, database experts did not notice at the beginning. Later, they made adjustments and improvements, and called them "optimization" and "compression."

The latest NoSQL databases, such as Neo4j and MongoDB, have made some improvements in SQL's expressiveness issues. Neo4j designed a strange query language called Cypher, which not only has an odd syntax, weak expressiveness, but also has surprisingly low efficiency, making it necessary to use Java "extensions" for almost any practical operation. MongoDB and others use JSON to represent queries, which is essentially writing a syntax tree (AST) in the compiler, and it is not intuitive and prone to errors.

Now it is clear that the main problem with databases is language design. The NoSQL database field, due to the lack of responsible language experts and due to profit motives, will remain in chaos for a long time, causing suffering for users.more simplistically, a database issue is not that complicated, as it shares similarities with "remote procedure calls" (RPC). With any programming language, almost any programming language, you can send this language's code to a "data server". The server accepts and executes this code, indexes, queries, and restructures the data, then returns the result to the client. If you understand the essence of SQL, you will find that this "procedural design" does not lose SQL's "descriptive" ability. Instead, due to the simplicity and prevalence of procedural languages, development efficiency is significantly increased. NoSQL databases have advantages over SQL and relational databases because they are developing in a hazy direction towards this "RPC" method.

Some people say that directly programming is not good because managing external storage and index structures are error-prone codes, and it is better to use a database. But who told you that you have to write your own external storage and index codes? You can completely use refined code libraries, put them on the server, and make them into a "storage index system". Your "query code" only needs to be sent over and called these code libraries.

Therefore, in my mind, there is no longer a "database", "relational", or "NoSQL" concept, as they bring more trouble and complicate simple problems. In my mind, there is only more general and simple data structures, and efficient storage processing methods for them.