def solution(new_id):
    answer = ''
    # 1 .대문자에 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자,빼기(-), 밑줄, 마침표 를 제외한 모든 문자를 제거ㅜ합니다.
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in "-_.":
            #  if c.isalnum() or c in "-_.":
            answer += c
    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 마침표(.) 가 처음이나 끝에 위치한다면 제거합니다.
    if answer and answer[0] == '.':  # answer 가 존재하는데 / exception
        answer = answer[1:]
    if answer and answer[-1] == '.':
        # if answer[-1:0] == '.':
        answer = answer[:-1]
    # 5. 빈 문자열이라면 new_id에 "a" 를 대입 합니다.
    if answer == '':
        answer = 'a'
    # 6. answer가 16자 이상이면 짜른다. 마치푬가 new_id에 끝에 위치한다면
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    # 7. 길이가 2자 이하일때  answer 마지막글자 붙여준다.
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print("hello")