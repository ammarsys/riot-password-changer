import os
import getpass

username = getpass.getuser()

directory = fr'C:\Users\{username}\AppData\Roaming\undetected_chromedriver'
os.chdir(directory)

file_path = os.path.join(directory, 'undetected_chromedriver.exe')
if os.path.exists(file_path):
    os.remove(file_path)
    print('Binary deleted successfully.')
else:
    print('Binary not found.')
