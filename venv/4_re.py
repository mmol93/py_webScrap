import re

# .: 하나의 문자를 의미
p = re.compile("ca.e")  #> care, cafe, case 등등

# ^ : 문자열의 시작을 의미
# $ : 문자열의 끝

def print_match(m):
    if m:
        print("m.group(): ", m.group())
        print("m.string: ", m.string)
        print("m.start(): ", m.start())
        print("m.end: ", m.end())
        print("m.span(): ", m.span())
    else:
        print("매칭되지 않음")

lst = p.findall("good care")
print(lst)

lst = p.findall("good care careless")
print(lst)