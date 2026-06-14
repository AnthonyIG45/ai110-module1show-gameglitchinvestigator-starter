from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# Custom string-handling validation tests

def test_guess_matches_string_secret():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_too_high_with_string_secret():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_too_low_with_string_secret():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"

# Custom tests to handle different input variables and see reaction

def test_parse_invalid_text():
    ok, value, err = parse_guess("abc")
    assert not ok
    assert value is None
    assert err == "That is not a number."

def test_parse_empty_string():
    # An empty input string should return a specific prompt message
    ok, value, err = parse_guess("")
    assert not ok
    assert err == "Enter a guess."

def test_parse_none_input():
    # Protects the app if a None type somehow slips into the parser
    ok, value, err = parse_guess(None)
    assert not ok
    assert err == "Enter a guess."

def test_parse_decimal_string():
    # Your float logic drops decimals. "50.9" should safely convert to integer 50
    ok, value, err = parse_guess("50.9")
    assert ok
    assert value == 50
    assert err is None

# Custom tests for edge cases with comparisons like extremely large values and negative values

def test_check_guess_negative_number():
    outcome, _ = check_guess(-15, 50)
    assert outcome == "Too Low"

def test_check_guess_extremely_large_number():
    outcome, _ = check_guess(999999999999, 50)
    assert outcome == "Too High"

# Custom tests for update_score edge cases

def test_update_score_win_points_floor():
    # If attempt_number is huge (e.g. 25), the formula 100 - 10 * (25 + 1) drops below zero.
    # The score should clamp and award the absolute minimum floor of 10 points.
    starting_score = 100
    new_score = update_score(
        current_score=starting_score, 
        outcome="Win", 
        attempt_number=25, 
        previous_outcome=None
    )
    # 100 starting points + 10 minimum guaranteed win points = 110
    assert new_score == 110

def test_update_score_consecutive_same_mistakes():
    # Tests your logic that two consecutive high/low answers penalize the user twice (-10 total)
    starting_score = 20
    
    # First high guess (-5)
    score_after_first = update_score(starting_score, "Too High", 1, None)
    # Second high guess (-5)
    score_after_second = update_score(score_after_first, "Too High", 2, "Too High")
    
    assert score_after_second == 10

def test_update_score_inverse_neutralization():
    # Tests that an inverse response flawlessly balances out to +5 points
    starting_score = 20
    new_score = update_score(
        current_score=starting_score, 
        outcome="Too High", 
        attempt_number=2, 
        previous_outcome="Too Low"
    )
    
    assert new_score == 25