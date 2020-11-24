l = open('lessons.txt','r')
q = open('quality.txt','r')
p = open('participants.txt','r')
u = open('users.txt','r')
ans = open('ans.txt', 'w')
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
teach = [] # - все учителя
for k in range(len(users)):
    if users[k][1] == 'tutor':
        teach.append(users[k])
a = [] #Только уроки физики
for k in range(len(les)):
    if str(les[k][2]) == 'phys':
        a.append(les[k])
for k in range(len(les)):
    les[k][3] = les[k][3].split()
date = []
for k in range(len(a)):
    date.append(a[k][3][0])
date = unique(date)
date.sort()
d = [[] for k in range(10)] # массив с уроками за каждый день
for k in range(len(date)):
    for i in range(len(a)):
        if a[i][3][0] == date[k]:
            d[k].append(a[i])
event = [[] for k in range(len(d))] 
for x in range(len(event)):
    for k in range(len(d[x])):
        for i in range(len(part)):
            if d[x][k][1] == part[i][0]:
                event[x].append(part[i][1]) # - ID всех пользователей, которые были в этот день       
                event[x] = unique(event[x])
parttutor = [[] for k in range((len(d)))] 
for x in range(len(event)):
    for k in range(len(event[x])):
        for i in range(len(teach)):
            if event[x][k] == teach[i][0]: #Если ID человека совпадает с ID учителя, то он учитель)))
                parttutor[x].append(event[x][k])
                parttutor[x] = unique(parttutor[x])  #ID Учителей, которые преподавали в этот день (11 янв. например)
lesday = [[] for k in range(10)] #- тут будут номера события,на которых были учителя
for x in range(len(lesday)):  
    for k in range(len(parttutor[x])):
        for i in range(len(part)):
            if part[i][1] == parttutor[x][k]: #Если ID учителя, который преподавал в этот день равен другому ID, значит вытягиваем номер события
                lesday[x].append(part[i]) #[[event],[tutorID (11.01.2020)]]
lessons = d #[11.01.2020[LesID,event,subject,[date]],12.01.2020[]...]]
techtutor = [[] for k in range((len(d)))] 
for x in range(len(lesday)):
    for k in range(len(lesday[x])):
        for i in range(len(lessons[x])):
            if lesday[x][k][0] == lessons[x][i][1]: #сравниваем event
                for g in range(len(qua)):
                    if lessons[x][i][0] == qua[g][0]:
                        techtutor[x].append(lesday[x][k][1]) #учитель
                        techtutor[x].append(qua[g][1]) #оценка
techtutorohnespases = [[] for k in range((len(d)))]
for x in range(len(techtutor)):
    for k in range(1,len(techtutor[x]),2):
        if techtutor[x][k] != '':
            techtutorohnespases[x].append(techtutor[x][k-1])
            techtutorohnespases[x].append(techtutor[x][k]) #не учитываем уроки без оценок
for x in range(len(techtutorohnespases)):    
    ans.write(str(x+11)+ '\n')
    for k in range(0,len(techtutorohnespases[x]),2):
        ans.write(techtutorohnespases[x][k] + '|'+ techtutorohnespases[x][k+1] + '\n')   #Дальше в эксель (для наглядности)
print('done')      
'''
for k in range(len(les)):
    if les[k][3][1][0] == '2' and les[k][3][1][1] >= '1':
        print(les[k][3]) # ['2020-01-16', '21:34:17.949531'] - только в этом случае из-за часового пояса изменится дата 
'''
l.close
q.close
p.close
u.close
