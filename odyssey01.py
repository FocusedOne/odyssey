from sys import exit

def mars():
    global time
    global drasin
    time = time - 1
    print time
    print "We have reached Mars orbit"
    if time <= 4:
        _drasin()
    elif time >= 4:
        print "nothing to see here"
        orders = raw_input("We can nav or scan: ")
        if "nav" in orders:
            navigation()
        elif "scan" in orders:
            scan()
        else:
            mars()
    else:
        mars()

def alpha():
    global time
    global drasin
    time = time - 1
    print time
    print "We have reached Alpha Centauri"
    if time >= 10:
        _drasin()
    elif time <= 9:
        print "nothing to see here"
        orders = raw_input("We can nav or scan: ")
        if "nav" in orders:
            navigation()
        elif "scan" in orders:
            scan()
        else:
            alpha()
    else:
        alpha()

def saturn():
    global time
    global drasin
    time = time - 1
    print time
    print "We have reached Saturn orbit"
    if time >= 8:
        _drasin()
    elif time <= 7:
        print "nothing to see here"
        orders = raw_input("We can nav or scan: ")
        if "nav" in orders:
            navigation()
        elif "scan" in orders:
            scan()
        else:
            saturn()
    else:
        saturn()

def start():
    global name
    print """Welcome, Captain %s
    The crew awaits your orders.""" % name

    orders = raw_input("nav or scan: ")
    if "nav" in orders:
        navigation()
    elif orders == "scan":
        print "Scanning sector"
        scan()
    elif "dead" in orders:
        dead("you killed it")
    else:
        start()
def scan():
    global drasin
    global time
    if time > 8:
        print "Captain, sensors show %r ships outside the solar system" % drasin
        navigation()
    elif time >= 6:
        print "Captain, sensors show %r ships near mars!" % drasin
        navigation()
    elif time >= 3:
        print "Captain, sensors show %r ships near Earth!" % drasin
        navigation()
    else:
        print "Something may be wrong with the sensors."
        navigation()

def navigation():
    global time
    global health
    print time
    print """Sir, from our current position we can travel to Mars, Saturn, Alpha Centauri or we could make a traning run around the moon"""
    
    choice = raw_input("Mars, Moon, Saturn, or Alpha Centauri: ")

    if choice == "Mars":
        mars()
    elif choice == "Moon":
        moon()
    elif choice == "Saturn":
        saturn()
    elif choice == "Alpha Centauri":
        alpha()
    elif choice == "scan":
        scan()
    else:
        print "I don't understand"
        navigation()

def moon():
    global time
    time = time - 1
    global health
    health = health + 1
    print """We have reached Lunar orbit."""
    print "%r time remaining" % time
    if time <= 3:
        _drasin()

    orders = raw_input("Your orders, captain: ")
    
    if "Destruct" in orders:
        dead("Your ship asplode.  Good job")
    elif "nav" in orders:
        navigation()
    elif "scan" in orders:
        scan()
    else:
        print "I don't understand"
        moon()

def _drasin():
    global time
    global health
    global hvms
    global angels
    global drasin
    print "We have %r time and %r health remaining" % (time, health)
    if drasin == 0:
        victory()
    if health == 0:
        dead("The Drasin have destroyed you, earth's only defender.")
    elif drasin > 0:
        print "Captain, %r Drasin in firing range!" % drasin
        orders = raw_input("We can fire HVMs, launch the archangels or run away: ")
        if orders == "hvms":
            hvms = hvms - 1
            drasin = drasin - 1
            health = health - 1
            time = time - 1
            print "HVM away...HIT, Strike one Drasin destroyer!"
            print "Laser strike, habitat ring.  We're venting atmosphere! %r" % health
            if drasin > 0:
                _drasin()
            elif drasin == 0:
                victory()
            else:
                _drasin()
        elif orders == "archangels":
            angels = angels - 1
            drasin = drasin - 1
            health = health - 1
            time = time - 1
            print "Go angels!  Scratch one Drasin destroyer!"
            print "We have %r time remaining" % time
            if drasin > 0:
                print "Laser strike, forward section! %r" % health
                _drasin()
        elif orders == "ramming speed":
            drasin = drasin - 1
            health = 1
            print "Odyssey sits dead in space"
            _drasin()
        elif orders == "destruct":
            drasin = drasin - 2
            health = 0
            print "Odyssey self destructs, taking two Drasin with her."
            print "Game over.  Good job!"
            dead('Self destructed')
        elif orders == "nav":
            health = health - 2
            print "Laser strike, engineering. %r health!" % health
            navigation()
        else:
            health = health - 1
            time = time - 1
            print "Laser strike, Habitat ring.  %r health!" % health
            _drasin()
    else:
        health = health - 1
        time = time - 1
        print "Captain, what do we do? Laser strike, hangar bay! %r health remaining" % health
        _drasin()
def victory():
    global health
    global name
    if health > 0:
        print "Congratulations, captain %r!  You've saved the world. Good job!" % name
        exit()
    elif health == 0:
        print "Well, you killed them all, but no cheeseburger for you."
        exit()
    else:
        print "well you won, but I'm not sure how."
        exit()

def dead(why):
    print why, "try harder next time!"
    if drasin == 0 and health > 10:
        print "Congratulations, Captain! You've saved the world and lived to enjoy a celebratory double cheeseburger!"
    elif drasin >= 1:
        print "Epic failure!"
    elif time == 0:
        print "Epic failure!"
    elif drasin == 0 and health < 1:
        print "You'll have no celebratory cheeseburger today, but at least you've saved the world!"
    else:
        print "Well, that was odd."
    exit(0)

time = 14
drasin = 5
health = 8
hvms = 3
angels = 1
print "Welcome to the Odyssey. Please input your name for command transfer"
name = raw_input ("> ")

start()
