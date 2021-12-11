{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "forward_net.py",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "17BLDC7bt6fdg5lONvbhV1kgM2Mcj_lF1",
      "authorship_tag": "ABX9TyPzkYrQmru+UOajJWbepb8d",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shinneko/180722_firsttry/blob/master/modules/forward_net.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lh37hkNCNEWH"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "class Sigmoid:\n",
        "  def __init__(self):\n",
        "    self.params = []\n",
        "\n",
        "  def forward(self,x):\n",
        "    return 1/(1+np.exp(-x))\n",
        "\n",
        "class Affine:\n",
        "  def __init__(self, W, b):\n",
        "    self.params = [W, b]\n",
        "\n",
        "  def forward(self, x):\n",
        "    W, b = self.params\n",
        "    out = np.dot(x,W) + b\n",
        "    return out"
      ]
    }
  ]
}