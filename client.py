import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover.jpg', 'wb')
fhand.write(img)
fhand.close()
