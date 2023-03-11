import os

newpath = r'target'
if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, 11):
    if not os.path.exists(newpath + r'/' + str(i)):
        os.makedirs(newpath + r'/' + str(i))
    os.system(f"echo текст, чтобы папки залились на гит > {newpath + '/' + str(i) + '/text.txt'}")