from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .settings import BASE_DIR

from os import listdir,system
from os.path import isfile, join
MOTION_DIR_PATH = "/media/"


def list(request):
	mp4s=[]
	h264s=[]
	path = BASE_DIR+MOTION_DIR_PATH
	for file in listdir(path):
		if(isfile(join(path,file))):
			ext = file.split('.')
			if(ext[1] and ext[1] == 'mp4'):
				mp4s.append(file)
			elif(ext[1] and ext[1] == 'h264'):
				h264s.append(file)
	context = {	
		'mp4s':mp4s,
		'h264s':h264s,
	}
	print(context)

	return render(request,'list.html',context)

def convert(request,filename):
	filename = str(filename)
	ext = filename.split('.')

	if(ext[1] == 'h264'):
		ret = system("ffmpeg -i "+filename+" -c copy "+ext[0]+".mp4 ")
		print("converted")
	return HttpResponseRedirect('/media/'+ext[0]+'.mp4')

