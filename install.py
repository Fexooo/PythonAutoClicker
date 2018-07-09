import time
import urllib.request
import zipfile
import os
import subprocess
import shutil
print("Installing necessary Components!");
print("In 3");
time.sleep(1);
print("In 2");
time.sleep(1);
print("In 1");
time.sleep(1);
print("Downloading Keyboard Module!");
urllib.request.urlretrieve("https://github.com/boppreh/keyboard/archive/master.zip", "master.zip");
print("Downloaded!");
time.sleep(1);
print("Extracting Keyboard Module!");
zip_ref = zipfile.ZipFile("master.zip", 'r');
zip_ref.extractall("install/");
zip_ref.close();
print("Extracted Keyboard Module!");
time.sleep(1);
print("Installing Keyboard Module!");
os.chdir("install/keyboard-master/");
os.system("python setup.py install");
os.chdir("..")
os.chdir("..")
print("Installed Keyboard Module!");
time.sleep(1);
print("Cleaing up...");
os.remove("master.zip");
shutil.rmtree("install")
print("Cleaned up!");
print("Finished Installing necessary Components!");
time.sleep(3);
exit();