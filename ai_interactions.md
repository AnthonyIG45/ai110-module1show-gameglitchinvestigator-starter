# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

    + I used both Gemini and Claude for this assignment. I mainly used claude for reading my files so I could sync any logic between the files like app.py and logic_utils.py.
    + I used Gemini to help me reason through some of the fixes I needed, helping with syntax, and writing the tests.

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

    + Claude was able to directly suggest and even make changes to my files, some of which I looked over and decided were acceptable, and a few that I felt the AI
    + Went on a bit of a trail and tried to make logic unnecessarily complex.

    + Gemini was extremely helpful in explaining certain small snippets of code and helping me brainstorm edge-case ideas without outright writing the test for me
    + So I could practice and learn how pytest works for future reference.

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

    + I manually verified everything that Claude tried to replace or update in my code. I did have to manually fix the point logic because it wasn't really understanding
    + How I wanted the point system to work from my explaination which could also be considered used error. I did much more prefer when it gave me smaller, more contained
    + Code fixes as opposed to when it tried to recommend changing a large amount of lines of code all at once. Made it easier to follow its reasoning and the code logic.

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Testing update bounds (Point calculation) | What is a potential logical test for point addition and final calculation? | Test expected final point output given specific inputs | Yes | Should take amount of attempts times 10 minus 100 and also subtract the points already removed from consecutive guesses. Works as should for worst case of guessing correct on last guess. |
| Testing different user inputs | How can I test potential parse edge cases like negatives, large ints, decimals, and text? | Suggested tests for each case which was handled in code. | Yes | And suggested another interesting test if the user attempted to pass a command or something like "None" which it treats strictly as text and not a command. |
| Testing the value conversion issues | How can I test the value conversion issue in logic_utils.py? | Suggested adding a test where the secret value is submitted as a string. | Yes | Handled in code by making sure that before any processing, that guess and secret are cast as ints. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
