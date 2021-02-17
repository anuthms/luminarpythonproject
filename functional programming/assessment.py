list_2019=[
    {"team":"mumbaicity","match_played":16,"won":10,"drawn":4,"loss":2,"goal_for":25,"goal_aquied":11,"goal_diff":14,"points":33},
    {"team":"ATK","match_played":15,"won":9,"drawn":3,"loss":3,"goal_for":20,"goal_aquied":18,"goal_diff":18,"points":30},
    {"team":"goa","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":24,"goal_aquied":19,"goal_diff":5,"points":23},
    {"team":"hyderabad","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":20,"goal_aquied":16,"goal_diff":4,"points":23},
    {"team":"northeast","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":21,"goal_aquied":20,"goal_diff":1,"points":23},
    {"team":"bengaluru","match_played":16,"won":4,"drawn":7,"loss":5,"goal_for":19,"goal_aquied":19,"goal_diff":8,"points":19},
    {"team":"janshedpur","match_played":16,"won":4,"drawn":6,"loss":6,"goal_for":15,"goal_aquied":19,"goal_diff":-4,"points":18},
]

#highest point

from functools import reduce
point_high=list(filter(lambda p1,p2: p1 if p1>p2 else p2,list(filter(lambda team:team["points"]**reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],list_2019))),list_2019)))

print(point_high)
