import torch
import subprocess


try:
    subprocess.check_output('nvidia-smi')
    print('Nvidia GPU detected!')
except Exception: # this command not being found can raise quite a few different errors depending on the configuration
    print('No Nvidia GPU in system!')
    

if torch.cuda.is_available():
    print("GPU is available")
else:
    print("GPU is not available")
