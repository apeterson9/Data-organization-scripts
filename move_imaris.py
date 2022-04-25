import os,shutil
# This script will move Position, Speed, and Time spreadsheets that are output by Imaris and move them into one folder to

#get the user input for which folder to go through. check it exists
user_input = input('Enter a directory containing tif files for one movie at a time\n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
print("Hooray we found your directory!")

#make a new directory to hold the position, speed and time files for that movie
new_dir = os.path.join(user_input,"1. position_speed_time")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

#iterate through the folders and copy the position, speed and time files into the new directory
for root, dirs, files in os.walk(user_input):
    # root = directories from what you specified
    # dirs = sub-directories from root
    # files = files from root and directories
    for name in files:
        
        if name.endswith(('t1_Position.csv','t1_Speed.csv','t1_Time.csv')):
            print(os.path.join(root, name))
            shutil.copy(os.path.join(root, name),new_dir)


#create a new file to put all the files