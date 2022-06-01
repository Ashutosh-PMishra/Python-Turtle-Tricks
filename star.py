import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col = ['violet','yellow','purple','green','red','white']
c = 0
#simplified Learner 
for i in range(100):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c == 5:
        c = 0
    else:
        c += 1
#lets see magic of python----->>>►