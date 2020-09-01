{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import style\n",
    "from collections import deque\n",
    "from time import sleep\n",
    "import pandas as pd\n",
    "from matplotlib.pyplot import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "style.use('ggplot')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "fps_counter = deque(maxlen=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "FPS = 105\n",
    "HM_SECONDS_SLICE = 500"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15360\n"
     ]
    }
   ],
   "source": [
    "data  = pd.read_csv(\"/home/cmn/BCI/EEGrunt/data/eegrunt-obci-ovibe-test-data.csv\").values\n",
    "print(len(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(FPS*HM_SECONDS_SLICE, len(data)):\n",
    "    new_data = data[i-FPS*HM_SECONDS_SLICE: i]\n",
    "    c4 = new_data[:,4]\n",
    "    \n",
    "    GRAPH = c4\n",
    "    print(c4)\n",
    "    sleep(1/FPS)\n",
    "    \n",
    "    plt.plot(c4)\n",
    "    show()\n",
    "    break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
