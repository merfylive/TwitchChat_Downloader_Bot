import requests
from pywinauto.application import Application



app = Application(backend="uia").start("F:\youtube, Design usw\CHat/release\TwitchDownloader.exe").connect(title="Twitch Downloader v1.50.4", timeout=100)
#app.TwitchDownloader.print_control_identifiers()
renderChat = app.TwitchDownloader.child_window(title="Chat Downloader", auto_id="btnChatDownload", control_type="Button").wrapper_object()
renderChat.click_input()
#app.TwitchDownloader.print_control_identifiers()
vod_link = "https://www.twitch.tv/videos/1639877813"
#vodclipLink = app.TwitchDownloader.child_window(auto_id="textUrl", control_type="Text").wrapper_object()
vodclipLink = app.TwitchDownloader.child_window(auto_id="textUrl", control_type="Edit").wrapper_object()
vodclipLink.type_keys(vod_link)