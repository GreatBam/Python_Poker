import re

rank_matrix = [
    {"id":1, "rank":"2", "value": 0},
    {"id":2, "rank":"3", "value": 0},
    {"id":3, "rank":"4", "value": 0},
    {"id":4, "rank":"5", "value": 0},
    {"id":5, "rank":"6", "value": 0},
    {"id":6, "rank":"7", "value": 0},
    {"id":7, "rank":"8", "value": 0},
    {"id":8, "rank":"9", "value": 0},
    {"id":9, "rank":"10", "value": 0},
    {"id":10, "rank":"J", "value": 0},
    {"id":11, "rank":"Q", "value": 0},
    {"id":12, "rank":"K", "value": 0},
    {"id":13, "rank":"A", "value": 0}
]
rank_straight_matrix = {
    "2" : 0,
    "3" : 0,
    "4" : 1,
    "5" : 1,
    "6" : 1,
    "7" : 1,
    "8" : 1,
    "9" : 0,
    "10" : 0,
    "J" : 0,
    "Q" : 0,
    "K" : 0,
    "A" : 0
}

numbers = ""

for rank in rank_straight_matrix:
    numbers += str(rank_straight_matrix[rank])
    
print(numbers)

y = re.findall('11111',numbers)

print(y)

# print(len(rank_straight_matrix))
# print(rank_straight_matrix["2"])

# for i in rank_straight_matrix:
#     print(rank_straight_matrix[i])
