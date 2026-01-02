n, m = map(int, input().split())
teams = {}
member_to_team = {}

for _ in range(n):
    team_name = input().strip()
    members = int(input())
    teams[team_name] = []

    for _ in range(members):
        name = input().strip()
        teams[team_name].append(name)
        member_to_team[name] = team_name

    teams[team_name].sort()

for _ in range(m):
    q_name = input().strip()
    q_num = int(input())

    if q_num == 0:
        for member in teams[q_name]:
            print(member)
    else:
        print(member_to_team[q_name])
