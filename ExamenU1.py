{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoVGTwH9nFTJvpTv1HpeCa",
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
        "<a href=\"https://colab.research.google.com/github/Aloverastegui/AV/blob/main/ExamenU1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Alumna: Alondra Vianey Verástegui Peña\n",
        "\n",
        "Materia: Protección de datos\n",
        "\n",
        "Carrera: Licenciatura en Ciencia de datos\n",
        "\n",
        "Semestre: 7°\n"
      ],
      "metadata": {
        "id": "4FhtAJHlgvNc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1."
      ],
      "metadata": {
        "id": "FEeKfO95iMHg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def serca_Prime (n):\n",
        "  if not Primo(n): return False\n",
        "  i = 0\n",
        "  while True:\n",
        "    i += 1\n",
        "    if Primo(n+i): return n+i\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  dato = serca_Prime(int(input(\"inserta numero: \")))\n",
        "\n",
        "  print(f\"El primo mas cercano es {dato}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3xfWhLWUgMOJ",
        "outputId": "d559181e-9c5e-4075-94b9-b75a0f05d1c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "inserta numero: 5\n",
            "El primo mas cercano es 7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2."
      ],
      "metadata": {
        "id": "cHM2Zh1miO1f"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def Primo(n):\n",
        "  if n < 2: return False\n",
        "  for i in range(2,int(n/2)+1):\n",
        "    if n % i == 0: return False\n",
        "  return True\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  dato = Primo(int(input(\"inserta numero: \")))\n",
        "  if dato:\n",
        "    print(\"es primo\")\n",
        "  else:\n",
        "    print(\"no es primo\")"
      ],
      "metadata": {
        "id": "6SVG0Hn7GOmp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ab359f50-3b0d-4c3b-a33a-b41c20325a1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "inserta numero: 5\n",
            "es primo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3."
      ],
      "metadata": {
        "id": "-y6thNYEiSAF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def median(datos):\n",
        "    mitad = len(datos) // 2\n",
        "    datos.sort()\n",
        "    return datos[mitad]\n",
        "\n",
        "\n",
        "a = float(input(\"ingresa primer valor: \"))\n",
        "b = float(input(\"ingresa segundo valor:\"))\n",
        "c = float(input(\"ingresa tercero valor:\"))\n",
        "lista=[a,b,c]\n",
        "print(median(lista))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a7ty6et6gWyK",
        "outputId": "7cd2d63d-e32f-4296-c1f1-4457a96ad7a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingresa primer valor: 5\n",
            "ingresa segundo valor:6\n",
            "ingresa tercero valor:7\n",
            "6.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4."
      ],
      "metadata": {
        "id": "hvkEMv8QiTlJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def contra():\n",
        "  contrasena = \"\"\n",
        "  for i in range(1,random.randrange(7,10)):\n",
        "    contrasena += chr(random.randrange(33,126,1))\n",
        "  return contrasena\n",
        "\n",
        "\n",
        "print(\"Contraseña generada: \",contra())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DbxY5pwxgfqp",
        "outputId": "d4067e4e-b6b3-4d00-dfae-0c0e389892c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contraseña generada:  k7t*KQU%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5."
      ],
      "metadata": {
        "id": "kSs0CmEbiVEO"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RgtYN13KFham",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8c079605-366a-41e2-a068-382cab480734"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingresa el primer valor: 5\n",
            "ingresa el primer valor: 4\n",
            "6.4031242374328485\n"
          ]
        }
      ],
      "source": [
        "def hipo (a,b):\n",
        "  return (a**2+b**2)**0.5\n",
        "\n",
        "\n",
        "a = float (input(\"ingresa el primer valor: \"))\n",
        "b = float (input(\"ingresa el primer valor: \"))\n",
        "resultado = hipo(a,b)\n",
        "print (resultado)"
      ]
    }
  ]
}