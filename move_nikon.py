import os,shutil
# This script will move files from one position on an LD or lumen dish and move them into the appropriate folders so you can open all the frames as a movie

#get the user input for which folder to go through. check it exists
user_input = input('Enter a directory containing your movies \n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
print("Hooray we found your directory!")

#ask the user how many positions are on the device and create that number of BF and fluor folders

for file in os.listdir(user_input):
    file_splits = file.split('_')
    path_name = file_splits[1] + ' ' + file_splits[2]
    movie_new_dir = os.path.join(user_input, path_name)
    if not os.path.exists(movie_new_dir):
        os.mkdir(movie_new_dir)
    shutil.move(os.path.join(user_input,file), movie_new_dir)


# #iterate through the folder and look for movies with the prefix and position and move into the right folder
# for root, dirs, files in os.walk(user_input):
#     # root = directories only from what you specified
#     # dirs = sub-directories from root
#     # files = files from root and directories
#
#     for name in files:
#         if name.endswith(('t1_Position.csv', 't1_Speed.csv', 't1_Time.csv')):
#             movie_new_dir = os.path.join(new_dir, os.path.basename(os.path.dirname(root)))
#             subdirname = os.path.basename(os.path.dirname(root))
#             print(subdirname)
#
#             #print('movie_new_dir')
#             #print(movie_new_dir)
#             if not os.path.exists(movie_new_dir):
#                 os.mkdir(movie_new_dir)
#             print(os.path.join(root, name))
#             shutil.copy(os.path.join(root, name),movie_new_dir)
#
