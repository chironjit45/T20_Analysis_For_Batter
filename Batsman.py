import pandas as pd

df = pd.read_csv("World cup 24.csv")

print("\n Batting Performance in powerplay")
powerplay= df[df['ball'].between(0.1,6.0)]
powerplay_performance = powerplay.groupby('striker').agg(
    balls_faced_in_powerplay = ('ball','size'),
    runs_scored_in_powerplay = ('runs_off_bat','sum'),
    match_played = ('match_id','nunique')

)
powerplay_performance['strike_rate'] = (powerplay_performance['runs_scored_in_powerplay']/powerplay_performance['balls_faced_in_powerplay']) * 100
top_powerplay_performance = powerplay_performance[(powerplay_performance['strike_rate']>140) & (powerplay_performance['runs_scored_in_powerplay']>120)]
top_powerplay_performance=top_powerplay_performance.reset_index()
top_powerplay_performance.rename(columns={
    'striker':'Batsman','balls_faced_in_powerplay':'Bowl Played','runs_scored_in_powerplay':'Total Runs','strike_rate':'Strike Rate',
    'match_played':'Match Played'
},inplace=True)
top_powerplay_performance=top_powerplay_performance[['Batsman','Match Played','Strike Rate','Total Runs']]
print(top_powerplay_performance.head(10))

print("\n Batting performance in middle overs ")
middle_overs= df[df['ball'].between(6.0,16.0)]
middle_over_performance = middle_overs.groupby('striker').agg(
     balls_faced_in_middle_overs  = ('ball','size'),
    runs_scored_in_middle_overs  = ('runs_off_bat','sum')
)
middle_over_performance['strike_rate'] = (middle_over_performance['runs_scored_in_middle_overs']/middle_over_performance['balls_faced_in_middle_overs'])*100
middle_over_performance = middle_over_performance[(middle_over_performance['strike_rate']>150) & (middle_over_performance['runs_scored_in_middle_overs']>70) &
                                                  (middle_over_performance['runs_scored_in_middle_overs']>=99) & (middle_over_performance['balls_faced_in_middle_overs']>60)]
middle_over_performance.sort_values(by='strike_rate' ,ascending = False).reset_index()
middle_over_performance=middle_over_performance.reset_index()
middle_over_performance.rename(columns={
        'striker':'Batsman','balls_faced_in_middle_overs':'Bowl played','runs_scored_in_middle_overs':'Total Runs','strike_rate':'Strike Rate'
},inplace = True)

middle_over_performance=middle_over_performance[['Batsman','Bowl played','Strike Rate','Total Runs']]
print(middle_over_performance)

print("\n Batting Performance in death overs")
death_overs= df[df['ball'].between(16.0,20.0)]
death_overs_performance = death_overs.groupby('striker').agg(
      balls_faced_in_death_overs = ('ball','size'),
     runs_scored_in_death_overs = ('runs_off_bat','sum')
)
death_overs_performance['strike_rate'] = (death_overs_performance['runs_scored_in_death_overs']/death_overs_performance['balls_faced_in_death_overs'])*100
death_overs_performance = death_overs_performance[(death_overs_performance['strike_rate']>180)& (death_overs_performance['runs_scored_in_death_overs']>=60)]
death_overs_performance=death_overs_performance.reset_index()
death_overs_performance.rename(columns={
    'striker':'Batsman','balls_faced_in_death_overs':'Bowl played','runs_scored_in_death_overs':'Total Runs','strike_rate':'Strike Rate'
},inplace=True)
death_overs_performance= death_overs_performance[['Batsman','Bowl played','Strike Rate','Total Runs']]
print(death_overs_performance)

