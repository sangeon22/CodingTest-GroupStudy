def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for c in new_id:
        if c.isalpha() or c.isdigit() or c in "-_.":
            #  if c.isalnum() or c in "-_.":
            answer += c

    while '..' in answer:
        answer = answer.replace('..', '.')


    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        # if answer[-1:0] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'

    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)

    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print("hello")