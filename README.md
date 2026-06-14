# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Games purpose is to generate a random number and have the user guess it with a set amount of guesses while being provided hints. Multiple difficulties with point amounts.

- Bugs Found:
   1. Issue with type conversion when checking guess to secret.
   2. All logic and UI code in app.py, need to seperate logic and refactor (not much of a bug but a coding courtesy)
   3. Points did not add properly or make sense
   4. Did not properly restart when pressing "New Game"
   5. Changing the difficulty literally does nothing
   6. Hints are backward and don't really work in general

- Fixes Applied:
   1. Normalize types making sure that guess and secret are always tried as ints regardless of the input variable type.
   2. Refactored code and separated logic (UI and Game Logic)
   3. Adjusted points to multiply based off difficulty chosen and based off consecutive guesses (Double too high/low gives deficit while consecutive inverse guess types nuetralize point loss)
   4. New game actually properly reruns the game. Adjusted initial attempt from 1 to 0, fixed UI issue too with -1 attempt showing if you lose
   5. Difficulty now reruns everything when swapped and the difficulty parameters are actually applied
   6. Hints now show if you are below the secret number, above the secret, or if you win or lose (run out of attempts)

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Game initiates defaulting to normal mode (7 attempts, secret number between 1-100)
2. User enters 40
3. Output is "Too Low", -5 points
4. User enters 75
5. Output is "Too High", +5 points
6. User enters 62
7. Outpit is "Win! The secret number was 62!"
8. User is awarded 70 points (100 - (10 * (2 attempts) + 1))
9. User presses "New Game" and a new number is generated and attempts are reset
10. User changes difficulty to hard mode (5 attempts, secret number between 1-200, point gain multiplied because of difficulty)

## 🧪 Test Results

================================================================================================================================================ test session starts ================================================================================================================================================
platform win32 -- Python 3.13.14, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\...\Code\CodePath\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 15 items                                                                                                                                                                                                                                                                                                   

tests\test_game_logic.py ...............                                                                                                                                                                                                                                                                       [100%]

================================================================================================================================================ 15 passed in 0.04s =================================================================================================================================================

## 🚀 Stretch Features

- I added the st.form for the submission box for inputs. Easier on the user for submitting answers to then be able to submit their next choice.
- Added a point multiplier for winning based off the difficulty the user is on.
