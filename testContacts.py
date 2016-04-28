#Tests Contacts App on Nexus 5 1080 x 1920 API 23
import sys
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

#Launch Contacts from the Home Screen
device.touch(335, 1700, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Add a contact
device.touch(950, 1700, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Make the contact local (if dialog box appears)
device.touch(310, 1060, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Activate the more fields category
device.touch(374, 893, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(352, 1406, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Add a name
device.touch(540, 522, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Contact for Validation'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Add an email
device.touch(540, 1500, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.type('TestValidationEmailForRobinson@email.com')
time.sleep(2)

#Add a phone number, set to home
device.touch(540, 1331, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.type('12345678900')
device.touch(540, 1478, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(540, 528, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Add a nickname
device.touch(540, 868, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Nickname for Validation'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Approve new contact
device.touch(1000, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Favorite the contact
device.touch(720, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)


#Edit Contact Tests

#Edit contact with intent of saving
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Change Name
device.touch(540, 823, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.type('2')
time.sleep(2)
#Change phone number
device.touch(600, 1150, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('5')
time.sleep(2)
#Change phone number type
device.touch(540, 1300, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(540, 528, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Change email
device.touch(540, 1652, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
for x in range(0, 10):
   device.press('KEYCODE_DPAD_LEFT', MonkeyDevice.DOWN_AND_UP)
device.type('2')
time.sleep(2)
#Approve changes
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Edit contact with intent of discarding changes
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Change Name
device.touch(540, 823, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
for x in range(0, 50):
   device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('Garbage')
time.sleep(2)
#Change phone number
device.touch(600, 1150, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
for x in range(0, 50):
   device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('0000000000')
time.sleep(2)
#Change phone number type
device.touch(540, 1300, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(540, 528, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Change email
device.touch(540, 1652, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
for x in range(0, 50):
   device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('garbageEmail@garbageService.goo')
time.sleep(2)
#Discard changes
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 305, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(725, 996, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Test Merging Contacts
#Add a contact
device.touch(950, 1700, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Add a name
device.touch(540, 900, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Contact for Validation Merged'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Save Contact
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Merge with the first contact
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Contact for Validation2'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(513, 534, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Approve changes
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)


#Test Seperating Contacts
device.touch(859, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(998, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(848, 1080, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Call number from Contact information screen
device.touch(862, 157, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Contact for Validation2'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(570, 500, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(500, 1300, MonkeyDevice.DOWN_AND_UP)
time.sleep(10)
device.touch(530, 1560, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Send message directly to Contact (this is to verify the name carries over to the messages app)
device.touch(960, 1300, MonkeyDevice.DOWN_AND_UP)
time.sleep(10)
#Back away from conversation with scripted Contact and Return to Home Screen
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Return to Contacts app
device.touch(335, 1700, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Sort by last name
device.touch(990, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 590, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 345, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(500, 1070, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(85, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Clean up Sort by
device.touch(990, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 590, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 345, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(500, 910, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(85, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Change Name Format
device.touch(990, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 590, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 560, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(500, 1070, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(85, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Clean up Name Format
device.touch(990, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 590, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(990, 560, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(500, 910, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(85, 145, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Open Favorite Contact
device.touch(260, 330, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(260, 615, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Remove favorite from Contact
device.touch(722, 152, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(792, 325, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#Test Deleting multiple contacts (clean up)
device.touch(862, 157, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
contactName = 'Test Contact for Validation'
for word in contactName.split(' '):
   device.type(word)
   device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Select both contacts created from this script
device.touch(570, 500, MonkeyDevice.DOWN)
time.sleep(1)
device.touch(570, 500, MonkeyDevice.UP)
time.sleep(1)
device.touch(570, 710, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
#Delete teh selected contacts
device.touch(1000, 157, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(1000, 290, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)
device.touch(840, 1013, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(1)
