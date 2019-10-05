from os import listdir
from os.path import isfile,join
import sys

def main(filename="C:/"):
	mp4s=[]
	h264s=[]
	for f in listdir(filename):
		if(isfile(join(filename,f))):
			ext = f.split('.')[1]
			if(ext == 'mp4'):
				mp4s.append(f)
			elif(ext == 'h264'):
				h264s.append(f)

	print("mp4s")
	print(mp4s)
	print("h264s")
	print(h264s)


if __name__ == '__main__':
	main(filename=sys.argv[1])
