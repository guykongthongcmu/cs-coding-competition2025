bags, nQuestion = input().split()
arr = input().split()

intNQUESTION = int(nQuestion)

questions = [] * intNQUESTION
for i in range(intNQUESTION):
    questions.append(input().split())


for i in range(intNQUESTION):
    sum = 0
    if questions[i][0] == "I":
        arr[int(questions[i][1]) - 1] = int(arr[int(questions[i][1]) - 1]) + int(questions[i][2])
    elif questions[i][0] == "D":
        arr[int(questions[i][1]) - 1] = int(arr[int(questions[i][1]) - 1]) - int(questions[i][2])
    else:
        for j in range(int(questions[i][1]) - 1,int(questions[i][2])):
            sum += int(arr[j])
        print(sum)
