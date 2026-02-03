#
#
# lines = [line.strip() for line in open("text/basketball data.txt")]
# games = [line.split(",") for line in lines]
# print(max([abs(int(g[2]) - int(g[4])) for g in games]))
#
#
# #same code with the one at the top
# with open("text/basketball data.txt") as f:
#     games = [line.strip().split(',') for line in f]
#
# print(max(abs(int(g[2]) - int(g[4])) for g in games))

# #same code with the one at the top, just explains it better
# lines = [line.strip() for line in open("text/basketball data.txt")]
# games = [line.split(",") for line in lines]
#
# biggest_diff = 0
# for g in games:
#     diff = abs(int(g[2]) - int(g[4]))
#     if diff>biggest_diff:
#         biggest_diff = diff
#         game_info = g
# print(game_info)

