import os, sys, io, tkinter, re, pandas

def get_players(file):
    "Finds the list of all players and adds to dictionary"
    players = dict()
    pattern = re.compile(r'players_countries={\n')
    for line in file:
        if(re.match(pattern, line)):
            line = file.readline() #skip line we just matched with
            while not (re.match('}\n', line)):
                player_name = line.strip().replace('"', '')
                line = file.readline()
                country_name = line.strip().replace('"', '')
                players[player_name] = country_name
                line = file.readline()
    return players


def main():
    print("importing file: " +sys.argv[1])
    file = open(sys.argv[1])

    players = get_players(file)
      
    print("%16s %12s" % ("player", "played as"))
    for key in players:
        print ("%16s %12s" % (key, players[key]))

if __name__ == '__main__':
    main();