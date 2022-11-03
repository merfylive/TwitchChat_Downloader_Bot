import requests
from pywinauto.application import Application
import time

vod_link = "https://www.twitch.tv/videos/1639877813"
speicherpfad = "C:/Users/kramm/OneDrive/Desktop/TwitchChat_Bot/Testfiles/Output"

app = Application(backend="uia").start("F:\youtube, Design usw\CHat/release\TwitchDownloader.exe").connect(title="Twitch Downloader v1.50.4", timeout=100)

renderChat = app.TwitchDownloader.child_window(title="Chat Downloader", auto_id="btnChatDownload", control_type="Button").wrapper_object()
renderChat.click_input()

vodclipLink = app.TwitchDownloader.child_window(auto_id="textUrl", control_type="Edit").wrapper_object()
vodclipLink.type_keys(vod_link)

getInfo = app.TwitchDownloader.child_window(title="Get Info", auto_id="btnGetInfo", control_type="Button").wrapper_object()
getInfo.click_input()
#time.sleep(10)

try:
    embedEmotes = app.TwitchDownloader.child_window(title="FFZ", auto_id="checkFfzEmbed", control_type="CheckBox").wrapper_object()
    embedEmotes.click_input()
    embedEmotes.click_input()

except:
    embedEmotes = app.TwitchDownloader.child_window(auto_id="checkEmbed", control_type="CheckBox").wrapper_object()
    embedEmotes.click_input()

download = app.TwitchDownloader.child_window(title="Download", control_type="Text").wrapper_object()
download.click_input()

pfad = app.TwitchDownloader.child_window(title="Adressband", control_type="ToolBar").wrapper_object()
pfad.type_keys(speicherpfad)


app.TwitchDownloader.print_control_identifiers()