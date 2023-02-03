import os

f1 = open('sever.txt', 'r')
Ssever = f1.read()
def run():
    code = 'docker run traffmonetizer/cli start accept --token Rfh4oFnQAovccm4KZKOX1bMbUOsz/1k0ua8wJAdJESM= --device-name ' +  Ssever
    os.system(code)
run()
