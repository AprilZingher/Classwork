
def setprogram(self):
    q = input("Type a new song or type 0 to finish.")
    if q != "0":
        self.program.append(q)
        setprogram(self)


concerts = []
people = []
flipdict = {
    "1": concerts,
    "0": people
}


class TicketOffice:
    def __init__(self, price: int, maxseats: int):
        self.price = price
        self.remaining = maxseats

    def editprice(self, newprice):
        self.price = newprice

    def getprice(self):
        return self.price

    def getremaining(self):
        return self.remaining

    def editremaining(self, a):
        self.remaining += a


class Person:
    def __init__(self, name: str, myconcerts: list):
        self.name = name
        self.concerts = myconcerts
        self.oldconcerts = []

    def getname(self):
        return self.name

    def getconcerts(self):
        return self.concerts

    def editname(self, astr):
        self.name = astr

    def addconcerts(self, anint: int):
        if concerts[anint].getremaining() != 0:
            self.concerts.append(anint)
            concerts[anint].editremaining(-1)
        else:
            print("There are no more tickets available.")

    def deleteconcerts(self, posi):
        q = self.concerts[posi]
        self.concerts.pop(posi)
        for x in people:
            if x == self:
                p = concerts[q].getattendees()
                for y in p:
                    if p[y] == x:
                        concerts[q].deleteattendees(y)
                        break
                break

    def passconcert(self, posi):
        a = self.concerts[posi]
        self.deleteconcerts(posi)
        self.oldconcerts.append(a)

    def getoldconcerts(self):
        return self.oldconcerts


class Concert:
    def __init__(self, name: str, date: str, location: str, price: int, maxseats: int):
        self.program = []
        self.name = name
        setprogram(self)
        self.date = date
        self.place = location
        self.attendees = []
        self.office = TicketOffice(price, maxseats)
        self.old = False

    def getname(self):
        return self.name

    def isold(self):
        return self.old

    def getdate(self):
        return self.date

    def getplace(self):
        return self.place

    def getprogram(self):
        return self.program

    def editname(self, astr):
        self.name = astr

    def editdate(self, astr):
        self.date = astr

    def editplace(self, astr):
        self.place = astr

    def addprogram(self, astr):
        self.program.append(astr)

    def getattendees(self):
        return self.attendees

    def addattendee(self, anint: int):
        self.attendees.append(anint)

    def deleteattendees(self, posi):
        self.attendees.pop(posi)

    def getprice(self):
        return self.office.getprice()

    def editprice(self, newprice):
        self.office.editprice(newprice)

    def getremaining(self):
        return self.office.getremaining()

    def editremaining(self, a):
        self.office.editremaining(a)

    def deleteprogram(self, posi):
        self.program.pop(posi)

    def flipold(self):
        self.old = not self.old
        p = self.getattendees()
        d = concerts
        r = -1
        for y in d:
            if d[y].getname() == self.getname():
                r = y
                break
        if r != -1:
            for x in p:
                people[p[x]].passconcert(r)


def createconcert():
    p = input("What's the name of your concert?")
    q = input("What's the price of one ticket? Type an integer.")
    r = input("How many tickets are available?")
    try:
        int(q)
        int(r)
    except ValueError:
        print("You didn't type an integer!")
        createconcert()
    else:
        newconcert = Concert(p, input("When is the concert?"),
                             input("Where is the concert?"), abs(int(q)), abs(int(r)))
        concerts.append(newconcert)
        if input('Do you want to create another concert? Type 0 to stop or anything else to continue.') != '0':
            createconcert()
        else:
            return


def findconcerts(tofind, b):
    for z in range(len(b)):
        if b[z] == tofind:
            return z
    return -1


def listconcerts(b):
    totallist = ""
    if len(b) > 0:
        for f in range(len(b)):
            totallist += (b[f].getname() + " ")
    else:
        totallist = "There are no items to list."
    return totallist


def concertselect(b):
    a = input("Type 1 to find a concert's info, type 0 to find a person's info.")
    if a == "1" or a == "0":
        if len(flipdict[a]) > 0:
            q = input('If you want to find an item, choose the name of that item. The items are:' +
                      listconcerts(flipdict[a]))
            if q != -1:
                p = findconcerts(q, flipdict[a])
            else:
                print("The given item isn't in the set.")
                return
        else:
            print("There are no elements in the given set.")
            return
    else:
        print("You didn't choose 1 or 0!")
        return
    if b == 0:
        actuallyprint(p, a)
    elif b == 1:
        actuallyedit(p, a)


def actuallyedit(posi, tstring):
    if tstring == "1":
        if not concerts[posi].isold():
            q = input("What do you want to edit? Type 1 for name, 2 for date, 3 for the program, 4 for the tickets "
                      "remaining, or 5 to set the concert as old.")
            if q == "1":
                concerts[posi].editname(input("What's the new name?"))
            elif q == "2":
                concerts[posi].editdate(input("What's the new date?"))
            elif q == "3":
                q2 = input("Would you like to delete a song (press 0) or add one (press 1)?")
                if q2 == "0":
                    z = concerts[posi].getprogram()
                    for y in range(len(z)):
                        print("Type " + str(y) + " to delete " + z[y])
                    p = input("Which will you delete? Type the corresponding number")
                    try:
                        int(p)
                    except ValueError:
                        print("You didn't type an integer!")
                        actuallyedit(posi, tstring)
                    else:
                        concerts[posi].deleteprogram(int(p) - 1)
                elif q2 == "1":
                    concerts[posi].addprogram(input("What's the name of the song you'd like to add?"))
                else:
                    print("You didn't type 0 or 1!")
                    actuallyedit(posi, tstring)
            elif q == "4":
                v = input("Type the amount of seats you'd like to add. If you'd like to remove tickets, write a "
                          "negative integer.")
                try:
                    int(v)
                except ValueError:
                    print("You didn't type an integer!")
                    actuallyedit(posi, tstring)
                else:
                    concerts[posi].editremaining(int(v))
            elif q == "5":
                caution = input("Are you CERTAIN you want to set this concert as passed? Once you do so, it can't be "
                                "edited. Type 0 if you're sure or anything else to exit the editing.")
                if caution == "0":
                    concerts[posi].flipold()
            else:
                print("You didn't type one of the given integers!")
                actuallyedit(posi, tstring)
    elif tstring == "0":
        q = input("What do you want to edit? Type 1 for name, 2 to delete concerts, or 3 to add a concert.")
        if q == "1":
            people[posi].editname(input("What's the new name you're choosing?"))
        elif q == "2":
            z = people[posi].getconcerts()
            for y in range(len(z)):
                print("Type " + str(y) + " to delete " + z[y])
            p = input("Which will you delete? Type the corresponding number")
            try:
                people[posi].getconcerts()[int(p)]
            except ValueError or IndexError:
                print("You didn't type one of the correct integers!")
                actuallyedit(posi, tstring)
            else:
                people[posi].deleteconcerts(int(p))
        elif q == "3":
            for y in range(len(concerts)):
                print("Type " + str(y) + " to add " + concerts[y].getname())
            p = input("Which will you add?")
            try:
                newq = int(p)
            except ValueError:
                print("You didn't type an integer!")
                actuallyedit(posi, tstring)
            else:
                if newq < 0 or newq > len(concerts):
                    print("That wasn't within the bounds!")
                    actuallyedit(posi, tstring)
                else:
                    people[posi].addconcerts(input(newq))
        else:
            print("You didn't type 1, 2, or 3!")
            actuallyedit(posi, tstring)


def convertlist(alist, tstring):
    printstring = []
    if tstring == "0":
        for x in alist:
            printstring.append(concerts[x].getname())
    if tstring == "1":
        for x in alist:
            printstring.append(people[x].getname())
    return printstring


def actuallyprint(posi, tstring):
    if tstring == "1":
        leng = len(concerts[posi].getattendees())
        q = (leng * concerts[posi].getprice())
        print(concerts[posi].getname() + " on " + concerts[posi].getdate() + " at " + concerts[posi].getplace() + ". Th"
              + "e program is:" + ", ".join(concerts[posi].getprogram()) +
              " The attendees are " + ", ".join(convertlist(concerts[posi].getattendees(), "1")) +
              ". The price is " + str(concerts[posi].getprice()) + ", and the total revenue is " + str(q) + "There are "
              + str(concerts[posi].getremaining()) + "seats remaining."
              )
    elif tstring == "0":
        print(people[posi].getname() + " is attending " + ', '.join(convertlist(people[posi].getconcerts(), "0")) + ". "
              "This person previously attended:" + ', '.join(convertlist(people[posi].getoldconcerts(), "0")))


def createperson():
    name1 = input("What's the next person's name?")
    if len(people) != 0:
        if findconcerts(name1, people) == -1:
            newperson = Person(name1, [])
            people.append(newperson)
        else:
            "This name already exists! Pick another name."
    else:
        newperson = Person(name1, [])
        people.append(newperson)


# def addnewconcerts(concertlist, concertsleft, personname):
#     currentlist = concertlist
#     currentleft = concertsleft
#     if len(currentlist) != 0 and len(concertsleft) != 0:
#         if input("Type 0 to stop adding concerts or press any key to continue") == "0":
#             return currentlist
#     if len(currentleft) != 0:
#         for y in range(len(concertsleft)):
#             print("Type " + str(y) + " to add " + concertsleft[y].getname())
#         p = input("Which will you add? Type the corresponding number")
#         try:
#             currentleft[int(p)]
#         except ValueError or IndexError:
#             print("You didn't type one of the correct integers!")
#             currentlist = addnewconcerts(concertlist, concertsleft, personname)
#             return currentlist
#         else:
#
#             a = findconcerts(currentleft[int(p)].getname(), concerts)
#             currentleft.pop(int(p))
#             if a != -1:
#                 concerts[a].addattendees(len(people))
#                 currentlist.append(concerts[a])
#             currentlist = addnewconcerts(currentlist, currentleft, personname)
#             return currentlist
#     else:
#         print("There are no more concerts to add!")
#         return currentlist


def mainfunc():
    if len(people) > 0 and len(concerts) > 0:
        q = (input("Type 'Person' to add a person, type 'Concert' to add a concert, type 'Print' to print a person's "
                   "name or concert name, or type 'Edit' to edit existing data."))
        if q == 'Person':
            createperson()
        elif q == 'Concert':
            createconcert()
        elif q == 'Print':
            concertselect(0)
        elif q == 'Edit':
            concertselect(1)
    elif len(concerts) == 0:
        createconcert()
    elif len(people) == 0:
        createperson()
    if input("Type 0 to end the program, or type anything else to continue.") != "0":
        mainfunc()


mainfunc()
