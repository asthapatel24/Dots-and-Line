import pygame,sys,random
global turn,boxes_done

pygame.init()
pygame.display.set_caption('Dots and Boxes')
screen=pygame.display.set_mode((640, 400))

dot=pygame.transform.scale(pygame.image.load('Dot-icon.png'), (23, 23))

blackh,blueh,greenh=pygame.Surface((75,3)),pygame.Surface((75,3)),pygame.Surface((75,3))
blackv,bluev,greenv=pygame.Surface((3,75)),pygame.Surface((3,75)),pygame.Surface((3,75))

blackh.fill((0,0,0));blueh.fill((0,0,255));greenh.fill((0,255,0));blackv.fill((0,0,0));bluev.fill((0,0,255));greenv.fill((0,255,0))

lines_to_disp=[]
done=[]
lines=[]
rects2,rects3=[],[]

boxes=[(0,7,8,15),(1,8,9,16),(2,9,10,17),(3,10,11,18),(4,11,12,19),(5,12,13,20),(6,13,14,21),(15,22,23,30),(16,23,24,31),(17,24,25,32),(18,25,26,33),(19,26,27,34),(20,27,28,35),(21,28,29,36),(30,37,38,45),(31,38,39,46),(32,39,40,47),(33,40,41,48),(34,41,42,49),(35,42,43,50),(36,43,44,51)]

boxes_filled=[0]*21
turn="user"
boxes_done=0

score={"user":0,"cpu":0}
square={"user":pygame.Surface((75,75)),"cpu":pygame.Surface((75,75)),"white":pygame.Surface((75,75))}
square["user"].fill((0,0,215));square["cpu"].fill((0,215,0));square["white"].fill((255,255,255))

rects4=[]
d=[]
for i in range(4):
	for j in range(24,31):
		lines.append([[j,i],0])
	if i!=3:
		for k in range(8,16):
			lines.append([[k,i],0])

def check_if_filled():
	global turn,boxes_done
	lis2=[]
	for box in boxes:
		if boxes_filled[boxes.index(box)]!=True:
			sides_filled=0
			for i in range(4):
				if lines[box[i]][1]==1:
					sides_filled+=1
			if sides_filled==4:
				lis2.append(True)
				boxes_done+=1
			else:
				lis2.append(0)
		else:	
			lis2.append(True)
	inc=lis2.count(True)-boxes_filled.count(True)
	if lis2!=boxes_filled or boxes_filled.count(0)==0:

		if turn=="cpu":
			turn="user"
		else:
			turn="cpu"
		for x in range(len(boxes_filled)):
			if boxes_filled[x]!=lis2[x]:
				boxes_filled[x]=lis2[x]
				rects4[x][1]=square[turn]
		return (True,inc)
	return False
	
def text_on_screen(text,antial,color,size,x,y,rect=False):	# Function to actually display the text on screen
        basicFont = pygame.font.Font(None, size)	# The font to be used
        text=basicFont.render(text,antial,color)
        if not rect:
                textRect = text.get_rect()	# Create a new 'rectangle' object if there is not one provided
        else:
                textRect = rect
        textRect.left = x
        textRect.top = y
        screen.blit(text, textRect)

def three_sides():
	three=[]
	for box in boxes:
		sides_filled=0
		line_not_done=""
		for i in range(4):
			if lines[box[i]][1]==1:
				sides_filled+=1
			if lines[box[i]][1]==0:
				line_not_done=lines[box[i]]
		if sides_filled==3:
			three.append([box,line_not_done])
	return three

def cpu_move():
	global turn
	inf=False
	three=three_sides()
	if three==[]:
		line_not_done=[]
		for line in lines:
			if line[1]==0:
				line_not_done.append(line)
		chain=False
		while len(line_not_done):
			rect=None
			random.shuffle(line_not_done)
			line=line_not_done.pop(0)
			lines[lines.index(line)][1]=1
			if three_sides()==three:
				break
			lines[lines.index(line)][1]=0
			if len(line_not_done)==0:
				chain=True
				break
		if chain:
			for line in lines:
				if line[1]==0:
					line_not_done.append(line)
			chains=[]
			for l in line_not_done:
				lines[lines.index(l)][1]=1
				chains.append((l,three_sides()))
				lines[lines.index(l)][1]=0
			chains.sort(key=lambda x:len(x[1]))
			line=chains[0][0]
			lines[lines.index(line)][1]=1
	else:
		line=(random.choice(three))[1]
		lines[lines.index(line)][1]=1	
	done.append(line[0])
	for x in rects2+rects3:
		if x[1]==line[0]:
			rect=x[0]
	if line[0][0] in range(24,31):
		lines_to_disp.append([greenh,rect,"H"])
	else:
		lines_to_disp.append([greenv,rect,"V"])
	turn="user"

def again():
	global turn,boxes_done,boxes_filled,done
	turn="user"
	boxes_done=0
	boxes_filled=[0]*21
	done=[]
	score["user"]=0
	score["cpu"]=0

def main():
	global turn
	rects=[]
	for i in range(100,400,75):
			for j in range(50,600,75):
				rects.append(pygame.Rect(j,i,3,3))
	for x in rects[0:7]+rects[8:15]+rects[16:23]:
		rects4.append([pygame.Rect(x.left+10,x.top+13,75,75),square["white"]])
	for j in range(4):
		for i in [x-1 for x in range(len(rects)) if (x%8!=0)]:
			rects2.append((pygame.Rect(rects[i].left+10,rects[j].centerx+50,75,40),[i,j]))
	for j in range(3):
		for i in range(len(rects)-16):
			rects3.append((pygame.Rect(rects[i].left,rects[j].centerx+50,40,70),[i,j]))
	clock=pygame.time.Clock()
	hv=[False,False]
	a=[False,None,None]
	id_=[]
	user_wins=False
	while True:
		screen.fill((255,255,255))
		clock.tick(140)
		for x in rects4:
			screen.blit(x[1],x[0])
		if a[0]:
			if hv[0]:
				screen.blit(a[2],(a[1].left,a[1].top+10))
			else:
				screen.blit(a[2],(a[1].left+10,a[1].top+10))
		text_on_screen("Dots & Boxes",True,(220,20,255),60,200,5)
		text_on_screen("Your Score: %d       Computer's Score: %d" %(score["user"],score["cpu"]),True,(0,0,0),25,180,370)

		text_on_screen("- "*50,True,(0,0,0),30,0,50)
		for [y,z,b] in lines_to_disp:
			if b=="H":
				screen.blit(y,(z.left,z.top+10))
			if b=="V":
				screen.blit(y,(z.left+10,z.top+10))
		for rect in rects:
			screen.blit(dot,rect)
		d=check_if_filled()
		check_if_filled()
		if d and len(d)==2:
			score[turn]+=d[1]
		
		if boxes_done==20 and turn!="user":
			for x in rects4:
				if x[1]==square["white"]:
					rects4[rects4.index(x)][1]=square[turn]
			score["user"]-=1;score["cpu"]+=1
		if turn=="cpu":
			cpu_move()
		if score["user"]+score["cpu"]==21:
			x="You Won!"
			if score["cpu"]>score["user"]:
				x="CPU Won!"
			text_on_screen(x,True,(0,0,0),60,0,0)
		pygame.display.update()
		event=pygame.event.poll()
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.MOUSEMOTION:
			for x in rects2:
				if x[0].collidepoint(event.pos):
					a[0],a[1],a[2]=True,x[0],blackh
					hv[0],hv[1]=True,False
					id_=x[1]
			for x in rects3:
				if x[0].collidepoint(event.pos):
					a[0],a[1],a[2]=True,x[0],blackv
					hv[1],hv[0]=True,False
					id_=x[1]
		if event.type==pygame.MOUSEBUTTONUP:
			if a[0]:
				a[0]=False
				do=False
				for x in lines:
					if x[0]==id_ and x[1]==0:
						lines_to_disp.append([{blackh:blueh,blackv:bluev}[a[2]],a[1],{blackh:"H",blackv:"V"}[a[2]]])
						done.append(id_)
						for x in lines:
							if x[0]==id_:
								x[1]=1
						turn="cpu"
						break
main()
