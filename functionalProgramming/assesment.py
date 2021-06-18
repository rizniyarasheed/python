#print highest salaried employee
# print employee names whose exp >10 years

isl_2019 = [
    {"team":"mumbaicity","match_played":16,"won":10,"drawn":4,"loss":2,"goal_for":25,"goal_acquired":11,"goal_differ":14,"points":34},
    {"team":"ATK","match_played":15,"won":9,"drawn":3,"loss":3,"goal_for":20,"goal_acquired":10,"goal_differ":10,"points":30},
    {"team":"goa","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":24,"goal_acquired":19,"goal_differ":5,"points":23},
    {"team":"hyderabad","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":20,"goal_acquired":16,"goal_differ":4,"points":23},
    {"team":"northeast","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":21,"goal_acquired":20,"goal_differ":1,"points":23},
    {"team":"bengaluru","match_played":16,"won":4,"drawn":7,"loss":5,"goal_for":19,"goal_acquired":19,"goal_differ":0,"points":19},
    {"team":"jamshedpur","match_played":16,"won":4,"drawn":6,"loss":6,"goal_for":15,"goal_acquired":19,"goal_differ":-4,"points":18},
    {"team":"chennaiyin","match_played":16,"won":3,"drawn":8,"loss":5,"goal_for":11,"goal_acq":12,"goal_differ":6,"points":20}
]


#higest point team
from functools import reduce
point_high=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],isl_2019))),isl_2019))
print(point_high)


#lowest point team
from functools import reduce
point_low=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["points"],isl_2019 ))),isl_2019))
print(point_low)


#higest gf