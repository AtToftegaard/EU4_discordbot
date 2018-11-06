import os, sys, io, tkinter, re, pandas

def get_players(file):
    "Finds the list of all players and adds to dictionary"
    players = dict()
    pattern = re.compile(r'players_countries={\n')
    for line in file:
        if(re.match(pattern, line)):
            line = file.readline() #skip line we just matched with
            while not (re.match('}\n', line)):
                players[line.strip().replace('"', '')] = "null"
                line = file.readline()
    return players

def get_playernations(players, file):
    "Saves player+country-names in dictionary"
    pattern = re.compile(r'player=')
    for line in file:
        if(re.match(pattern,line)):
            player_name = re.search('".*"', line)
            line = file.readline() #get next line where the name of country is
            country_name = re.search('".*"', line)
            if(country_name):
                country_name = country_name.group(0)
                player_name = player_name.group(0)
                players[player_name.replace('"', '')] = country_name.replace('"', '')

def main():
    print("importing file: " +sys.argv[1])
    file = open(sys.argv[1])

    players = get_players(file)
    file.seek(0)
    player_nations = get_playernations(players, file)
    
    print("%16s %12s" % ("player", "played as"))
    for key in players:
        print ("%16s %12s" % (key, players[key]))

if __name__ == '__main__':
    main();