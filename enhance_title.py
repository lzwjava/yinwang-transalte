import os

title_mapping = {
    "2017-05-23-kotlin.md": "I. Kotlin and Checked Exceptions",
    "2023-12-23-cs-course-5.md": "CS Course 5",
    "2016-02-12-self-driving-car.md": "Self-Driving Car",
    "2019-09-30-autopilot-responsibility.md": "Autopilot Responsibility",
    "2021-02-16-cs-reading-course.md": "I. Computer Science Reading Class (Experiment)",
    "2013-07-13-church-turing.md": "Church and Turing",
    "2016-05-22-positive-thinking.md": "Misconceptions of Positive Thinking",
    "2016-09-14-tests.md": "Tests",
    "2013-04-15-terminology.md": "Several Cool Professional Terminologies",
    "2016-10-13-c-sharp-disposable.md": "IDisposable Interface in C#",
    "2017-08-14-travel-wisdom.md": "Traveling Wisely",
    "2016-07-10-tesla-autopilot-fatal-crash.md": "Tesla's Autopilot Caused Fatal Accident",
    "2021-04-16-cello-technique.md": "Why is the Cello so Hard to Learn?",
    "2019-09-14-machine-vs-human.md": "I. Machine and Human Visual Ability Gap (1)",
    "2012-07-04-dan-friedman.md": "GTF - Great Teacher Friedman",
    "2022-02-22-myopia.md": "Myopia",
    "2019-09-15-machine-vs-human-2.md": "Machine vs Human 2",
    "2015-09-19-parser.md": "Misunderstandings About Parser",
    "2019-07-21-pnp2.md": "PNP2",
    "2012-09-18-texmacs.md": "Texmacs",
    "2017-04-14-experience-and-insight.md": "Extensive Experience and Insight",
    "2018-02-16-chengdu-pollution.md": "The Fog in Chengdu",
    "2021-05-11-gucs-sample.md": "Title: Ground-Up Computer Science",
    "2013-03-08-on-syntax.md": "On Syntax",
    "2017-04-23-ai.md": "Artificial Intelligence Limitations",
    "2013-03-04-braid.md": "Braid",
    "2012-07-25-semantics.md": "What is Semantics?",
    "2021-09-16-youth-cs-student.md": "Youth CS Student",
    "2013-04-11-scheme-setup.md": "I. Scheme Programming Environment Setup",
    "2013-04-07-test-driven-dev.md": "Test-Driven Development (TDD)",
    "2019-07-12-learning-philosophy.md": "Wisdom in Learning",
    "2022-02-07-reading-course.md": "Reading Course",
    "2013-03-26-lisp-dead-alive.md": "Lisp is Dead, Long Live Lisp!",
    "2013-03-24-tools.md": "Tools",
    "2014-04-18-golang.md": "Golang",
    "2020-02-05-how-to-read-code.md": "How to Read Other People's Code",
    "2016-04-13-pay-blog.md": "Voluntary Paid Methods for Blog Posts",
    "2013-04-18-language-design-mistake2.md": "Language Design Mistake 2",
    "2016-01-18-java.md": "Giving Java a Fair Statement",
    "2015-02-01-creative-thinking.md": "A Isn't Great, I Suppose You Mean B Then?",
    "2013-04-10-cornell.md": "Why Did I Leave Cornell",
    "2014-02-09-programmer-mental.md": "Programmer's Psychological Disease",
    "2019-12-24-compilers.md": "Compilers",
    "2022-02-22-advanced-cs-course.md": "Advanced CS Course",
    "2015-06-07-software-engineering.md": "Alluded to as Software Engineering",
    "2013-03-15-language-design-mistake1.md": "Language Design Mistake 1",
    "2015-02-20-other-peoples-bug.md": "Other People's Bugs",
    "2014-02-18-dijkstra-interview.md": "An Interview Video About Dijkstra",
    "2015-10-18-turing.md": "Turing's Aura",
    "2013-11-25-pysonar2-sg.md": "Pysonar2-SG",
    "2017-05-25-dsl.md": "DSL (Domain Specific Language) Misconceptions",
    "2014-11-12-interstellar.md": "Interstellar",
    "2018-04-13-computer-science.md": "Mystery Computer Science",
    "2015-03-17-design.md": "The Importance of Design",
    "2014-01-04-authority.md": "I and the Story of Authority",
    "2013-03-07-linux-windows-mac.md": "About Linux, Windows, and Mac",
    "2015-12-21-tesla-model-x.md": "Tesla Model X Door Design Issues",
    "2013-04-17-languages.md": "About Language Pondering",
    "2015-11-21-programming-philosophy.md": "Programming Intelligence",
    "2017-05-17-practical-idealism.md": "Practical Idealism",
    "2020-03-23-wisdom-of-intelligence.md": "Doubts About Intelligence",
    "2013-04-02-currying.md": "Limitation of Currying",
    "2015-03-20-trap-of-intelligence.md": "Trap of Intelligence",
    "2016-09-18-rust.md": "Rust",
    "2015-03-11-git-etiquette.md": "About Git's Etiquette",
    "2017-11-05-words.md": "Words",
    "2016-03-09-alpha-go.md": "Alpha-Go",
    "2017-07-08-living-philosophy.md": "Living Philosophy",
    "2013-03-07-oberon.md": "Oberon Operating System: The Overlooked Jewel",
    "2015-03-21-accent.md": "Accent",
    "2020-05-23-american-english-problems.md": "American English Problems",
    "2013-04-01-lazy-evaluation.md": "Lazy Evaluation",
    "2013-04-13-generality.md": "Speaking of a Program's 'Generality'",
    "2015-07-04-math.md": "Mathematics and Programming",
    "2020-04-30-individualized-learning.md": "One-on-One Teaching Plan",
    "2015-06-14-dry-principle.md": "Principle Mistakes of DRY",
    "2013-04-14-standard-exam-language.md": "Standard Exam Language",
    "2017-10-16-ergonomics.md": "Body Science",
    "2016-06-08-java-value-type.md": "Does Java Have Value Types?",
    "2019-09-16-machine-vs-human-3.md": "Machine vs Human 3",
    "2019-09-11-talk-is-not-cheap.md": "Talk is Not Cheap",
    "2018-02-22-smart-contract.md": "Smart Contract",
    "2013-04-20-editor-ide.md": "Editor and IDE",
    "2017-11-04-alphago-zero.md": "Albgo Zero and Strong Artificial Intelligence",
    "2014-04-24-relational.md": "The Essence of Relational Models",
    "2013-03-07-design-patterns.md": "Decrypting 'Design Patterns'",
    "2020-03-06-english-learning-tips.md": "English Learning Experiences",
    "2022-12-12-continuation-course.md": "Advance and Concurrent Computing Focused Workshop",
    "2019-08-19-microkernel.md": "About Microkernel Dialogue",
    "2017-11-01-power-of-reasoning.md": "Rational Power",
    "2013-04-14-markdown.md": "Markdown Issues",
    "2015-04-03-paradigms.md": "Object-Oriented Programming (OOP)",
    "2021-02-15-cs3.md": "CS3",
    "2017-07-06-cat-travel-china.md": "Bringing a Cat Home from Abroad",
    "2016-06-06-swift.md": "Swift Language Design Flaw",
    "2013-03-31-purely-functional.md": "Purely Functional",
    "2013-04-01-hindley-milner.md": "Hindley-Milner"
}


def update_file_title(file_path, new_title):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith('title:'):
                file.write(f'title: "{new_title}"\n')
            else:
                file.write(line)

# Iterate through the files in the directory


def update_titles_in_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name in title_mapping:
            file_path = os.path.join(directory_path, file_name)
            new_title = title_mapping[file_name]
            update_file_title(file_path, new_title)
            print(f'Updated title in {file_name} to "{new_title}"')


# Example usage
directory_path = './translated_texts'
update_titles_in_directory(directory_path)
