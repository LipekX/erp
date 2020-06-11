#Original code by Lipa#9327 https://github.com/LipekX https://lipa.ga/
#If you are making your own version of this tool, please leave this 1 line. Thank you <3
import time
import configparser
import io
import os
from pypresence import Presence
from appJar import gui

#config name
configfile_name = "config.ini"
#check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    #create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, "w")

    #add content to the file
    config = configparser.ConfigParser()
    config.add_section('presence')

    config['presence']['id'] = 'null'
    config['presence']['state'] = 'It works!'
    config['presence']['details'] = 'Discord ERP By Lipa <3'
    config['presence']['timestart'] = '1'
    config['presence']['timend'] = '2'
    config['presence']['imgbig'] = 'logo'
    config['presence']['imagesmall'] = ''
    config['presence']['toolsmall'] = 'It works!'
    config['presence']['toolbig'] = ''

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

#gui
app = gui("Discord ERP By Lipa", "500x250")
app.loadSettings(fileName="settings.ini", useSettings=True)
app.setIcon("icon.gif")
app.setBg("yellowgreen")
app.setFont(11)
app.addLabel("title", "Discord ERP")
app.setLabelBg("title", "yellow")
app.addLabel("main", "Main Settings")
app.addLabelEntry("ClientID")
app.addLabelEntry("State")
app.addLabelEntry("Details")
app.addLabel("time", "Timestamps")
app.addLabel("timew", "Time is in unix. Use epochconverter.com")
app.setLabelBg("timew", "red")
app.addLabelEntry("Start*")
app.addLabelEntry("End*")
app.addLabel("images", "Images")
app.addLabelEntry("Big*")
app.addLabelEntry("Small*")
app.addLabel("tooltipss", "Tooltips")
app.addLabelEntry("big*")
app.addLabelEntry("small*")
app.addLabel("optional", "* Optional")
#after button press
def press(button):
    if button == "Run":
        app.saveSettings(fileName="settings.ini")
        #get entries from gui
        cld = app.getEntry("ClientID")
        ste = app.getEntry("State")
        dsc = app.getEntry("Details")
        eps = app.getEntry("Start*")
        epe = app.getEntry("End*")
        igb = app.getEntry("Big*")
        igs = app.getEntry("Small*")
        tlb = app.getEntry("big*")
        tls = app.getEntry("small*")
        client_id = cld
        config = configparser.ConfigParser()
        config.add_section('presence')

        config['presence']['id'] = cld
        config['presence']['state'] = ste
        config['presence']['details'] = dsc
        config['presence']['timestart'] = eps
        config['presence']['timend'] = epe
        config['presence']['imgbig'] = igb
        config['presence']['imagesmall'] = igs
        config['presence']['toolsmall'] = tlb
        config['presence']['toolbig'] = tls

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    else:
        #read config   
        config = configparser.ConfigParser()
        config.read('config.ini')

        #set variables
        didf = config['presence']['id']
        dste = config['presence']['state']
        ddsc = config['presence']['details']
        deps = config['presence']['timestart']
        depe = config['presence']['timend']
        digb = config['presence']['imgbig']
        digs = config['presence']['imagesmall']
        dtlb = config['presence']['toolsmall']
        dtls = config['presence']['toolbig']

        #set presence
        client_id = didf
        RPC = Presence(client_id)
        RPC.connect()
        RPC.update(state=dste, details=ddsc, start=deps, end=depe, large_image=digb, small_image=digs, large_text=dtlb, small_text=dtls)
        app.saveSettings(fileName="settings.ini")

#rest of gui
app.addButtons(["Run", "Save"], press)
app.addLabel("down1", "Made with <3 By Lipa#9327")
app.go()