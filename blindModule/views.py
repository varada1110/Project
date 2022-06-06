from django.shortcuts import render,redirect
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from IPython.display import Image
from cv2 import (VideoCapture, imwrite)
import os
import subprocess

global imagePath
# Create your views here.
def blindModule(request):

    return subprocess.run(['python', 'Untitled1.py'], shell=False, timeout=1800)