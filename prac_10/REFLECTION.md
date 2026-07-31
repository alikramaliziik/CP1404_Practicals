# Practical 10 – Testing, APIs, and Course Reflection

## Programs

| File | Description |
|------|-------------|
| `testing.py` | Unit tests and doctests for `repeat_string()`, `is_long_word()`, `format_sentence()`, and the `Car` class — verifying correct behaviour using `assert` statements and `doctest.testmod()` |
| `wiki.py` | Wikipedia API client that fetches page title, summary, and URL, handling `PageError` and `DisambiguationError` gracefully |

---

## CP1404 Practical Reflection – Week 10

### Estimates

**How was your estimate accuracy usually?**  
My estimates were mostly moderate — the difference between estimated and actual time was generally small, but the actual time taken was consistently a bit longer than planned.

**How did your estimate accuracy improve or change during the course of the subject?**  
Over time I started factoring in unplanned events like persistent bugs, and I began allocating buffer time for those situations. That made my later estimates more realistic than my early ones.

**What did you learn from doing these estimates?**  
Having an estimate improves time management and sharpens focus — knowing that time is running helps me stay attentive and concentrated on the task rather than drifting.

---

### Code Reviews

**What have you learned from being reviewed by other people?**  
Being reviewed gave me broader perspectives on my code that I had not considered myself. It improved both my understanding of the code and my ability to communicate about it clearly.

**What have you learned from doing code reviews of other people?**  
Reviewing others' code showed me that there are many valid ways to solve the same problem. Different people take different approaches and still arrive at a correct solution, which expanded how I think about writing my own code.

**Good Code Review 1**
- [Dharshanaprasad – Prac 8 review](https://github.com/Dharshanaprasad/cp1404practicals/pull/4#issuecomment-3132828884)

This was the code review for Practical 8, focused on class reuse of the Guitar class with classification by year. The code followed good principles including error catching and proper flow control, which gave me a solid example of clean OOP structure to learn from.

**Good Code Review 2**
- [Alex-M-K-wong – Prac 5 review](https://github.com/alikramaliziik/CP1404-PRACTICALS/pull/1#issuecomment-3066672501)

This code review covered Practical 5, which included reading from and writing to files. The code demonstrated good error checking for missing files and made good use of methods and classes, reinforcing the importance of defensive file handling.

---

### Practicals Overall

**What would you change if you were in charge of the subject?**  
There is nothing to change — the quality is top notch and the materials are user-friendly, making learning enjoyable and practical.

**What did you do really well for practicals in this subject?**  
The use of methods throughout the subject — which makes code more maintainable, promotes reuse, and improves readability. Also class reuse, such as writing a base `Car` class and then implementing various versions like `Taxi` and `SilverServiceTaxi` under it, which reinforced good object-oriented design.
