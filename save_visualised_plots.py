from tensorflow.keras.datasets import mnist
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plotHistory(model_history, figname):
  fig = plt.figure(figsize=(20,10))
  gs = gridspec.GridSpec(nrows=4,
                         ncols=4,
                         figure=fig,
                         width_ratios= [1, 1, 1, 1], # width of each of the␣
                         height_ratios=[1, 1, 1, 1], # height of each of the␣ wspace=0.5, # vertical margin between columns
                         hspace=0.5) # horizontal margin between columns # create 5 different axis located in the grid
    
  ax1 = fig.add_subplot(gs[0:2, 0:2])
  ax2 = fig.add_subplot(gs[0:2, 2:4]) # the plot starts in position 1 (at the␣ 􏰀→end of column 0) and ends in position 4 (at the end of column 4)

  ax1.plot(model_history.history["accuracy"], 'tab:orange', label = 'Training Accuracy');
  ax1.plot(model_history.history["val_accuracy"], 'tab:pink', label = 'Validation Accuracy');
  ax1.title.set_text('Accuracy & Validation Accuracy')
  ax1.set_xlabel('Epoch');
  ax1.legend()
  ax2.plot(model_history.history["loss"], 'tab:olive', label = 'Training Loss');
  ax2.plot(model_history.history["val_loss"], 'tab:cyan', label = 'Validation Loss');
  ax2.title.set_text('Loss & Validation Loss') ax2.set_xlabel('Epoch');
  ax2.legend()
  
  fig.suptitle('Training history', size=20);
  
  plt.savefig(f"{figname}.PNG")
  plt.show()
