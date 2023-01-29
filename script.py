print(0.1+0.1*5-0.3*4)
print((3.14+0.3)/2+0.15)
print(-13-7)
print(3 > 10)
# False

print(3 < 10)
# True

print(3 == 10) # равны ли объекты?
# False
print(1.57*3/1.5==3.14)
print('PY'in"Python")

s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 139953609727144, foo

s2 = "bar"
print(id(s2), s2) #проверяем идентификатор
# 139953609727088, bar

s1 = s1+s2
print(id(s1), s1) #проверяем идентификатор
# 139953459591296, foobar

s = "Hello!"

print(s[0])
# H

print(s[4])
# o




