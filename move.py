from transmission_rpc import Client
from os import listdir, makedirs
from os.path import isdir
import shutil

download_dir = 'TORRENTS_FOLDER'
move_to = 'TARGET_FOLDER'
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

if len(completed) == 0:
  print('No completed downloads found')
  exit()

print('Following dirs will be moved: to "%s"' % move_to)
for d in completed:
    print("  - %s" % d)
print()
print("Do you confirm? [y/n]")
confirm = str(input())
if confirm == 'y':
    for c in completed:
        spath = download_dir + '/' + c
        tpath = move_to + '/' + c
        shutil.move(spath, tpath)
else:
    print('Canceled!')

print('Finished!')
