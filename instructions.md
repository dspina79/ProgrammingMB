# Zoo Program: Your Tasks

Welcome, Scout! This program models a zoo full of animals. It works, sort of, but it has some bugs and some missing features. Your job is to fix and finish it.


## How the code is organized

| File | What it does |
|------|--------------|
| `animal.py` | The `Animal` base class. Every animal has a `name`, a `move()` method and an `animal_type()` method. |
| `menagerie.py` | All the specific animals (`Giraffe`, `Lion`, `Elephant`, and so on). Each one is a class that **inherits** from `Animal`. |
| `zoo.py` | The `Zoo` class, which keeps track of the animals at the zoo. |
| `main.py` | The script you run. It builds a zoo, adds animals and prints the roster. |

Run `python main.py` after each task to check your work. Add or change animals in `main.py` as you go to test your changes.

---

## Task 1: Make the animals migrate

In `zoo.py`, the `migrate()` method is empty. It only contains `pass`.

**Goal:** When you call `zoo.migrate()`, every animal in the zoo should print its `move()` message.

**Check your work:** Add `zoo.migrate()` to the end of `main.py`. You should see one line of movement for each animal you added, including both lions.

> 💡 **Think about it:** Look at what `Zoo` actually stores in `self.animals`. Does it keep the animal objects, or something else? Can you call `move()` on what's stored there? You may need to change how the zoo keeps track of its animals.

---

## Task 2: Remove an animal from the zoo

In `zoo.py`, the `remove_animal(self, animal_type, animal_name)` method is also empty.

**Goal:** Remove **one specific animal**, the one whose type and name both match. If the zoo has 4 lions and you call `zoo.remove_animal('Lion', 'Beth')`, only Beth should leave. The other 3 lions stay.

**Check your work:**
- Add several lions with different names, remove one, then print the roster. The lion count should go down by exactly one.
- Call `migrate()` afterward. The removed animal should no longer appear.
- What happens if you try to remove an animal that isn't in the zoo? Make sure the program doesn't crash.

---

## Task 3: Lions are showing up as giraffes!

Run `python main.py`. The program adds two lions and an elephant, but the roster says there are giraffes at the zoo.

**Goal:** Find out why lions are counted as giraffes and fix it.

**Check your work:** The roster should list `Lion` with a count of 2.

> 💡 **Hint:** The zoo groups animals using `animal_type()`.

---

## Task 4: The roster total is wrong

At the bottom of the roster, `print_roster()` prints the total number of animals at the zoo. Compare that number to the animals you actually added in `main.py`.

**Goal:** Fix `print_roster()` so the total matches the real number of animals.

**Check your work:** With 2 lions and 1 elephant, the total should be **3**. Add more animals and make sure the total still matches.

---

## Task 5: New animals are arriving

The zoo is getting four new kinds of animals:

- Penguin
- Red Panda
- Zebra
- Bat

**Goal:** Add a class for each one in `menagerie.py`. Each class should:

1. Inherit from `Animal`.
2. Be named for the animal. (Class names can't have spaces. How would you name the red panda?)
3. Override `animal_type()` so it returns its own name.

**Check your work:** Add at least one of each new animal in `main.py`. Each should show up on the roster under its own name with the right count.

---

## Task 6: Give the animals their own moves

Right now, most animals use the plain `move()` from `Animal`, which just prints something like `Archie moves.` That's boring!

**Goal:** Override `move()` in **at least 3 different animal classes** so each one moves in its own way. For example, a bat might fly through the night sky and a penguin might waddle or swim.

**Check your work:** Run `zoo.migrate()`. Your animals should each print their own movement instead of the default message.

---

## Bonus challenges

- Add a special method for one of your new animals, like `Elephant` has `remember()`.
- Make the roster print its columns neatly lined up.

## Discuss with your counselor

- What is **inheritance**, and how does this program use it?
- What does it mean to **override** a method? Point to an example in your code.
- Why did you have to change how `Zoo` stores animals to finish Tasks 1 and 2?
