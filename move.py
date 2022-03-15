from transmission_rpc import Client
from os import listdir, makedirs
from os.path import isdir
import shutil

download_dir = 'TORRENTS_FOLDER'
move_to = 'TARGET_FOLDER'

def validate_dirs():
    if download_dir == 'TORRENTS_FOLDER':
        print('ERROR: "download_dir" folder was not set')
        return False
    
    if move_to == 'TARGET_FOLDER':
        print('ERROR: "move_to" folder was not set')
        return False
    
    return True

def prepare():
    makedirs(move_to, exist_ok=True)
    all_dirs = set()
    for f in listdir(download_dir):
        if f == '_completed':
            continue
        if isdir(download_dir + '/' + f):
            all_dirs.add(f)


    c = Client()
    r = c.get_torrents()
    downloading = set()
    for i in r:
        if i.status != 'seeding':
            downloading.add(i.name)

    completed = all_dirs.difference(downloading)

    return completed

def move_files(completed):
    if len(completed) == 0:
        print('ERROR: No completed downloads found')
        return

    print('Following dirs will be moved: to "%s"' % move_to)
    i = 0
    for d in completed:
        print("  %2d) %s" % (i + 1, d))
        i+=1
    print()
    print("Do you confirm? [y/n]")
    confirm = str(input())
    if confirm == 'y':
        for c in completed:
            spath = download_dir + '/' + c
            tpath = move_to + '/' + c
            shutil.move(spath, tpath)
            print('Finished!')
    else:
        print('Canceled!')


if __name__ == '__main__':
    is_valid = validate_dirs()
    if is_valid:
        completed = prepare()
        move_files(completed)