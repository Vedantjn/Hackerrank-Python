# for _ in range(int(raw_input())):
# n= int(input())
# res=[]
# grade=[]

# for i in range(n):
#     name=input()
#     mark=float(input())
#     res.append([name,mark])
#     grade.append([mark])#calculating 2nd lowest
#     # print(res)
#     # print(grade)
#     grade=sorted(set(grade))#sorted unique
#     # print(grade)
#     m=grade[1]
#     # print(m)

#     name=[]
#     for val in res:
#         if m==val[1]:
#             name.append(val[0])
#     # print(name)#unsorted
#     name.sort()
#     # print(name)#sorted
#     for nm in name:
#         print(nm)
# ==========================================================================
# l = []
# second_lowest_names = []
# scores = set()

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name, score])
#     scores.add(score)

# second_lowest = sorted(scores)[1]

# for name, score in l:
#     if score == second_lowest:
#         second_lowest_names.append(name)

# for name in sorted(second_lowest_names):
#     print(name, end='\n')
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # for _ in range(int(input())):
    no_of_students = int(input())
    records = []
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])
records = dict(records)
scores = sorted(set(records.values()))
second_lowest_score = scores[1]
second_lowest_students = [name for name,
                          score in records if score == second_lowest_score]
second_lowest_students.sort()
for name in second_lowest_students:
    print(name)
