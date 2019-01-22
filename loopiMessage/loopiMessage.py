import os
import time

cmd = """osascript<<END
tell application "Messages"
send "hello friend" to buddy "<iMessage id>" of (service 1 whose service type is iMessage)
end tell
END"""

def send_Message():
     os.system(cmd)

while 1:
     time.sleep(1)
     send_Message()
