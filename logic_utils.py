#FIIXED: Difficulty now makes sense

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 50
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100

def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIXED: Logic now properly displays Higher or Lower

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

#FIXED: If a hint is followed by the inverse hint, scores nullify. If 2 of the same are followed by each other, score -5 each time.
#EXAMPLE: "Go Higher" -5 then "Go Lower" +5 Total points = 0. "Go Higher" -5 then "Go Higher" -5 Total points = -10.

def update_score(current_score: int, outcome: str, attempt_number: int, previous_outcome: str):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    is_inverse = (outcome == "Too High" and previous_outcome == "Too Low") or (outcome == "Too Low" and previous_outcome == "Too High")

    if is_inverse:
        return current_score + 5
    
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5

    return current_score
