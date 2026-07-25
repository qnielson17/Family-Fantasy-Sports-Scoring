import numpy as np
import pandas as pd

def score_gp(filename, sprint = False):
    arr = np.genfromtxt(filename, delimiter = ',', dtype = None, skip_header = 5, skip_footer = 1)

    # Free Practice 1
    fp1_result = arr[:,1][2:5]
    fp1_da = arr[:,2][2:5]
    fp1_moto = arr[:,3][2:5]
    fp1_quincey = arr[:,4][2:5]
    fp1_wynn = arr[:,5][2:5]
    fp1_paige = arr[:,6][2:5]
    fp1_rees = arr[:,7][2:5]

    if sprint == False: # Weeks without sprint races have three free practice sessions
        # Free Practice 2
        fp2_result = arr[:,9][2:5]
        fp2_da = arr[:,10][2:5]
        fp2_moto = arr[:,11][2:5]
        fp2_quincey = arr[:,12][2:5]
        fp2_wynn = arr[:,13][2:5]
        fp2_paige = arr[:,14][2:5]
        fp2_rees = arr[:,15][2:5]

        # Free Practice 3
        fp3_result = arr[:,17][2:5]
        fp3_da = arr[:,18][2:5]
        fp3_moto = arr[:,19][2:5]
        fp3_quincey = arr[:,20][2:5]
        fp3_wynn = arr[:,21][2:5]
        fp3_paige = arr[:,22][2:5]
        fp3_rees = arr[:,23][2:5]

    elif sprint == True: # Weeks with sprint race replace FP2 with sprint qualifying and FP3 with the sprint
        # Sprint Qualifying
        sq_result = arr[:,9][2:7]
        sq_da = arr[:,10][2:7]
        sq_moto = arr[:,11][2:7]
        sq_quincey = arr[:,12][2:7]
        sq_wynn = arr[:,13][2:7]
        sq_paige = arr[:,14][2:7]
        sq_rees = arr[:,15][2:7]

        # Sprint
        sprint_result = arr[:,17][2:10]
        sprint_da = arr[:,18][2:10]
        sprint_moto = arr[:,19][2:10]
        sprint_quincey = arr[:,20][2:10]
        sprint_wynn = arr[:,21][2:10]
        sprint_paige = arr[:,22][2:10]
        sprint_rees = arr[:,23][2:10]

    # Qualifying
    quali_result = arr[:,25][2:12]
    quali_da = arr[:,26][2:12]
    quali_moto = arr[:,27][2:12]
    quali_quincey = arr[:,28][2:12]
    quali_wynn = arr[:,29][2:12]
    quali_paige = arr[:,30][2:12]
    quali_rees = arr[:,31][2:12]

    # Race
    race_result = arr[:,33][2:25]
    race_da = arr[:,34][2:25]
    race_moto = arr[:,35][2:25]
    race_quincey = arr[:,36][2:25]
    race_wynn = arr[:,37][2:25]
    race_paige = arr[:,38][2:25]
    race_rees = arr[:,39][2:25]

    # Create DataFrame of weekend results
    names = [arr[1][2], arr[1][3], arr[1][4], arr[1][5], arr[1][6], arr[1][7]]
    if sprint == False:
        indices = ['FP1', 'FP2', 'FP3', 'Quali', 'Race']
    elif sprint == True:
        indices = ['FP1', 'SQ', 'Sprint', 'Quali', 'Race']
        
    df = pd.DataFrame(np.nan, index = indices, columns = names)

    # Score points for each session
    # Set FP1 Scores
    df.loc['FP1','Dad'] = score_practice(fp1_result, fp1_da)
    df.loc['FP1','Mom'] = score_practice(fp1_result, fp1_moto)
    df.loc['FP1','Quincey'] = score_practice(fp1_result, fp1_quincey)
    df.loc['FP1','Wynn'] = score_practice(fp1_result, fp1_wynn)
    df.loc['FP1','Paige'] = score_practice(fp1_result, fp1_paige)
    df.loc['FP1','Rees'] = score_practice(fp1_result, fp1_rees)

    if sprint == False:
        # Set FP2 Scores
        df.loc['FP2','Dad'] = score_practice(fp2_result, fp2_da)
        df.loc['FP2','Mom'] = score_practice(fp2_result, fp2_moto)
        df.loc['FP2','Quincey'] = score_practice(fp2_result, fp2_quincey)
        df.loc['FP2','Wynn'] = score_practice(fp2_result, fp2_wynn)
        df.loc['FP2','Paige'] = score_practice(fp2_result, fp2_paige)
        df.loc['FP2','Rees'] = score_practice(fp2_result, fp2_rees)

        # Set FP3 Scores
        df.loc['FP3','Dad'] = score_practice(fp3_result, fp3_da)
        df.loc['FP3','Mom'] = score_practice(fp3_result, fp3_moto)
        df.loc['FP3','Quincey'] = score_practice(fp3_result, fp3_quincey)
        df.loc['FP3','Wynn'] = score_practice(fp3_result, fp3_wynn)
        df.loc['FP3','Paige'] = score_practice(fp3_result, fp3_paige)
        df.loc['FP3','Rees'] = score_practice(fp3_result, fp3_rees)
    elif sprint == True:
        # Set Sprint Qualifying scores
        df.loc['SQ','Dad'] = score_sprint_quali(sq_result, sq_da)
        df.loc['SQ','Mom'] = score_sprint_quali(sq_result, sq_moto)
        df.loc['SQ','Quincey'] = score_sprint_quali(sq_result, sq_quincey)
        df.loc['SQ','Wynn'] = score_sprint_quali(sq_result, sq_wynn)
        df.loc['SQ','Paige'] = score_sprint_quali(sq_result, sq_paige)
        df.loc['SQ','Rees'] = score_sprint_quali(sq_result, sq_rees)

        # Set Sprint Scores
        df.loc['Sprint','Dad'] = score_sprint(sprint_result, sprint_da)
        df.loc['Sprint','Mom'] = score_sprint(sprint_result, sprint_moto)
        df.loc['Sprint','Quincey'] = score_sprint(sprint_result, sprint_quincey)
        df.loc['Sprint','Wynn'] = score_sprint(sprint_result, sprint_wynn)
        df.loc['Sprint','Paige'] = score_sprint(sprint_result, sprint_paige)
        df.loc['Sprint','Rees'] = score_sprint(sprint_result, sprint_rees)

    # Set Quali Scores
    df.loc['Quali','Dad'] = score_quali(quali_result, quali_da)
    df.loc['Quali','Mom'] = score_quali(quali_result, quali_moto)
    df.loc['Quali','Quincey'] = score_quali(quali_result, quali_quincey)
    df.loc['Quali','Wynn'] = score_quali(quali_result, quali_wynn)
    df.loc['Quali','Paige'] = score_quali(quali_result, quali_paige)
    df.loc['Quali','Rees'] = score_quali(quali_result, quali_rees)

    # Set Race Scores
    df.loc['Race','Dad'] = score_race(race_result, race_da)
    df.loc['Race','Mom'] = score_race(race_result, race_moto)
    df.loc['Race','Quincey'] = score_race(race_result, race_quincey)
    df.loc['Race','Wynn'] = score_race(race_result, race_wynn)
    df.loc['Race','Paige'] = score_race(race_result, race_paige)
    df.loc['Race','Rees'] = score_race(race_result, race_rees)

    return df

def score_practice(result, guess):
    if len(result) != len(guess):
        print(f"ERROR: Length of results and guesses do not match. Check that your session matches for both results and guesses.")

    score = 0
    for i in range(len(guess)):
        # Driver in correct position = 3 points
        if result[i] == guess[i]: 
            score += 3
        # Driver in top 3 in incorrect position = 1 point
        elif guess[i] in result:
            score += 1
    
    # Check maximum score
    if score > 9: 
        print(f"ERROR: Score exceeds maximum points possible. Check that you have submitted the correct session.")

    return score

def score_sprint_quali(result, guess): 
    if len(result) != len(guess):
            print(f"ERROR: Length of results and guesses do not match. Check that your session matches for both results and guesses.")

    score = 0
    front_row = result[0:2]
    for i in range(len(guess)):
        # Driver in correct front row position = 5 points
        if  i < 2 and result[i] == guess[i]:
            score += 5
        # Driver in correct position (non-front row) = 3 points
        elif i > 1 and result[i] == guess[i]:
            score += 3
        # Driver in top 5 but incorrect position = 1 point
        elif guess[i] in result:
            score += 1

    # Check maximum score
    if score > 19: 
        print(f"ERROR: Score exceeds maximum points possible. Check that you have submitted the correct session.")

    return score

def score_sprint(result, guess): 
    if len(result) != len(guess):
            print(f"ERROR: Length of results and guesses do not match. Check that your session matches for both results and guesses.")

    score = 0
    podium = result[0:3]
    for i in range(len(guess)):
        # Driver as sprint winner = 17 points
        if i == 0 and result[i] == guess[i]:
            score += 17
        # Driver on podium (non-winner) in correct position = 13 points
        elif 0 < i and i < 3 and result[i] == guess[i]:
            score += 13
        # Driver on prodium (non-winner) in incorrect position = 10 points
        elif i < 3 and guess[i] in podium:
            score += 10
        # Driver guess in correct position (non-podium) = 8 points
        elif i > 2 and result[i] == guess[i]:
            score += 8
        # Driver guess in top 8 in incorrect position = 3 points
        elif guess[i] in result:
            score += 3

    # Check maximum score
        if score > 83: 
            print(f"ERROR: Score exceeds maximum points possible. Check that you have submitted the correct session.")

    return score

def score_quali(result, guess):
    if len(result) != len(guess):
            print(f"ERROR: Length of results and guesses do not match. Check that your session matches for both results and guesses.")

    score = 0
    front_row = result[0:2]
    top4 = result[0:4]
    for i in range(len(guess)):
        # Driver in correct front row position = 7 points
        if i < 2 and result[i] == guess[i]:
            score += 7
        # Driver in correct position (non-front row) = 5 points
        elif i > 1 and result[i] == guess[i]:
            score += 5
        # Driver in front two rows but incorrect position = 2 points
        elif i < 4 and guess[i] in top4:
            score += 2
        # Driver in top ten but incorrect position = 1 point
        elif guess[i] in result:
            score += 1

    # Check maximum score
        if score > 54: 
            print(f"ERROR: Score exceeds maximum points possible. Check that you have submitted the correct session.")

    return score

def score_race(result, guess):
    if len(result) != len(guess):
            print(f"ERROR: Length of results and guesses do not match. Check that your session matches for both results and guesses.")

    score = 0
    podium = result[0:3]
    points = result[0:10]
    for i in range(len(guess)):
        # Driver guess as winner = 50 points
        if i == 0 and result[i] == guess[i]:
            score += 50
        # Driver guess on podium (non-winner) in correct position = 40 points
        elif i < 3 and result[i] == guess[i]:
            score += 40
        # Driver guess on podium (non-winner) in incorrect position = 30 points
        elif i < 3 and guess[i] in podium:
            score += 30
        # Driver guess in correct position (non-podium) = 25 points
        elif i > 2 and result[i] == guess[i]:
            score += 25
        # Driver guess in "the points" i.e. top ten in incorrect position = 10 points
        elif i < 10 and guess[i] in points:
            score += 10

    # Check maximum score
        if score > 605: 
            print(f"ERROR: Score exceeds maximum points possible. Check that you have submitted the correct session.")

    return score