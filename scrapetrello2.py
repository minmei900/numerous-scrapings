# import needed libraries 

import ast
import urllib2
import json
import sys

# initialize variables

prioprod = 0
hourprod = 0
oldcardname = []
oldlabel = []
prio = []
cardname = []
savcardname = []
label = []
desc = []
labstr = ""

# do trello web api call to get all cards on partechdev board

page = urllib2.urlopen("https://api.trello.com/1/boards/JrX2JYZd/cards?fields=name,labels,desc&key=ed9025399a1a34476bbeff665335f29d&token=a4d15b04d7e2290adac243c4b934acb6e9abcb80de0196dad9dd293628880d3a")

result = page.read()

jason = json.loads(result)

if sys.argv[1] == "debug3":
    print json.dumps(jason, sort_keys=True, indent=4, separators=(',', ': '))
    print jason
    print len(jason)
    print range(len(jason))

# read beginning of portfolio cycle data from files (done with dump parameter)

f = open('/home/chad/gasbuddy/loadtrellonum.dat','r')
f1 = open('/home/chad/gasbuddy/loadtrellocurnum.dat','r')
f2 = open('/home/chad/gasbuddy/loadtrellocard.dat','r')
f3 = open('/home/chad/gasbuddy/loadtrellolabel.dat','r')

oldnumproj = f.read()
numproj = int(f1.read())
oldcardname = f2.read()
oldlabel = f3.read()

if sys.argv[1] == "debug":
    print oldnumproj
    print oldcardname
    print oldlabel

# run main parsing routine to populate all current lists

for element in range(len(jason)):

    #print element

    ststr = jason[element]["name"]
    if "#" in ststr:
        sp1 = ststr.find(" ")
        prio.append(int(ststr[1:sp1]))
        savcardname.append(ststr[sp1+1:])
    else:
        prio.append(numproj)
        savcardname.append(ststr)

    cardname.append(ststr)

    destr = jason[element]["desc"]
    sistr = destr.find("Size: ")
    if sistr >= 0:
        destr = destr[sistr+6:sistr+7]
        if destr == "S":
            desc.append(20)
        elif destr == "M":
            desc.append(60)
        elif destr == "L":
            desc.append(180)
        elif destr == "X":
            desc.append(540)
    else:
        desc.append("##")

    #print len(jason[element]["labels"])
    gotlabel = 0
    for element2 in range(len(jason[element]["labels"])):
        labstr = jason[element]["labels"][element2]["name"]
        if labstr[0] == "1":
            label.append(0)
            gotlabel=1
        elif labstr[0] == "2":
            label.append(25)
            gotlabel=1
        elif labstr[0] == "5":
            label.append(50)
            gotlabel=1
        elif labstr[0] == "7":
            label.append(75)
            gotlabel=1
        elif labstr[0] == "D":
            label.append(100)
            gotlabel=1
        else:
            if element2 == len(jason[element]["labels"])-1:
                if gotlabel == 0:
                    label.append(0)
    if labstr == "":
        #print "null"
        label.append(0)
    labstr = ""
        
# Strip first 8 instruction cards

prio = prio[8:]
cardname = cardname[8:]
savcardname = savcardname[8:]
desc = desc[8:]
label = label[8:]

# change to lists

oldcardname = ast.literal_eval(oldcardname)
oldlabel = ast.literal_eval(oldlabel)

# calculate metrics from new and old data

for element in range(len(prio)):
    if cardname[element][:6] == "Link t" and element == len(prio):
        break
    if sys.argv[1] != "debug2" and sys.argv[1] != "dump":
        revprio = 100*(numproj-int(prio[element]))/numproj 
        #print revprio

        #print 'savcardname: ' + savcardname[element]

        #print oldcardname
        for i, item in enumerate(oldcardname):
            #print i
            #print item
            if savcardname[element] in item:
                #print 'found'
                oldcardnameindex = i

        #print 'oldcardname index: ' + str(oldcardnameindex)

        #print oldlabel
        for i, item in enumerate(oldlabel):
            if i == oldcardnameindex:
                oldlabelnum = item

        #print 'oldlabelnum: ' + str(oldlabelnum)

        if oldlabelnum != '':
            rightlabel = int(label[element]) - int(oldlabelnum)
        else:
            rightlabel = int(label[element])
        #print 'rightlabel: ' + str(rightlabel)

        hourprod += rightlabel*int(desc[element])/100
        prioprod += revprio*rightlabel*int(desc[element])/10000

if sys.argv[1] == "debug2":
    print prio
    print cardname
    print savcardname
    print label
    print desc
    print len(prio)
    print len(cardname)
    print len(savcardname)
    print len(label)
    print len(desc)

# return argument-based results

if sys.argv[1] == "hours":
    print hourprod
if sys.argv[1] == "prio":
    print prioprod
if sys.argv[1] == "dump":
    g = open('/home/chad/gasbuddy/loadtrellonum.dat','w')
    g2 = open('/home/chad/gasbuddy/loadtrellocard.dat','w')
    g3 = open('/home/chad/gasbuddy/loadtrellolabel.dat','w')
    json.dump(len(prio),g)
    json.dump(savcardname,g2)
    json.dump(label,g3)

