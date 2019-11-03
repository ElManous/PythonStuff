from lxml import html
import requests
import re
import json


# Call the link I want to scrape
club_page = requests.get('https://www.premierleague.com/clubs')
tree = html.fromstring(club_page.content)

linkLocation = tree.cssselect('.indexItem')

#Create an empty list for us to send each team's link to
teamLinks = []

#For each link...
for i in range(0,20):
    
    #...Find the page the link is going to...
    temp = linkLocation[i].attrib['href']
    
    #...Add the link to the website domain...
    temp = "http://www.premierleague.com/" + temp
    
    #...Change the link text so that it points to the squad list, not the page overview...
    temp = temp.replace("overview", "squad")
    
    #...Add the finished link to our teamLinks list...
    teamLinks.append(temp)

# create lists to differentiate the type of links 
playerLink1 = []
playerLink2 = []
 
# Download liverpool's team page
squadPage = requests.get(teamLinks[9])
squadTree = html.fromstring(squadPage.content)
    
# Extract the player links
playerLocation = squadTree.cssselect('.playerOverviewCard')

# For each player link within the team page..
for i in range(len(playerLocation)):
        
# save the link, complete with domain..
    playerLink1.append("http://www.premierleague.com/" + playerLocation[i].attrib['href'])
        
# For the second link, change the page from player overview to stats
    playerLink2.append(playerLink1[i].replace("overview", "stats"))


# create lists for each stat I want to scrape

Name = []
Position = []
Apps = []
Goals = []
Assists = []
Passes = []
BCC = []
CleanSheets = []
GKSaves = []
Tackles = []
Ints = []

j=0

# use for loop to loop thru the stats page to attain the stats I want
for i in range(len(playerLink2)):
    playerPage2 = requests.get(playerLink2[i])
    playerTree2 = html.fromstring(playerPage2.content)

# Player name
    tempName = str(playerTree2.cssselect('div.name')[0].text_content())
    
# assign the player position
    if(j<29):
        if (j<3):
            spot = "GK"
        elif (j<11 ):
            spot = "D"
        elif(j<21):
            spot = "M"
        else:
            spot = "F"
        j+=1
        #print(j)
        Position.append(spot)
    
# Appearances
    try:
        tempApps = playerTree2.cssselect('.statappearances')[0].text_content()
        tempApps = int(re.search(r'\d+', tempApps).group())
    except IndexError:
        tempApps = 0
# Goals   
    try:
        tempGoals = playerTree2.cssselect('.statgoals')[0].text_content()
        tempGoals= int(re.search(r'\d+', tempGoals).group())
    except IndexError:
        tempGoals = 0
# Assists        
    try:
        tempAssists = playerTree2.cssselect('.statgoal_assist')[0].text_content()
        tempAssists = int(re.search(r'\d+', tempAssists).group())
    except IndexError:
        tempAssists = 0
# Passes   
    try:
        tempPasses = playerTree2.cssselect('.stattotal_pass')[0].text_content()
        tempPasses = int(re.search(r'\d+', tempPasses).group())
    except IndexError:
        tempPasses = 0
# Big chances created   
    try:
        tempBCC = playerTree2.cssselect('.statbig_chance_created')[0].text_content()
        tempBCC = int(re.search(r'\d+', tempBCC).group())
    except IndexError:
        tempBCC = 0
# Clean sheets    
    try:
        tempCleanSheets = playerTree2.cssselect('.statclean_sheet')[0].text_content()
        tempCleanSheets = int(re.search(r'\d+', tempCleanSheets).group())
    except IndexError:
        tempCleanSheets = 0
# GK Saves
    try:
        tempGksaves = playerTree2.cssselect('.statsaves')[0].text_content()
        tempGksaves = int(re.search(r'\d+', tempGksaves).group())
    except IndexError:
        tempGksaves = 0
# Tackles
    try:
        tempTackles = playerTree2.cssselect('.stattotal_tackle')[0].text_content()
        tempTackles = int(re.search(r'\d+', tempTackles).group())
    except IndexError:
        tempTackles = 0
# Interceptions
    try:
        tempInts = playerTree2.cssselect('.statinterception')[0].text_content()
        tempInts = int(re.search(r'\d+', tempInts).group())
    except IndexError:
        tempInts = 0


    
# Append each player's stats to the lists I created earlier
    Name.append(tempName)
    Apps.append(tempApps)
    Goals.append(tempGoals)
    Assists.append(tempAssists)
    Passes.append(tempPasses)
    BCC.append(tempBCC)
    GKSaves.append(tempGksaves)
    CleanSheets.append(tempCleanSheets)
    Tackles.append(tempTackles)
    Ints.append(tempInts)


data={} #create a dictionary for storing player info
data['players']=[] 

#loop through players info and add their data to a specific entry in data
for i in range(0,29): 
    data['players'].append({
        'name':Name[i],
        'position':Position[i],
        'apps':Apps[i],
        'goals':Goals[i],
        'assists':Assists[i],
        'passes':Passes[i],
        'big chances created':BCC[i],
        'cleansheets':CleanSheets[i],
        'gksaves':GKSaves[i],
        'tackles':Tackles[i],
        'ints':Ints[i]
    })
#open file with JSON and dump data into output file
with open('playerData.txt','w') as outfile: 
    json.dump(data,outfile)








