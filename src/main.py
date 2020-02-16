import cv2
from api_calls import text_from_image, read_text
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import texttospeech

import time

from matplotlib import pyplot as plt

from PIL import Image

from Levenshtein import distance as levenshtein_distance

import numpy as np

from collections import defaultdict

import string

import simpleaudio as sa

from pydub import AudioSegment
from pydub.playback import play
import io


with open('../wp_1gram.txt') as f:
    lines = f.readlines()
processed_lines = [l.strip().split('\t') for l in lines]

word_counts = defaultdict(int)
for entry in processed_lines:
    #print(entry)
    try:
        count, word = entry
    except:
        print(entry)
        continue
    word_counts[word.lower()] += int(count)
