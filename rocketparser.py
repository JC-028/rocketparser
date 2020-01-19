# parser for openrocket sims stored in CSV files
# (c) Yung-Ber software studios
import turtle, sys
print('press CTRL-C in the terminal to quit')
points=[]
apogee=0
loop=1
print('parsing...')
for line in open(sys.argv[1]):
	if loop == 1:
		sim=(line.replace('# ','')).replace(' (Up to date)','')
	loop+=1
	if '#' in line:
		points.append((line.replace('# ','')).replace('\n',''))
		continue
	X,Y=line.split(',')
	Y=float(Y)
	if Y > apogee:
		apogee=Y
del(loop)
plot=turtle.Turtle()
plot.hideturtle()
plot.penup()
plot.goto(-350,0)
plot.pendown()
x=-350
y=0
print('plotting...')
try:
	for line in open(sys.argv[1]):
		if '#' in line:
			continue
		X,y=line.split(',')
		y=float(y)
		plot.goto(x,y)
		x+=1
	while 1:
		pass
except KeyboardInterrupt:
	pass
print('\nPARSE COMPLETE:')
sim+='\napogee: '+str(apogee)+' meters\nevents:'
print('apogee: '+str(apogee*3.25)+'ft')
print('events:')
for point in points:
	print('|	'+point)
	sim+='\n|	'+point
print('CREATING LOG...')
data=open('rocket.log','w')
data.write(sim)
data.close()
