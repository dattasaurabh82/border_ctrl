#!/usr/bin/python
'''
            _____                  _
           | ___ \                | |
           | |_/ /  ___   _ __  __| |  ___  _ __
           | ___ \ / _ \ | '__|/ _` | / _ \| '__|
           | |_/ /| (_) || |  | (_| ||  __/| |
           \____/  \___/ |_|   \__,_| \___||_|
                              _                _
                             | |              | |
            ___  ___   _ __  | |_  _ __  ___  | |
           / __|/ _ \ | '_ \ | __|| '__|/ _ \ | |
          | (__| (_) || | | || |_ | |  | (_) || |
           \___|\___/ |_| |_| \__||_|   \___/ |_|

  -------------- 9-9-9-9-9-9-9-9-9-9-9-9-9 ---------------

               __  __      __ __          __    ___
         /\   / _ /  \\  /|_ |__)|\ ||\/||_ |\ | |
        /--\  \__)\__/ \/ |__| \ | \||  ||__| \| |

      __  __  __  __      __          __       ___ __
     |__)|__)/  \|__) /\ / _  /\ |\ ||  \ /\    | /  \
     |   | \ \__/|   /--\\__)/--\| \||__//--\   | \__/

         __ __     ___ __  __          __      __
        /  /  \|\ | | |__)/  \|    \_//  \/  \|__)
        \__\__/| \| | | \ \__/|__   | \__/\__/| \

         ___ __ __      __ ___  ___ __         __    __
    ||\ | | |_ |__)|\ ||_   |    | |__) /\\  /|_ |  (_
    || \| | |__| \ | \||__  |    | | \ /--\\/ |__|____)

                        __ __  __  __ __
                    /\ /  |__)/  \(_ (_
                   /--\\__| \ \__/__)__)

              ___ __ __        ___  __
         ||\ | | |_ |__)|\ | /\ | |/  \|\ | /\ |
         || \| | |__| \ | \|/--\| |\__/| \|/--\|__

                  __  __               __
                 |  \/  \|\/| /\ ||\ |(_
                 |__/\__/|  |/--\|| \|__)

'''

import subprocess
import time
import webbrowser
import os
import urllib
import json
from bs4 import BeautifulSoup

url = " "
latest_url = " "
stripped_url = " "
stripped_url_final = " "
www_index = 0
com_index = 0
visa_status = False

us_counter = 0

print '''            _____                  _
           | ___ \                | |
           | |_/ /  ___   _ __  __| |  ___  _ __
           | ___ \ / _ \ | '__|/ _` | / _ \| '__|
           | |_/ /| (_) || |  | (_| ||  __/| |
           \____/  \___/ |_|   \__,_| \___||_|
                              _                _
                             | |              | |
            ___  ___   _ __  | |_  _ __  ___  | |
           / __|/ _ \ | '_ \ | __|| '__|/ _ \ | |
          | (__| (_) || | | || |_ | |  | (_) || |
           \___|\___/ |_| |_| \__||_|   \___/ |_|
      '''
def n_voice_alert(text, cn_cde):
  # making voice alerts:
  f = subprocess.Popen(["say", text, cn_cde, "Embassy"], stdout=subprocess.PIPE)
  feedback, errrrrr = f.communicate()
  print feedback


def p_voice_alert(text):
  # making voice alerts:
  f = subprocess.Popen(["say", text], stdout=subprocess.PIPE)
  feedback, errrrrr = f.communicate()
  print feedback



def domian_exe(header, domain_extension, buff):
  if domain_extension in url:
    # there could be other vars of domain to be added later .cn, .in, .org, .edu, .io,
    stripped_url = url.lstrip(header) # remove the http or https tags from beginning
    www_index = stripped_url.index("/") + 2 # counting after that
    com_index = stripped_url.index(domain_extension) + buff # finding till .com or other domain endings
    stripped_url_final = stripped_url[www_index: com_index: ] # joing them to get the mail url btn them
    print "cleaned main url domain is:", stripped_url_final
    print " "
    print "---------------------------------------------"
    print " "

    ########## Find the website's IP #############
    #----- Running terminal command:  nslookup <website> -----#
    p = subprocess.Popen(["nslookup", stripped_url_final], stdout=subprocess.PIPE)
    output, err = p.communicate() # grabbing the value from terminal
    print "IP address data of url by ns lookup command: ", output
    print " "
    print "---------------------------------------------"
    print " "
     #---- strip and get the single simple IP ----#
    index_of_ip = output.rfind("Address: ") # finding the index of last addess
    url_ip = output[(index_of_ip + 9): len(output)-2] # indexing from the last address index to the last character and getting everything in-between
    print "Simplified IP: ", url_ip
    print " "
    print "---------------------------------------------"
    print " "
    #----- find url's country code -----#
    command = "%s%s%s" % ("ipinfo.io/",url_ip,"/country")
    q = subprocess.Popen(["curl", command], stdout=subprocess.PIPE)
    ip_info, errr = q.communicate() # grabbing the value from terminal
    #print ip_info
    url_cn_code = "%s%s" % (ip_info[len(ip_info)-3], ip_info[len(ip_info)-2])
    print "URL's country code is:", url_cn_code # IMPORTANT TO COMPARE LATER
    print " "
    print "---------------------------------------------"
    print " "
    #------ find your ip and country ------#
    r = subprocess.Popen(["curl", "ipinfo.io/country"], stdout=subprocess.PIPE)
    self_ip_info, errrr = r.communicate() # grabbing the value from terminal
    #print self_ip_info and country code
    your_cn_code = "%s%s" % (self_ip_info[len(self_ip_info)-3], self_ip_info[len(self_ip_info)-2])
    print "Your country code is:", your_cn_code # IMPORTANT TO COMPARE LATER
    print " ", "\n"


    #---------------country comparison--------------#
    if your_cn_code != url_cn_code:
      url_country = json_data[url_cn_code]["CountryName"]
      _url_country = url_country.replace(" ", "+")
      your_current_country = json_data[your_cn_code]["CountryName"]
      _your_current_country = your_current_country.replace(" ", "+")
      
      print "you need a visa to travel to:", url_country, "from your country:", your_current_country
      # making voice alerts:
      alert_message = "Sorry. You need a visa to travel to this domain. Please contact the"
      n_voice_alert(alert_message, url_country)
      alert_message = "We will be closing this tab in 5 seconds after this message ends. Happy Browsing"
      p_voice_alert(alert_message)

      # QUIT THE TAB
      # -- Other part of subprocess calls is down in the main loop and we would already be in the folder
      # -- as this func is called after other subprocess call(the call to take you to the main folder)
      time.sleep(5)
      subprocess.call(["osascript", quitter_script]) # RUN THE QUITTER TAB SCRIPT . We are already in the directory
      # OPEN a google search page for visa
      visa_url = "https://www.google.com/#q=visa+for+" + _url_country + "+from+" + _your_current_country
      webbrowser.open_new_tab(visa_url)

    else:
      print "you don't need a visa."
      alert_message = "This domain is in your country. So you don't need a visa. Happy Browsing"
      p_voice_alert(alert_message)

      #visa_status = False
      #return visa_status

    print "##############################################", "\n", "\n"



# for 3 digit domain ext buff is 4
# for 2 digit domain ext buff is 3

# a lot of other domains needs to be in-corporated
# I'm lazy so just did these few.. in a very un-optimized way

def domain_check():
  if "http://" in url:
    if ".com" in url:
      domian_exe('http:', ".com", 4)
    if ".org" in url:
      domian_exe('http:', ".org", 4)
    if ".edu" in url:
      domian_exe('http:', ".edu", 4)
    if ".net" in url:
      domian_exe('http:', ".net", 4)
    if ".cc" in url:
      domian_exe('http:', ".cc", 3)
    if ".io" in url:
      domian_exe('http:', ".io", 3)
    if ".me" in url:
      domian_exe('http:', ".me", 3)
    if ".eu" in url:
      domian_exe('http:', ".eu", 3)
    if ".in" in url:
      domian_exe('http:', ".in", 3)
    if ".dk" in url:
      domian_exe('http:', ".dk", 3)
    if ".cn" in url:
      domian_exe('http:', ".cn", 3)
    if ".jp" in url:
      domian_exe('http:', ".jp", 3)
    if ".kr" in url:
      domian_exe('http:', ".kr", 3)
    if ".tw" in url:
      domian_exe('http:', ".tw", 3)
    if ".uk" in url:
      domian_exe('http:', ".uk", 3)
    if ".it" in url:
      domian_exe('http:', ".it", 3)
    if ".fr" in url:
      domian_exe('http:', ".fr", 3)
    if ".ae" in url:
      domian_exe('http:', ".ae", 3)
    if ".hk" in url:
      domian_exe('http:', ".hk", 3)
    if ".cc" in url:
      domian_exe('http:', ".cc", 3)
    if ".io" in url:
      domian_exe('http:', ".io", 3)
    if ".me" in url:
      domian_exe('http:', ".me", 3)
    if ".eu" in url:
      domian_exe('http:', ".eu", 3)
    if ".ac" in url:
      domian_exe('http:', ".ac", 3)
    if ".ca" in url:
      domian_exe('http:', ".ca", 3)
    if ".af" in url:
      domian_exe('http:', ".af", 3)
    if ".at" in url:
      domian_exe('http:', ".at", 3)
    if ".ar" in url:
      domian_exe('http:', ".ar", 3)
    if ".au" in url:
      domian_exe('http:', ".au", 3)
    if ".be" in url:
      domian_exe('http:', ".be", 3)
    if ".br" in url:
      domian_exe('http:', ".br", 3)
    if ".tv" in url:
      domian_exe('http:', ".tv", 3)


  elif "https://" in url:
    if ".com" in url:
      domian_exe('https:', ".com", 4)
    if ".org" in url:
      domian_exe('https:', ".org", 4)
    if ".edu" in url:
      domian_exe('https:', ".edu", 4)
    if ".net" in url:
      domian_exe('https:', ".net", 4)
    if ".cc" in url:
      domian_exe('https:', ".cc", 3)
    if ".io" in url:
      domian_exe('https:', ".io", 3)
    if ".me" in url:
      domian_exe('https:', ".me", 3)
    if ".eu" in url:
      domian_exe('https:', ".eu", 3)
    if ".in" in url:
      domian_exe('https:', ".in", 3)
    if ".dk" in url:
      domian_exe('https:', ".dk", 3)
    if ".cn" in url:
      domian_exe('https:', ".cn", 3)
    if ".jp" in url:
      domian_exe('https:', ".jp", 3)
    if ".kr" in url:
      domian_exe('https:', ".kr", 3)
    if ".tw" in url:
      domian_exe('https:', ".tw", 3)
    if ".uk" in url:
      domian_exe('https:', ".uk", 3)
    if ".it" in url:
      domian_exe('https:', ".it", 3)
    if ".fr" in url:
      domian_exe('https:', ".fr", 3)
    if ".ae" in url:
      domian_exe('https:', ".ae", 3)
    if ".hk" in url:
      domian_exe('https:', ".hk", 3)
    if ".cc" in url:
      domian_exe('https:', ".cc", 3)
    if ".io" in url:
      domian_exe('https:', ".io", 3)
    if ".me" in url:
      domian_exe('https:', ".me", 3)
    if ".eu" in url:
      domian_exe('https:', ".eu", 3)
    if ".ac" in url:
      domian_exe('https:', ".ac", 3)
    if ".ca" in url:
      domian_exe('https:', ".ca", 3)
    if ".af" in url:
      domian_exe('https:', ".af", 3)
    if ".at" in url:
      domian_exe('https:', ".at", 3)
    if ".ar" in url:
      domian_exe('https:', ".ar", 3)
    if ".au" in url:
      domian_exe('https:', ".au", 3)
    if ".be" in url:
      domian_exe('https:', ".be", 3)
    if ".br" in url:
      domian_exe('https:', ".br", 3)
    if ".tv" in url:
      domian_exe('https:', ".tv", 3)

  else :
    print "couldn't find either http or https"
    print url
    print "---------------------------------------------"

########## ------------- Loading some basic JSON DATA for later
json_data_url = "https://api.myjson.com/bins/9ie91"
json_response = urllib.urlopen(json_data_url)
json_data = json.loads(json_response.read())

##########------------- init part of script ------------##########
# to get the path of the folder where the script is kept
main_path = os.getcwd()
#print main_path.find('/', 8)
index_of_3rd_slash = main_path.find("/", 8)
directory = main_path[(index_of_3rd_slash + 1): len(main_path)] # WOULD NEEDED DOWN THERE
#directory = main_path[(main_path.index("Desktop")): len(main_path)]
#print directory
dump_file = "%s%s" % (main_path, "/url.txt") # WOULD NEEDED DOWN THERE
#print dump_file
##########------------- main loop ------------############

#directory = "Desktop/scarperProject/python_scripts"
#apple_script = "activeWindow.app"
apple_script = "activeWindow.scpt"
#dump_file = '/Users/saurabh.datta/Desktop/url.txt'
quitter_script = "quitter.scpt"

us_counter = 0

while True:
  # --------- grab the active tab's url --------- #
  #/Users/saurabh.datta/Desktop/scraperproject/python_scripts
  subprocess.call(["cd ", directory], shell=True)
  subprocess.call(["osascript", apple_script])

  file = open(dump_file, "r")
  content = (file.read())
  url = str(content)
  #url = dump_file
  print "un-edited url: ", url, "  :: Length of url: ", len(url)
  print " "
  print "---------------------------------------------"
  print " "

  if latest_url != url:
    domain_check()
  else:
    print " "
    print "--------------------------------"
    print "No new domains have been visited"
    print "--------------------------------", "\n"

  latest_url = url

  time.sleep(20)