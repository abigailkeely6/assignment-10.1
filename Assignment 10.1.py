import os.path

directoryName = input('What is the name of the directory?')
fileName = input('What is the name of this file?')
filePath = os.path.join(directoryName, fileName)
if not os.path.isdir(directoryName):
  os.mkdir(directoryName)
username = input('What is your name?')
userAddy = input('What is your address?')
userPhone = input('What is your phone number?')
userInfo = (username, userAddy, userPhone)
file = open(filePath, 'w')
file.write(str(userInfo))
file.close()
file = open(filePath, 'r+')
print('Your file says', file.read())
file.close()