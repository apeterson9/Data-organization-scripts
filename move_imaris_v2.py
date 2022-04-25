import os,shutil
# This script will move Position, Speed, and Time spreadsheets that are output by Imaris and move them into one folder to

# TODO: if you run this script on the same folder twice, it will create another "Imaris file for analysis" folder with all the position/speed/time files in it without hierarchy

#get the user input for which folder to go through. check it exists
user_input = input('Enter a directory containing your movies \n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
print("Hooray we found your directory!")

#make a new directory to hold the position, speed and time files for that movie
new_dir = os.path.join(user_input,"Imaris output for analysis")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
print(new_dir)
#iterate through the folders and look for movie folders (ie Movie 1, Movie 2) and copy the position, speed and time files into the new directory
for root, dirs, files in os.walk(user_input):
    # root = directories only from what you specified
    # dirs = sub-directories from root
    # files = files from root and directories

    for name in files:
        if name.endswith(('t1_Position.csv', 't1_Speed.csv', 't1_Time.csv')):
            movie_new_dir = os.path.join(new_dir, os.path.basename(os.path.dirname(root)))
            subdirname = os.path.basename(os.path.dirname(root))
            print(subdirname)

            #print('movie_new_dir')
            #print(movie_new_dir)
            if not os.path.exists(movie_new_dir):
                os.mkdir(movie_new_dir)
            print(os.path.join(root, name))
            shutil.copy(os.path.join(root, name),movie_new_dir)

