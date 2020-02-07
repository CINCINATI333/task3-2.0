l = open('lessons.txt','r')
q = open('quality.txt','r')
p = open('participants.txt','r')
u = open('users.txt','r')
les = l.read()
qua = q.read()
part = p.read()
users = u.read()
def unique(x):
    x = set(x)
    x = list(x)
    return x
def TheBestDataCleaner(x):
    x = x.split('\n ')
    for k in range(len(x)):
        x[k] = x[k].split('|')
        x[k][0] = x[k][0].replace(' ','')
        x[k][1] = x[k][1].replace(' ','')
    return x

def TheBestDataCleaner2(y):
    y = y.split('\n ')
    for k in range(len(y)):
        y[k] = y[k].split('|')
        y[k][0] = y[k][0].replace(' ','')
        y[k][1] = y[k][1].replace(' ','')
        y[k][2] = y[k][2].replace(' ','')
    return y
qua = TheBestDataCleaner(qua)
part = TheBestDataCleaner(part)
users = TheBestDataCleaner(users)
les = TheBestDataCleaner2(les)
print(les)
les = les.split('\n ')
teach = users # - все учителя
for k in range(len(users)):
    if users[k][1] == 'tutor':
        teach.remove(users[k])
print('teach','\n',teach)
print('users','\n', users)
a = [] #Только уроки физики
for k in range(len(les)):
    if str(les[k][2]) == 'phys':
        a.append(les[k])
for k in range(len(les)):
    les[k][3] = les[k][3].split()
    #print(les[k][3])
b = []
i = 0
date = []
for k in range(len(a)):
    date.append(a[k][3][0])
date = set(date)
date = list(date)
date.sort()
#print(date)
d = [[],[],[],[],[],[],[],[],[],[]] # массив с уроками за каждый день
for k in range(len(date)):
    for i in range(len(a)):
        if a[i][3][0] == date[k]:
            d[k].append(a[i])
#print(d[0])
event = []
#for j in range(len)
for k in range(len(d)):
    for i in range(len(part)):
        if d[0][k][1] == part[i][0]:
            event.append(part[i][1]) # - ID всех пользователей, которые были в этот день
event = set(event)
event = list(event)
print(event)
teaevent = []
for k in range(len(event)):
    for i in range(len(teach)):
        if event[k] == teach[i][0]: #Если ID человека совпадает с ID учителя, то он учитель)))
            teaevent.append(event[k])
            teaevent = unique(teaevent)  #ID Учителей, которые преподавали в этот день (11 янв. например)
#print('teaevent','\n',teaevent) 

#print(teach) # - Тут все чуваки, которые были на уроках 11 января
#print(part)
lesday = [] #- тут будут номера события,на которых были учителя
for k in range(len(teaevent)):
    for i in range(len(part)):
        if part[i][1] == teaevent[k]: #Если ID учителя, который преподавал в этот день равен другому ID, значит вытягиваем номер события
            lesday.append(part[i][0])
            #lesday = unique(lesday)
print(lesday)
numoflessons = []
for k in range(len(lesday)):
    for i in range(len(d)):
        if lesday[k] == d[0][i][1]:
            numoflessons.append(d[0][i][0])
print(numoflessons)





'''mbydate = []
for k in range(len(a)):
    for i in range(len(qua)):
        if a[k][0] == qua[i][0]:
            mbydate.append(qua[i])'''
#mbydate = set(mbydate)
#bydate = list(mbydate)
#print(mbydate)
#print(len(mbydate))

'''
print('-----------------------------') 
print(d[0])    #Все Уроки по физике 11 января
print('-----------------------------')       
print(d[0][0])
print('-----------------------------')

marks = []
for k in range(len(d)):
    for i in range(len(qua)):
        if d[k][0][0] == qua[i][0]:
'''
#print(int(qua[0][1])+int(qua[1][1])) - складываем оценки
#print(d[k])
    # print(a[k][3],'---',a[k][3][0][8],a[k][3][0][9],'---', a[k][0])


#for k in range(len(les)):
    #if les[k][3][1][0] == '2' and les[k][3][1][1] >= '1':
        #print(les[k][3]) # ['2020-01-16', '21:34:17.949531'] - только в этом случае из-за часового пояса изменится дата 

l.close
q.close
p.close
u.close
