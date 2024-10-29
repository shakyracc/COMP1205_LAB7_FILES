**School of Science, Computing and Artificial Intelligence**
**The University of the West Indies, Five Islands**  

# COMP1205 - Lab 6: Files & Exceptions

## Instructions

### 1. Mad Libs Program
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word **ADJECTIVE**, **NOUN**, **ADVERB**, or **VERB** appears in the text file. For example, a text file may look like this:

```
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
```

The program would find these occurrences and prompt the user to replace them.

Example interaction:

```
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
```

The following text file would then be created:

```
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
```

The results should be printed to the screen and saved to a new text file.

### 2. Scrabble Scoring

In the Scrabble game, you have some tiles in your hand, each with a letter on it, and your goal is to form a word using any combination of those letters. Different letters are worth different numbers of points. For example, an “a” is worth only one point, because “a” is such a common letter. But “q”? “z”? Those doozies are each worth ten points, because they’re so tough to use. . . . or should we say ”puzzling” to use. Yes, that’s better. To calculate the score for a word, we add up the scores for each of its letters. For example, the score for “zap” would be 14. That’s because z is worth 10, a is worth 1, and p is worth 3.

Each letter is worth the following points:

- **1 point**: a, e, i, o, u, l, n, s, t, r
- **2 points**: d, g
- **3 points**: b, c, m, p
- **4 points**: f, h, v, w, y
- **5 points**: k
- **8 points**: j, x
- **10 points**: q, z

#### Tasks
- **(a)** Write a function that, given a word, tells you how many points that word is worth.
- **(b)** Suppose that there are a bunch of words that can be made right now, but we don’t know which one will give the most points. Should you make the word “zap”? “pack”? “quack”? Write a function that could take a bunch of words and tell us which is the best one. Consider: How many parameters should we have in such a function?