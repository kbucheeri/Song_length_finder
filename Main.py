#time program for playlists
f = open("D:\\Music\\Paul McCartney discography\\1970.McCartney (Remaster)\\McCartney.txt", "r")
#print(f.read())
lengths = []
txt = f.read()
#print(txt)
lines = txt.splitlines(False)
print(lines)
for i in lines:
    first_instance = i.find('[')
    if(first_instance >= 0):
        lengths.append(i[first_instance:])
print(lengths)
