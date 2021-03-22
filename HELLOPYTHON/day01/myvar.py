a = 7  
b = 7.3 
c = True 
d = "안녕" 
e = '7' 


print(a+1)
print(b)
print(c)
print(d + str(a))
print(int(e)+1)

#
print(1.04**30)


#Python 문자열 위치
#숫자로 표현. 
f = "Life is too short, You need Python"

print("첫번재 문자 f[0] : " + f[0])
print("마지막 문자 f[-1] : " + f[-1])

#문자열 슬라이싱
g = f[0]+f[1]+f[2]+f[3]
print(g) # Life
print(f[0:4]) # Life
# 시작점 부터 출력을 원하는 지점까지의 숫자를 적어주면 그 사이의 문자열을  출력해준다.
# 슬라이싱 기법은 끝 반호를 포함하지 않기 때문에 4로 입력
# 0 <= f < 4

print(f[5:]) # is too short, You need Python
# 끝 번호를 지정해주지않으면 시작번호부터 문자열의 끝까지 뽑아냄

print(f[:17]) # Life is too short
# 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.

print(f[:]) # Life is too short, You need Python
# 문자열 다 출력됨
print(f[19:-7]) # You need
# f 19 부터 -8 위치의 문자열까지 출력됨

h = "Pithon"
print(h[:1]+'y'+h[2:]) # 슬라이싱을 이용해서 i 를 y 로변경


# 문자열 포매팅
a = "I eat %d apples." % 3
print(a) #I eat 3 apples.

a = "I eat %s apples." % "five"
print(a) #I eat five apples.

# 문자열 은 %s 숫자는 %d 로 포매팅 함.


#2개이상의 값 넣기
number = 10
day = "three"
a= "I ate %d apples. so I was sick for %s days" %(number, day)
print(a)

# 포매팅 연산자에 % 써야하는 경우 %% 두번 써준다.
a = "Error is %d%%." %98
print(a)

# 포맷 코드와 숫자 함께 사용
a = "%10s" % "hi"
print(a) # hi 오른쪽 정렬됨. 총 문자열 10개 중 마지막 2개에 hi 들어감.역으로도 동일하게 적용됨

a = "%-10sjane" % 'hi'
print(a) # hi 왼쪽 정렬됨

# 소수점 표현
a = "%0.4f" % 3.42134234
print(a) # 3.4213 소수점 4번째 자리까지만 나타남

a = "%10.4f" % 3.42134234
print(a) # 전체 길이가 10개인 문자열 공강에 오른쪽으로 정렬됨.


### 리스트 관련 함수
#1.리스트 요소 추가(append)
a = [1,2,3]
a.append([5,6])
print(a) #[1, 2, 3, [5, 6]] / 리스트에 다시 리스트 추가

#2. 리스트 정렬(sort)
a=[1,4,2,3]
a.sort()
print(a) # [1, 2, 3, 4] 요소를 순서대로 정렬해준다.

#3. 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)  #['b', 'c', 'a']  현재 리스트를 그대로 거꾸로 뒤집는다.

#4. index 위치 반환
a = [1,2,3]
print(a.index(3))  # 2 / 3은 a 리스트의 세번재 요소(a[2])

#5. insert
a = [1,2,3]
a.insert(0, 4) #0번째 자리, 즉 첫번째 요소 위치에 값 4를 삽입  [4, 1, 2, 3]

# 6.remove
a = [1,2,3,1,2,3]
a.remove(3) # 리스트에서 첫번재로 나오는 3을 삭제
print(a)  # [1, 2, 1, 2, 3]

# 7. pop
a = [1,2,3]
print(a.pop())  # pop()은 마지막 값을 반환 해준다.
print(a) # a를 출력하면 pop()에서 나온 값을 제외하고 출력된다.









  

