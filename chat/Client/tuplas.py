import linsimpy
tse = linsimpy.TupleSpaceEnvironment()
# data = [user,nick,status,latitude,longitude,distancia]

def checkNick(nick):
    try:
        tse.rdp(("NICK", nick))
        return True
    except:
        return False

def createUser(data):
    user = data[0]
    nick = data[1]
    status = data[2]
    latitude = data[3]
    longitude = data[4]
    distancia = data[5]

    tse.out(("NICK",nick))
    tse.out(("USER", nick, [user, status, latitude, longitude, distancia]))
    
    createUsers(data)
    user = tse.rdp(("USER",nick,[user, status, latitude, longitude, distancia]))
    print(f"User created {user}")
    if(status == True):
        try:
            online = tse.inp(("ONLINE",object))
            tsOnline = list(online[1])
            tsOnline.append(nick)
            tse.out(("ONLINE",tuple(tsOnline)))
        except:
            tsOnline = [nick]
            tse.out(("ONLINE",tuple(tsOnline)))
    else:
        try:
            offline = tse.inp(("OFFLINE",object))
            tsOffline = list(offline[1])
            tsOffline.append(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))
        except:
            tsOffline = [nick]
            tse.out(("OFFLINE",tuple(tsOffline)))

def createUsers(data):
    listUsers = []
    try:
        x = tse.inp(("USERS",object))
        listUsers = list(x[1])
        listUsers.append(data)
        tse.out(("USERS", listUsers))
    except:
        listUsers = data 
        tse.out(("USERS", listUsers))

def readAllUsers():
    try:
        users = tse.rdp(("USERS",object))
        return users
    except:
        return('Users not found')


def readUser(nick):
    try:
        user = tse.rdp(("USER",nick, object))
        return user
    except:
        return("User not found")
def listOnline():
    try:
        online = tse.rdp(("ONLINE",object))    
        print(online)
        return list(online[1])
    except: 
        print(f"Tuple matching not found")
        
def listOffline():
    try:
        offline = tse.rdp(("OFFLINE",object))    
        print(offline)
        return list(offline[1])
    except: 
        print(f"Tuple matching not found")

def updateStatus(nick,status):
    tsOnline = []
    tsOffline = []
    user = tse.inp(("USER",nick,object))
    tsUser = list(user[2])
    tsUser[1] = status
    tse.out(("USER",nick,tsUser))
    
    if(status == True):
        try:
            offline   = tse.inp(("OFFLINE",object))
            tsOffline = list(offline[1])
            tsOffline.remove(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))

            online    = tse.inp(("ONLINE",object))
            tsOnline  = list(online[1])
            tsOnline.append(nick)
            tse.out(("ONLINE",tuple(tsOffline)))
        except:
            tsOnline = [nick]
            tse.out(("ONLINE",tuple(tsOnline)))
    else:
        try:
            online   = tse.inp(("ONLINE",object))
            tsOnline = list(online[1])
            tsOnline.remove(nick)
            tse.out(("ONLINE",tuple(tsOnline)))

            offline    = tse.inp(("OFFLINE",object))
            tsOffline  = list(offline[1])
            tsOffline.append(nick)
            tse.out(("OFFLINE",tuple(tsOffline)))
        except:
            tsOffline = [nick]
            tse.out(("OFFLINE",tuple(tsOnline)))

    dataUser = tse.rdp(("USER",nick,object))
    return dataUser     

def updateLatitude(nick,lat):
    user = tse.inp(("USER",nick,object))
    tsUser = list(user[2])
    tsUser[2] = lat
    tse.out(("USER",nick,tsUser))
    return(tse.rdp(("USER",nick,object)))
def updateLongitude(nick,lon):
    user = tse.inp(("USER",nick,object))
    tsUser = list(user[2])
    tsUser[3] = lon
    tse.out(("USER",nick,tsUser))
    return(tse.rdp(("USER",nick,object)))

def updateDistancia(nick,dis):
    user = tse.inp(("USER",nick,object))
    tsUser = list(user[2])
    print(tsUser[4])
    tsUser[4] = dis
    tse.out(("USER",nick,tsUser))
    return(tse.rdp(("USER",nick,object)))

