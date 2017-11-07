import sys
import dbus
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class InternalsPlasmaDesktopSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(InternalsPlasmaDesktopSkill, self).__init__(name="InternalsPlasmaDesktopSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        internals_switchuser_plasma_skill_intent = IntentBuilder("SwitchUserKeywordIntent").\
            require("InternalSwitchUserKeyword").build()
        self.register_intent(internals_switchuser_plasma_skill_intent, self.handle_internals_switchuser_plasma_skill_intent)
        
        internals_lock_plasma_skill_intent = IntentBuilder("LockKeywordIntent").\
            require("InternalLockDesktopKeyword").build()
        self.register_intent(internals_lock_plasma_skill_intent, self.handle_internals_lock_plasma_skill_intent)
        
        internals_logout_plasma_skill_intent = IntentBuilder("LogoutKeywordIntent").\
            require("InternalLogoutDesktopKeyword").build()
        self.register_intent(internals_logout_plasma_skill_intent, self.handle_internals_logout_plasma_skill_intent)
        
        internals_increasebrightness_plasma_skill_intent = IntentBuilder("IncreaseBrightnessKeywordIntent").\
            require("InternalIncreaseBrightnessDesktopKeyword").build()
        self.register_intent(internals_increasebrightness_plasma_skill_intent, self.handle_internals_increasebrightness_plasma_skill_intent)
        
        internals_decreasebrightness_plasma_skill_intent = IntentBuilder("DecreaseBrightnessKeywordIntent").\
            require("InternalDecreaseBrightnessDesktopKeyword").build()
        self.register_intent(internals_decreasebrightness_plasma_skill_intent, self.handle_internals_decreasebrightness_plasma_skill_intent)

        internals_maximumbrightness_plasma_skill_intent = IntentBuilder("MaximumBrightnessKeywordIntent").\
            require("InternalMaximumBrightnessDesktopKeyword").build()
        self.register_intent(internals_maximumbrightness_plasma_skill_intent, self.handle_internals_maximumbrightness_plasma_skill_intent)
        
        internals_minimumbrightness_plasma_skill_intent = IntentBuilder("MinimumBrightnessKeywordIntent").\
            require("InternalMinimumBrightnessDesktopKeyword").build()
        self.register_intent(internals_minimumbrightness_plasma_skill_intent, self.handle_internals_minimumbrightness_plasma_skill_intent)
        
        internals_movemainpanel_plasma_skill_intent = IntentBuilder("MoveMainPanelKeywordIntent").\
            require("InternalMoveMainPanelDesktopKeyword").build()
        self.register_intent(internals_movemainpanel_plasma_skill_intent, self.handle_internals_movemainpanel_plasma_skill_intent)
        
        internals_addwidget_plasmapanel_skill_intent = IntentBuilder("AddWigetToPanelKeywordIntent").\
            require("InternalAddWidgetToPanelDesktopKeyword").build()
        self.register_intent(internals_addwidget_plasmapanel_skill_intent, self.handle_internals_addwidget_plasmapanel_skill_intent)

        internals_addwidget_plasmadesktop_skill_intent = IntentBuilder("AddWigetToDesktopKeywordIntent").\
            require("InternalAddWidgetToDesktopKeyword").build()
        self.register_intent(internals_addwidget_plasmadesktop_skill_intent, self.handle_internals_addwidget_plasmadesktop_skill_intent)
    
    def handle_internals_switchuser_plasma_skill_intent(self, message):
        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/KSMServer") 
        remote_object.openSwitchUserDialog(dbus_interface = "org.kde.KSMServerInterface")
        
        self.speak_dialog("internals.switchuser")
    
    def handle_internals_logout_plasma_skill_intent(self, message):        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/KSMServer") 
        remote_object.logout(1, 0, 0, dbus_interface = "org.kde.KSMServerInterface")
        
        self.speak_dialog("internals.logout")
    
    def handle_internals_lock_plasma_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/ScreenSaver") 
        remote_object.Lock(dbus_interface = "org.freedesktop.ScreenSaver")
        
        self.speak_dialog("internals.lock")

    def handle_internals_increasebrightness_plasma_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl")
        currentbrightness = remote_object.brightness(dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        if currentbrightness >=25 and currentbrightness < 1500:
            currentbrightness += 50
            remote_object.setBrightness(currentbrightness, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.increasebrightness")
        
    def handle_internals_decreasebrightness_plasma_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl")
        currentbrightness = remote_object.brightness(dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        if currentbrightness <=1500 and currentbrightness > 25:
            currentbrightness -= 50
            remote_object.setBrightness(currentbrightness, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.decreasebrightness")
        
    def handle_internals_maximumbrightness_plasma_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl") 
        remote_object.setBrightness(1500, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.maximumbrightness")
        
    def handle_internals_minimumbrightness_plasma_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl") 
        remote_object.setBrightness(25, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.minimumbrightness")
        
    def handle_internals_movemainpanel_plasma_skill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('InternalMoveMainPanelDesktopKeyword'), '')
        getloc = utterance.replace(" ", "")
        location = getloc

        if location == "bottom":
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
            remote_object.evaluateScript("var v = panelIds; panelById(v[0]).location = 'bottom';")
            self.speak_dialog("internals.changeloc")
        elif location == "top":
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
            remote_object.evaluateScript("var v = panelIds; panelById(v[0]).location = 'top';")
            self.speak_dialog("internals.changeloc")
        elif location == "left":
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
            remote_object.evaluateScript("var v = panelIds; panelById(v[0]).location = 'left';")
            self.speak_dialog("internals.changeloc")
        elif location == "right":
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
            remote_object.evaluateScript("var v = panelIds; panelById(v[0]).location = 'right';")
            self.speak_dialog("internals.changeloc")
        else:
            self.speak_dialog("internals.badlocation")
            
    def handle_internals_addwidget_plasmapanel_skill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('InternalAddWidgetToPanelDesktopKeyword'), '')
        getwidname = utterance.replace(" ", "")
        getwidname.encode('utf-8')
        genJsc = 'var utter = "{0}"; var r = knownWidgetTypes; var wr = knownWidgetTypes; var readablelist = []; for(var ir = 0; ir < r.length; ir++){{ var n = r[ir].split(".").pop(); readablelist.push(n); }}; if (readablelist.indexOf(utter) !== -1){{ var utterancematch = utter; for (var lr=0; lr < r.length; lr++){{ if (wr[lr].match(utterancematch)) {{ var widgtName = (wr[lr]); var v = panelIds; panelById(v[0]).addWidget(widgtName); }}; }}; }} else {{ print ("Keyword not Found"); }}'.format(getwidname)
        sendJsc = genJsc
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(sendJsc)
        self.speak_dialog("internals.widadded")
        
    def handle_internals_addwidget_plasmadesktop_skill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('InternalAddWidgetToDesktopKeyword'), '')
        getwidname = utterance.replace(" ", "")
        getwidname.encode('utf-8')
        genJsc = 'var utter = "{0}"; var r = knownWidgetTypes; var wr = knownWidgetTypes; var readablelist = []; for(var ir = 0; ir < r.length; ir++){{ var n = r[ir].split(".").pop(); readablelist.push(n); }}; if (readablelist.indexOf(utter) !== -1){{ var utterancematch = utter; for (var lr=0; lr < r.length; lr++){{ if (wr[lr].match(utterancematch)) {{ var widgtName = (wr[lr]); var mainDesktop = desktops(); var d = mainDesktop[0]; d.addWidget(widgtName); }}; }}; }} else {{ print ("Keyword not Found"); }}'.format(getwidname)
        sendJsc = genJsc
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(sendJsc)
        self.speak_dialog("internals.widadded")
        
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return InternalsPlasmaDesktopSkill()
