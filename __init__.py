"""
Plasma User Control Mycroft Skill.
"""

import sys
import dbus
import psutil
import platform
import datetime
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)


class InternalsPlasmaDesktopSkill(MycroftSkill):
    """
    Plasma User Control Skill Class.
    """

    def __init__(self):
        """
        Initialization
        """
        super(InternalsPlasmaDesktopSkill, self).__init__(
            name="InternalsPlasmaDesktopSkill")
                 
    @intent_handler(IntentBuilder("SwitchUserKeywordIntent").
                    require("InternalSwitchUserKeyword").build())
    def handle_internals_switchuser_plasma_skill_intent(self, message):
        """
        Switch User
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/KSMServer") 
        remote_object.openSwitchUserDialog(dbus_interface = "org.kde.KSMServerInterface")
        
        self.speak_dialog("internals.switchuser")
    
    @intent_handler(IntentBuilder("LogoutKeywordIntent").
                    require("InternalLogoutDesktopKeyword").build())
    def handle_internals_logout_plasma_skill_intent(self, message):        
        """
        Log Out
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/KSMServer") 
        remote_object.logout(1, 0, 0, dbus_interface = "org.kde.KSMServerInterface")
        
        self.speak_dialog("internals.logout")
    
    @intent_handler(IntentBuilder("LockKeywordIntent").
                    require("InternalLockDesktopKeyword").build())
    def handle_internals_lock_plasma_skill_intent(self, message):
        """
        Lock Screen
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.ksmserver","/ScreenSaver") 
        remote_object.Lock(dbus_interface = "org.freedesktop.ScreenSaver")
        
        self.speak_dialog("internals.lock")

    @intent_handler(IntentBuilder("IncreaseBrightnessKeywordIntent").
                    require("InternalIncreaseBrightnessDesktopKeyword").build())
    def handle_internals_increasebrightness_plasma_skill_intent(self, message):
        """
        Increase Brightness
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl")
        currentbrightness = remote_object.brightness(dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        if currentbrightness >=25 and currentbrightness < 1500:
            currentbrightness += 50
            remote_object.setBrightness(currentbrightness, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.increasebrightness")
    
    @intent_handler(IntentBuilder("DecreaseBrightnessKeywordIntent").
                    require("InternalDecreaseBrightnessDesktopKeyword").build())
    def handle_internals_decreasebrightness_plasma_skill_intent(self, message):
        """
        Decrease Brightness
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl")
        currentbrightness = remote_object.brightness(dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        if currentbrightness <=1500 and currentbrightness > 25:
            currentbrightness -= 50
            remote_object.setBrightness(currentbrightness, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.decreasebrightness")
        
    @intent_handler(IntentBuilder("MaximumBrightnessKeywordIntent").
                    require("InternalMaximumBrightnessDesktopKeyword").build())    
    def handle_internals_maximumbrightness_plasma_skill_intent(self, message):
        """
        Maximum Brightness
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl") 
        remote_object.setBrightness(1500, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.maximumbrightness")
    
    @intent_handler(IntentBuilder("MinimumBrightnessKeywordIntent").
                    require("InternalMinimumBrightnessDesktopKeyword").build())
    def handle_internals_minimumbrightness_plasma_skill_intent(self, message):
        """
        Minimum Brightness
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.freedesktop.PowerManagement","/org/kde/Solid/PowerManagement/Actions/BrightnessControl") 
        remote_object.setBrightness(25, dbus_interface = "org.kde.Solid.PowerManagement.Actions.BrightnessControl")
        
        self.speak_dialog("internals.minimumbrightness")
    
    @intent_handler(IntentBuilder("MoveMainPanelKeywordIntent").
                    require("InternalMoveMainPanelDesktopKeyword").build())
    def handle_internals_movemainpanel_plasma_skill_intent(self, message):
        """
        Move Main Panel
        """
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
    
    @intent_handler(IntentBuilder("AddWigetToPanelKeywordIntent").
                    require("InternalAddWidgetToPanelDesktopKeyword").build())
    def handle_internals_addwidget_plasmapanel_skill_intent(self, message):
        """
        Add Widget To Panel
        """
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
    
    @intent_handler(IntentBuilder("AddWigetToDesktopKeywordIntent").
                    require("InternalAddWidgetToDesktopKeyword").build())
    def handle_internals_addwidget_plasmadesktop_skill_intent(self, message):
        """
        Add Wiget To Desktop
        """        
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
    
    @intent_handler(IntentBuilder("ToogleTouchPadKeywordIntent").
                    require("InternalToogleTouchPadKeyword").build())
    def handle_internals_toogletouchpad_plasmadesktop_skill_intent(self, message):
        """
        Handle Touchpad
        """        
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('InternalToogleTouchPadKeyword'), '')
        gettogglequery = utterance.replace(" ", "")
        gettogglequery.encode('utf-8')
        
        if (gettogglequery == "enable") or ( gettogglequery == "enabled"):
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmanetworkmanagement","/modules/touchpad")
            remote_object.enable(dbus_interface = "org.kde.touchpad")
            self.speak("Touchpad Enabled")
        elif (gettogglequery == "disable") or (gettogglequery == "disabled"):
            bus = dbus.SessionBus()
            remote_object = bus.get_object("org.kde.plasmanetworkmanagement","/modules/touchpad")
            remote_object.disable(dbus_interface = "org.kde.touchpad")
            self.speak("Touchpad Disable")
        else:
            self.speak("Touchpad toggle not found, valid toggle's are: touchpad enable, touchpad disable")
    
    @intent_handler(IntentBuilder("ShowKlipperKeywordIntent").
                    require("InternalToogleKlipperKeyword").build())
    def handle_internals_toogleklipper_plasmadesktop_skill_intent(self, message):
        """
        Show Klipper
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.klipper","/klipper") 
        remote_object.showKlipperPopupMenu(dbus_interface = "org.kde.klipper.klipper")
   
    @intent_handler(IntentBuilder("ClearKlipperKeywordIntent").
                    require("InternalClearKlipperKeyword").build())
    def handle_internals_clearklipper_plasmadesktop_skill_intent(self, message):
        """
        Clear Klipper
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.klipper","/klipper") 
        remote_object.clearClipboardHistory(dbus_interface = "org.kde.klipper.klipper")
    
    @intent_handler(IntentBuilder("NextDesktopKeywordIntent").
                    require("InternalNextDesktopKeyword").build())
    def handle_internals_nextdesktop_plasmadesktop_skill_intent(self, message):
        """
        Go To Next Virtual Desktop
        """        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.KWin","/KWin") 
        remote_object.nextDesktop(dbus_interface = "org.kde.KWin")
 
    @intent_handler(IntentBuilder("PreviousDesktopKeywordIntent").
                    require("InternalPreviousDesktopKeyword").build())
    def handle_internals_previousdesktop_plasmadesktop_skill_intent(self, message):
        """
        Go To Previous Virtual Desktop
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.KWin","/KWin") 
        remote_object.previousDesktop(dbus_interface = "org.kde.KWin")
    
    @intent_handler(IntentBuilder("SuspendCompositingKeywordIntent").
                    require("InternalSuspendCompositingKeyword").build())
    def handle_internals_suspendcompositing_plasmadesktop_skill_intent(self, message):
        """
        Suspend Compositing
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.KWin","/Compositor") 
        remote_object.suspend(dbus_interface = "org.kde.kwin.Compositing")
        
    @intent_handler(IntentBuilder("ResumeCompositingKeywordIntent").
                    require("InternalResumeCompositingKeyword").build())    
    def handle_internals_resumecompositing_plasmadesktop_skill_intent(self, message):
        """
        Resume Compositing
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.KWin","/Compositor") 
        remote_object.resume(dbus_interface = "org.kde.kwin.Compositing")

    @intent_handler(IntentBuilder("SystemSummaryKeywordIntent").
                    require("InternalSystemSummaryKeyword").build())
    def handle_internals_systemsummary_plasmadesktop_skill_intent(self, message):
        """
        Speak System Summary
        """
        uname_info = platform.uname()
        uname_os = uname_info[0]
        uname_systemversion = uname_info[1]
        uname_kernelversion = uname_info[2]
        cores = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory()[2]
        disk_usage = psutil.disk_usage('/')[3]
        online_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        online_since = online_time.strftime("%A %d. %B %Y")
        reply = "I am currently running on {0} version {1}. This system is named {2} and has {3} CPU cores. Current Disk utilization is {4} percent. Current CPU utilization is {5} percent. Current Memory utilization is {6} percent. System is online since {7}.".format(uname_os, uname_kernelversion, uname_systemversion, cores, disk_usage, cpu_usage, memory_usage, online_since)
        self.speak(reply)
    
    @intent_handler(IntentBuilder("AddTopPanelDesktopKeywordIntent").
                    require("InternalAddTopPanelKeyword").build())
    def handle_internals_addpaneltop_plasmadesktop_skill_intent(self, message):
        """
        Add New Panel To Top
        """
        topJsc = 'var plasma = getApiVersion(1); var toppanel = new plasma.Panel; toppanel.location = "top"; toppanel.height = gridUnit * 2;'
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(topJsc)
    
    @intent_handler(IntentBuilder("AddLeftPanelDesktopKeywordIntent").
                    require("InternalAddLeftPanelKeyword").build())
    def handle_internals_addpanelleft_plasmadesktop_skill_intent(self, message):
        """
        Add New Panel To Left
        """
        leftJsc = 'var plasma = getApiVersion(1); var leftpanel = new plasma.Panel; leftpanel.location = "left"; leftpanel.height = gridUnit * 2;'
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(leftJsc)
    
    @intent_handler(IntentBuilder("AddRightPanelDesktopKeywordIntent").
                    require("InternalAddRightPanelKeyword").build())
    def handle_internals_addpanelright_plasmadesktop_skill_intent(self, message):
        """
        Add New Panel To Right
        """
        rightJsc = 'var plasma = getApiVersion(1); var rightpanel = new plasma.Panel; rightpanel.location = "right"; rightpanel.height = gridUnit * 2;'
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(rightJsc)
    
    @intent_handler(IntentBuilder("AddBottomPanelDesktopKeywordIntent").
                    require("InternalAddBottomPanelKeyword").build())
    def handle_internals_addpanelbottom_plasmadesktop_skill_intent(self, message):
        """
        Add New Panel To Bottom
        """
        bottomJsc = 'var plasma = getApiVersion(1); var bottompanel = new plasma.Panel; bottompanel.location = "bottom"; bottompanel.height = gridUnit * 2;'
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript(bottomJsc)
            
    def stop(self):
        """
        Mycroft Stop Function
        """
        pass


def create_skill():
    """
    Mycroft Create Skill Function
    """
    return InternalsPlasmaDesktopSkill()
