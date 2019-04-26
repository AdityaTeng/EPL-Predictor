import pandas as pd
import numpy as np 
import math

df = pd.read_csv('Downloads/E0.csv')
df1 = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]

def predictor(home_team, away_team):
	#Total Games Played (TGP)
	TGP = len(df.index)
	print(TGP)

	#Total Home Goals (THG)
	count_1=0
	THG=0 
	for i in range(0,TGP):
	    temp_1 = int(df1.iat[count_1,3])
	    THG = THG + temp_1
	    count_1 = count_1+1
	print(THG)

	#Total Average Away Goals Scored (TAHGS)
	TAHGS = THG/TGP
	print(TAHGS)

	#Total Away Goals (TAG)
	count_2=0
	TAG=0 
	for i in range(0,TGP):
	    temp_2 = int(df1.iat[count_2,4])
	    TAG = TAG + temp_2
	    count_2 = count_2+1
	print(TAG)

	#Total Average Away Goals Scored (TAAGS)
	TAAGS = TAG/TGP
	print(TAAGS)

	#Total Average Home Goals Conceded (TAHGC) &
	#Total Average Away Goals Conceded (TAAGC)
	TAHGC = TAAGS
	TAAGC = TAHGS


	#Get Home Team & Away TEam from User
	HT = df1.loc[df1['HomeTeam'] == home_team]
	AT = df1.loc[df1['AwayTeam'] == away_team]

	#Home Team Games Played (HTGP) &
	#Away Team Games Played (ATGP)
	HTGP = len(HT.index)
	ATGP = len(AT.index)
	
	#Home Team Total Home Goals Scored (HTTHGS)
	count_3=0
	HTTHGS=0 
	for i in range(0,HTGP):
	    temp_3 = int(HT.iat[count_3,3])
	    HTTHGS = HTTHGS + temp_3
	    count_3 = count_3+1
	print(HTTHGS)

	#Home Team Average Home Goals Scored (HTAHGS)
	HTAHGS = HTTHGS/HTGP
	print(HTAHGS)

	#Home Team Attack Strength (HTAS)
	HTAS = HTAHGS/TAHGS
	print(HTAS)

	#Home Team Total Home Goals Conceded (HTTHGC)
	count_4=0
	HTTHGC=0 
	for i in range(0,HTGP):
	    temp_4 = int(HT.iat[count_4,4])
	    HTTHGC = HTTHGC + temp_4
	    count_4 = count_4+1
	print(HTTHGC)

	#Home Team Average Home Goals Conceded (HTAHGC)
	HTAHGC = HTTHGC/HTGP
	print(HTAHGC)

	#Home Team Defence Weakness (HTDW)
	HTDW = HTAHGC/TAHGC
	print(HTDW)

	#Away Team Total Away Goals Scored (ATTAGS)
	count_5=0
	ATTAGS=0 
	for i in range(0,ATGP):
	    temp_5 = int(AT.iat[count_5,4])
	    ATTAGS = ATTAGS + temp_5
	    count_5 = count_5+1
	print(ATTAGS)

	#Away Team Average Away Goals Scored (ATAAGS)
	ATAAGS = ATTAGS/ATGP
	print(ATAAGS)

	#Away Team Attack Strength (ATAS)
	ATAS = ATAAGS/TAAGS
	print(ATAS)

	#Away Team Total Away Goals Conceded (ATTAGC)
	count_6=0
	ATTAGC=0
	for i in range(0,ATGP):
	    temp_6 = int(AT.iat[count_6,3])
	    ATTAGC = ATTAGC + temp_6
	    count_6 = count_6+1
	print(ATTAGC)

	#Away Team Average Away Goals Conceded (ATAAGC)
	ATAAGC = ATTAGC/ATGP
	print(ATAAGC)

	#Away Team Defence Weakness (ATDW)
	ATDW = ATAAGC/TAAGC
	print(ATDW)

	#Expected Home Team Goals &
	#Expected Away Team Goals
	λ_H = HTAS*ATDW*TAHGS
	λ_A = ATAS*HTDW*TAAGS
	print('Expected Home Team Goals = ',λ_H)
	print('Expected Away Team Goals = ',λ_A)

	#Poisson Distribution Formula:
	#P(k)= [{λ^(k)} * {e^(-λ)}]/ k!
	#Where λ is the no. of expected goals and k is the no. of goals
	Exp_H = np.exp(-λ_H) 
	Exp_A = np.exp(-λ_A)
	print(Exp_H)
	print(Exp_A)

	#Probability of Home Team Goals (0-8)
	PHTG = []
	for x in range(0,8):
	    temp_7 = (λ_H**x)*(Exp_H/math.factorial(x))
	    PHTG.append(temp_7)

	print(PHTG)

	#Probability of Away Team Goals (0-8)
	PATG = []
	for x in range(0,8):
	    temp_8 = (λ_A**x)*(Exp_A/math.factorial(x))
	    PATG.append(temp_8)

	print(PATG)

	#Creating Lists for Probability Table Dataframe
	list0 = []
	list1 = []
	list2 = []
	list3 = []
	list4 = []
	list5 = []
	list6 = []
	list7 = []

	for i in range(0,8):
	    temp_9 = PHTG[0]*PATG[i]
	    list0.append(temp_9)

	for i in range(0,8):
	    temp_10 = PHTG[1]*PATG[i]
	    list1.append(temp_10)

	for i in range(0,8):
	    temp_11 = PHTG[2]*PATG[i]
	    list2.append(temp_11)

	for i in range(0,8):
	    temp_12 = PHTG[3]*PATG[i]
	    list3.append(temp_12)

	for i in range(0,8):
	    temp_13 = PHTG[4]*PATG[i]
	    list4.append(temp_13)

	for i in range(0,8):
	    temp_14 = PHTG[5]*PATG[i]
	    list5.append(temp_14)

	for i in range(0,8):
	    temp_15 = PHTG[6]*PATG[i]
	    list6.append(temp_15)
	    
	for i in range(0,8):
	    temp_16 = PHTG[7]*PATG[i]
	    list7.append(temp_16)
	    
	print(list0)
	print(list1)
	print(list3)
	print(list3)
	print(list4)
	print(list5)
	print(list6)
	print(list7)

	#Probability Table
	PT = pd.DataFrame({0:list0,1:list1,2:list2,3:list3,4:list4,5:list5,6:list6,7:list7})
	PT

	#Home Team Winning Probability (HTWP)
	list8 = [0,1,2,3,4,5,6,7]
	HTWP = 0
	DP = 0
	ATWP = 0
	for j in range(0,8):
	    for i in list8:
	        if i>j:
	            temp_17 = PT.iloc[j][i]
	            HTWP = HTWP + temp_17
	        elif i==j:
	            temp_18 = PT.iloc[j][i]
	            DP = DP + temp_18
	        else:
	            temp_19 = PT.iloc[j][i]
	            ATWP = ATWP + temp_19
	print('Home Team Winning Probability: ', HTWP, '     i.e. ', HTWP*100, '%')
	print('Draw Probability: ', DP, '     i.e. ', DP*100, '%')
	print('Away Team Winning Probability: ', ATWP, '     i.e. ', ATWP*100, '%')


	#Home Team Betting Odds (HTBO)
	HTBO = 1/HTWP
	print('Home Team Betting Odds: ', HTBO)

	#Draw Betting Odds (DBO)
	DBO = 1/DP
	print('Draw Betting Odds: ', DBO)

	#Away Team Betting Odds (HTBO)
	ATBO = 1/ATWP
	print('Away Team Betting Odds: ', ATBO)

	#Finding Top 3 Predicted Scores and their Probability
	HG1 = 0
	AG1 = 0
	P1 = 0

	HG2 = 0
	AG2 = 0
	P2 = 0

	HG3 = 0
	AG3 = 0
	P3 = 0

	for i in range(0,8):
	    for j in range(0,8):
	        x = PT.iloc[i][j]
	        if x>P1:
	            P1 = x
	            AG1 = i
	            HG1 = j
	        elif (x>P2):
	            P2=x
	            AG2 = i
	            HG2 = j
	        elif (x>P3):
	            P3 = x
	            AG3 = i
	            HG3 = j
	        else:
	            continue
	            
	P1 = P1*100
	P2 = P2*100
	P3 = P3*100
	print('Score 1: ',HG1,'-',AG1,'      ','Probability:',P1,'%')
	print('Score 2: ',HG2,'-',AG2,'      ','Probability:',P2,'%')
	print('Score 3: ',HG3,'-',AG3,'      ','Probability:',P3,'%')

	#Predicted Score 1
	PS1 = [HG1, AG1, P1]

	#Predicted Score 2
	PS1 = [HG2, AG2, P2]

	#Predicted Score 1
	PS1 = [HG3, AG3, P3]

	predictions = {'Home Team Winning Probability': HTWP, 'Draw Probability': DP, 'Away Team Winning Probability': ATWP,
					'Predicted Score 1': PS1, 'Predicted Score 2': PS2, 'Predicted Score 3': PS3, 
					'Home Team Betting Odds: ': HTBO, 'Draw Betting Odds: ': DBO, 'Away Team Betting Odds: ': ATBO}

	return predictions