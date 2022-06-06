{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3d2654e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting azure-cognitiveservices-vision-computervision\n",
      "  Downloading azure_cognitiveservices_vision_computervision-0.9.0-py2.py3-none-any.whl (39 kB)\n",
      "Collecting msrest>=0.5.0\n",
      "  Downloading msrest-0.6.21-py2.py3-none-any.whl (85 kB)\n",
      "Collecting azure-common~=1.1\n",
      "  Downloading azure_common-1.1.28-py2.py3-none-any.whl (14 kB)\n",
      "Requirement already satisfied: requests~=2.16 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2.25.1)\n",
      "Requirement already satisfied: requests-oauthlib>=0.5.0 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.3.1)\n",
      "Collecting isodate>=0.6.0\n",
      "  Downloading isodate-0.6.1-py2.py3-none-any.whl (41 kB)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2020.12.5)\n",
      "Requirement already satisfied: six in c:\\users\\varada\\anaconda3\\lib\\site-packages (from isodate>=0.6.0->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.15.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.26.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2.10)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (3.0.4)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\varada\\anaconda3\\lib\\site-packages (from requests-oauthlib>=0.5.0->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (3.2.0)\n",
      "Installing collected packages: isodate, msrest, azure-common, azure-cognitiveservices-vision-computervision\n",
      "Successfully installed azure-cognitiveservices-vision-computervision-0.9.0 azure-common-1.1.28 isodate-0.6.1 msrest-0.6.21\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade azure-cognitiveservices-vision-computervision"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3b96081d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pygame\n",
      "  Downloading pygame-2.1.2-cp38-cp38-win_amd64.whl (8.4 MB)\n",
      "Installing collected packages: pygame\n",
      "Successfully installed pygame-2.1.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pygame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "74881a8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a person in a blue shirt\n"
     ]
    }
   ],
   "source": [
    "from azure.cognitiveservices.vision.computervision import ComputerVisionClient\n",
    "from msrest.authentication import CognitiveServicesCredentials\n",
    "from IPython.display import Image\n",
    "from cv2 import *\n",
    "\n",
    "import os\n",
    "import pyttsx3\n",
    "\n",
    "region = \"centralindia\"\n",
    "key = \"56231a7876fa489d82f888f5c71be200\"\n",
    "endpoint = \"https://assistivedevice.cognitiveservices.azure.com/\"\n",
    "cam_port = 0\n",
    "cam = VideoCapture(cam_port)\n",
    "  \n",
    "# reading the input using the camera\n",
    "result, image = cam.read()\n",
    "if result:\n",
    "    imagePath = \"C:/Users/Varada/Desktop/Django_Projects/Final_Project/text.jpg\"\n",
    "    imwrite(imagePath, image)\n",
    "\n",
    "\n",
    "credentials = CognitiveServicesCredentials(key)\n",
    "client = ComputerVisionClient(endpoint=endpoint,credentials=credentials)\n",
    "k = open(imagePath,\"rb\")\n",
    "\n",
    "with k as img:\n",
    "    result = client.describe_image_in_stream(img)\n",
    "\n",
    "m = result.captions[0].text\n",
    "print(m)\n",
    "#Image(filename=imagePath,width=120,height=120)\n",
    "\n",
    "engine = pyttsx3.init()\n",
    "  \n",
    "# an audio will be played which speaks the test if pyttsx3 recognizes it\n",
    "engine.say(m)                             \n",
    "engine.runAndWait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6de16668",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "523073e9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
