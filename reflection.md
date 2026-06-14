# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  + The game appeared okay showing a difficulty changing setting, location for a guess, new game button, submit guess button, show/hide hints, and Developer Debug Info.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  + Does not restart the game when pressing "New Game".
  + The hints are backwards and don't really make sense.
  + Difficulty selection does not change secret number or change the guess parameters.
  + Normal and Hard difficulty statistics were swapped.
  + Odd vs Even number of attempts remaining affects what type the secret number is being compared as (string - Int vs Int - Int).
  + logic_utils.py isn't properly imported into app.py.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret: 66, Guess: 50 | Expected Hint: Guess Higher | Actual Hint: Guess Lower | No errors, just incorrect hint output |
| New Game | Clicking should set new game guess to 1 | Sets Current guess to 0 which is out of loop scope| Game does not properly restart |
| Difficulty Switching| Should Switch secret range between 20 - 100 and number of guesses | Switches amount of guesses allowed, does not change secret number | Improper switch |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  + I used Gemini to help remind me of the git commands for forking, cloning, and making new commits.
  + Claude Sonnet was used to assist in actually inspecting and altering specific files like explaining what error meant, how to make changes,
  + and where bugs were located at.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  + Attempts starts at 1, but New Game resets to 0 (app.py:96-97 vs app.py:135) — inconsistent initialization means the first game shows one fewer attempt than available.

  + This was correct reviewing the code and on launch, it sets your attempt at 1, then pressing "New Game" would set attempt to 0 which was out of bounds for the play loop.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  + At the top of app.py, add this import line:
  + from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score
  + Then delete the 4 function definitions that are currently in app.py (lines 4–65), since they'll now live in logic_utils.py.
  + The functions are in the same directory as app.py, so no path gymnastics needed — Python finds logic_utils.py automatically when you run from that folder.

  + I verified that the refactoring does technically work, but it messes up the streamlit UI to include all of that code as a comment and text box at the top when running.
  + It was partially true.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  + Reruns essentially restarts certain logic in streamlit whereas states to refresh a given game or session activity. Like in a videogame, if you win a round and both teams switch sides.
  + The teams maintain their score and their mid-game stats, but everyone is back alive and no one has any active streaks. This would be an example of a rerun. A session state would be
  + like if you were playing the game, watching an end-match screen, sitting in lobby, or loading into a new match.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
