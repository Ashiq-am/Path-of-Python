import os
import shutil

os.chdir('C:\\')
username = os.environ['USERNAME']

# The folder which contains the wallpaper files
source = (
            "C:\\Users\\" + username + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\")

# You will have to add the path of your
# destination here. Just make sure the
# folder exists on the desktop.
destination = ("C:\\Users\\" + username + "\\Desktop\\WALLPAPER\\")

for the_file in os.listdir(destination):

    path_of_file = os.path.join(destination, the_file)
    base_file, ext = os.path.splitext(the_file)

    if ext == ".jpg":
        try:
            if os.path.isfile(path_of_file):
                os.unlink(path_of_file)

        except Exception as e:
            print(e)

for name_of_file in os.listdir(source):
    shutil.copy(source + name_of_file, destination)
    print(name_of_file)
