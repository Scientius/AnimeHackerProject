import csv
import requests
from bs4 import BeautifulSoup
#Site to Jack Data From, Anime Style
url ="https://myanimelist.net/anime/season"
    
count = 0
#CSV File Creation to Save Data Into
filler = open("myanime{}.csv".format(count),'w',encoding="utf-8",newline='')

new = open("textmal.text", 'w',encoding="utf-8")
#Data Writer for CSV File
writer = csv.writer(filler)

#CSV File Data Headers
rows = ["Name","Score","Summary"]
writer.writerow(rows)

f = open("myanimelink.csv",'r')

reader = csv.DictReader(f)
gg = []
gg.append(url)

for link in reader:
    
    print(link["Season"] + "\t:\t"  +link["link"])
    
    gg.append(link["link"])

f.close()

myanimelist = list(dict.fromkeys(gg))

#Function to Jack Data 
def get_data(html_file):
    """ Scraping Data from My Anime List """
    #Parse HTML data into CSV File
    global count
    filler = open("myanime{}.csv".format(count),'w',encoding="utf-8",newline='')
    writer = csv.writer(filler)
    count += 1
    rows = ["Name","Score","Summary"]
    #CSV File Headers
    writer.writerow(rows)

    mal = BeautifulSoup(html_file , "html.parser")

    #Scraping Name and Score of Anime from Site HTML 
    summer = mal.find("div",class_ = "js-categories-seasonal")

    who=summer.find_all("div",class_="seasonal-anime js-seasonal-anime")

        #Loop for Jacking the Data
        
    for win in who :
            
        title = win.find("div")
            
        aniwin = win.find("div", class_="information")

        summary = win.find("span", class_="preline")
            
        scoreman = aniwin.find("div", class_ ="scormem")
            
        score = scoreman.find("span", class_="score")
                    
        ss = score.text.strip(" ")
            
        name = title.p.text

        summ = summary.text.strip(" ")
        
        print("       ")
            
        n = name.strip(" \n")
            
        s = ss.split()[0].strip(" \n")

        su = summ.strip(" \n")
            
        print(name.strip(" \n"), end= " : ")
            
        print(ss.split()[0])

        print(summ)
            
        print("     ")
        

            #Checking if Anime is Scored

        if s == "N/A":
                #Replace "NA" score with Different Output
            writer.writerow([n,"not scored yet"])
                
            #new.write(str(n) + ":" + str(s) + "\n")
                
            #new.write("-------------------------------\n")
                
        else:
                  
            writer.writerow([n,s,su])
                #writing in csv file
            #new.write(str(n) + ":" +str(s) + "\n")
                
            #new.write("-------------------------------\n")

for i in myanimelist:
    try:
        print(i)
        anime0 =  requests.get(i).text
        get_data(anime0)

    except:
        print("Reinitialize Data Scrape ...")

#Program Exit
filler.close()
new.close()