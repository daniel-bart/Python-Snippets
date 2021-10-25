import sys
import time
import random
import socket
import datetime
import os
import telepot
from telepot.loop import MessageLoop
from shutil import copyfile
import subprocess


date_zeit = datetime.datetime.now() + datetime.timedelta(minutes=30)



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg['text'].count('/schreib') >= 1 and msg['text'] != '/schreib':
	command,zeichen = msg['text'].split("/schreib ",1)
	zeichen[1:]
	if len(zeichen) <=25:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen])
	elif len(zeichen) >= 26 and len(zeichen) <= 50:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
	elif len(zeichen) >=51 and len(zeichen) <= 75:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
	elif len(zeichen) >=76 and len(zeichen) <= 100:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
	elif len(zeichen) >=101 and len(zeichen) <= 125:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
	elif len(zeichen) >=126 and len(zeichen) <= 150:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:125]
		zeichen6 = zeichen[125:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen6])
	elif len(zeichen) >=151 and len(zeichen) <= 175:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:125]
		zeichen6 = zeichen[125:150]
		zeichen7 = zeichen[150:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen6])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen7])
	elif len(zeichen) >=176 and len(zeichen) <= 200:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:125]
		zeichen6 = zeichen[125:150]
		zeichen7 = zeichen[150:175]
		zeichen8 = zeichen[175:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen6])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen7])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen8])
	elif len(zeichen) >=201 and len(zeichen) <= 225:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:125]
		zeichen6 = zeichen[125:150]
		zeichen7 = zeichen[150:175]
		zeichen8 = zeichen[175:200]
		zeichen9 = zeichen[200:]
		os.system("mpg123 -m /root/ringtone.mp3")
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen6])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen7])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen8])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen9])
	elif len(zeichen) >=226 and len(zeichen) <= 250:
		bot.sendMessage(chat_id, "Angezeigt wird: " + zeichen)
		clear = "##clear##"
		subprocess.call(['bash','tcp.sh','%s' % clear])
		zeichen1 = zeichen[:25]
		zeichen2 = zeichen[25:50]
		zeichen3 = zeichen[50:75]
		zeichen4 = zeichen[75:100]
		zeichen5 = zeichen[100:125]
		zeichen6 = zeichen[125:150]
		zeichen7 = zeichen[150:175]
		zeichen8 = zeichen[175:200]
		zeichen9 = zeichen[200:225]
		zeichen10 = zeichen[225:]
		os.system("mpg123 -m /root/ringtone.mp3")	
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen1])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen2])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen3])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen4])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen5])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen6])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen7])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen8])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen9])
		subprocess.call(['bash','/root/tcp.sh','%s' % zeichen10])
	elif len(zeichen) >=251:
		bot.sendMessage(chat_id, "Deine Nachricht ist leider zu lang!(max. 250 Zeichen)")
	#zeichenfolge = '(echo -en "display\n"; echo ' + zeichen
	#endfolge = zeichenfolge + ') > /dev/tcp/localhost/4444'
	#print(endfolge)
	#zeichenfolge = 'echo -n "sign/add/10:"' + zeichen
	#endfolge = zeichenfolge + ' | nc -u -w 10 localhost 4444&'
	#os.system("mpg123 -m /root/ringtone.mp3")
	#os.system(endfolge)
		

    elif content_type == 'text' and msg['text'] == '/schreib':
	bot.sendMessage(chat_id, "Du hast den Text hinter /schreib vergessen!")
	
    elif content_type == 'text' and msg['text'] == '/roll':
	bot.sendMessage(chat_id, random.randint(1,6))
    elif content_type == 'text' and msg['text'] == '/kassenstand':
	ip = get_ip()
	#print(ip)
	bot.sendMessage(chat_id, "Dein Guthaben kannst du [hier](%s) nachschauen." % ip,parse_mode= 'Markdown')
	bot.sendMessage(chat_id, "Usr: ****, Pw: ****")

    elif content_type == 'text' and msg['text'].count('/guthaben') == 1 and msg['text'] != '/guthaben':
	command,name = msg['text'].split("/guthaben ",1)
	name[1:]
	bot.sendMessage(chat_id, "Ich suche Guthaben von " + name)
	x = 0
	minus = '-'
	with open("/root/guthaben.txt") as search:
    	    for line in search:
                line = line.rstrip()  # remove '\n' at end of line
                if name in line:
		    bot.sendMessage(chat_id, line + ' \xe2\x82\xac'.decode('utf8'))
		    x += 1
		if name in line and minus in line:
		    bot.sendMessage(chat_id, "%s, du solltest wohl mal wieder einzahlen." % name) 
	if x == 0:
	   bot.sendMessage(chat_id, "Ich habe leider kein Guthaben zu dem Namen %s gefunden." % name)
         
    elif content_type == 'text' and msg['text'] == '/guthaben':
	bot.sendMessage(chat_id, "Du hast deinen Namen hinter /guthaben vergessen!")


    elif content_type == 'photo':
	file_nummer = datetime.datetime.now()
	os.system("mpg123 -m /root/ringtone.mp3")
        bot.download_file(msg['photo'][-1]['file_id'], "/root/info-beamer/info-beamer-pi/Switch/second/foto/%s.jpg" % file_nummer)
	copyfile('/root/info-beamer/info-beamer-pi/Switch/second/foto/%s.jpg' % file_nummer, '/root/info-beamer/info-beamer-pi/Switch/second/%s.jpg' % file_nummer)
	bot.sendMessage(chat_id, "Dein Bild wird gleich angezeigt.")

   # elif content_type == 'document':
	#gif_name = datetime.datetime.now()
	#bot.download_file(msg['document'][-1]['file_id'], "/root/gif/%s.gif" % gif_name)
	#os.system("ffmpeg -i %s.gif -pix_fmt yuv420p out.mp4" % gif_name)

    elif content_type == 'text' and msg['text'] == '/highscore':
	erster = open("/root/erster.txt",'r+')
	zweiter = open("/root/zweiter.txt",'r+')
	dritter = open("/root/dritter.txt",'r+')
	var1 = erster.read().replace('\n', '') + ' km/h'
	var2 = zweiter.read().replace('\n', '') + ' km/h'
	var3 = dritter.read().replace('\n', '') + ' km/h'
	bot.sendMessage(chat_id, 'Die aktuelle Highscore sieht wie folgt aus:')
	bot.sendMessage(chat_id, 'Platz 1. %s' % var1 )
	bot.sendMessage(chat_id, 'Platz 2. %s' % var2 )
	bot.sendMessage(chat_id, 'Platz 3. %s' % var3 )
	erster.close()
	zweiter.close()
	dritter.close()



bot = telepot.Bot('*******')
MessageLoop(bot, handle).run_as_thread()
#print ('Listening ...')

# Keep it running.
while 1:
    if datetime.datetime.now() >= date_zeit:
	ordner_name = "/root/info-beamer/info-beamer-pi/Switch/second/"
	test = os.listdir(ordner_name)
	for item in test:
    	    if item.endswith(".jpg"):
        	os.remove(os.path.join(ordner_name, item))
	date_zeit = datetime.datetime.now() + datetime.timedelta(minutes=30)
    time.sleep(10)