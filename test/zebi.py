import mediapipe
import sys
import os

print("--- DIAGNOSTIC ---")
print("Version Python :", sys.version)
print("Chemin de l'exécutable :", sys.executable)
print("Emplacement du module Mediapipe :", mediapipe.__file__)
print("Contenu du module :", dir(mediapipe))