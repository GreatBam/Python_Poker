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

for i in range(len(rank_matrix)):
    for key in rank_matrix:
        print(key[i+1])
