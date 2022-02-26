

# 내림차순으로 정렬한다
# list map으로  배열을 string으로 바꾼다
def solution(numbers):
    numbers = list(map(str, numbers))
    ["3", "0","5"]
    numbers.sort(key = lambda x: x *3, reverse= True)
    return str(int(''.join(numbers)))

    list(map(lambda x:sorted(reverse=True)('',join(x))), numbers)

   # map에 있는 Int 배열을  String list로 변환한다
   # num , sort() 를 사용하여 key조건에 맞게 배열
   #
   #  print(numbers)  => ['6', '10', '2']
   #
   #  numbers.sort(reverse= True) => ['9','5','34','30','3']
   #
   #  [999], [500], [343434],[303030], [333]  => 3글자가있으면 3글자만 비교한다
   #
   #  print(number)고고
   #
   #  return ''.join(numbers) 만 하면 0000이 출력 그래서 int변환되 string으로 다시


