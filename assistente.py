from inicializador_modelos import *
# from transcritor import *

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk import word_tokenize, corpus

from threading import Thread

# import lampada
# import tocador

import secrets
import pyaudio
import wave

import json
import os

FORMATO = pyaudio.paInt16
AMOSTRAS = 1024
CANAIS = 1
TEMPO_DE_GRAVAÇÃO = 5
CAMINHA_AUDIO_FALA = "E:\\MEGAsync\\projectServ\\www\\projetos\\ia\\dev\\assistente-iluminacao\\temp\\"
CAMINHA_CONFIG = "E:\\MEGAsync\\projectServ\\www\\projetos\\ia\\dev\\assistente-iluminacao\\data\\config.json"
# CAMINHA_AUDIO_FALA = "/home/john/projectServ/www/projetos/ia/aulas/PLN/dev/assistente_virtual/temp"
# CAMINHA_CONFIG = "/home/john/projectServ/www/projetos/ia/aulas/PLN/dev/assistente_virtual/config.json"

IDIOMA_CORPUS = "portuguese"
CONFIG = CAMINHA_CONFIG

def iniciar():
    ...

    return []

def configurar_atuadores():
    ...

    return []

def capturar_fala():
    ...

    return []

def gravar_fala():
    ...

    return []

def transcrever_fala():
    ...

    return []

def inicitranscrever_falaar():
    ...

    return []

def carregar_fala():
    ...

    return []

def processar_transcricao():
    ...

    return []

def validar_comando():
    ...

    return []

def atuar():
    ...

    return []