{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NidhaK/ICT-academy/blob/main/data_preprocessing.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "_uuid": "674378297bf7f78937a4f1aa466932e68466efcd",
        "id": "4La4w4kJEMSs"
      },
      "cell_type": "markdown",
      "source": [
        "### Data Pre-processing Stage\n",
        "\n",
        "  This notebook contains the basic data pre processing steps.\n",
        "  * Preprocessing refers to the transformations applied to the data before feeding it to the machine learning algorithms.\n",
        "  * The data gathered from different sources is collected in raw format which is not feasible for the analysis.\n",
        "  * Data Preprocessing technique is used to convert the raw data into a clean data set."
      ]
    },
    {
      "metadata": {
        "_uuid": "fe10f16ae89b1e2579469abba5542de59d18ca7d",
        "id": "TWNqU20HEMSu"
      },
      "cell_type": "markdown",
      "source": [
        "#### Why preprocessing ?\n",
        "1. Real world data are generally\n",
        "    * Incomplete: lacking attribute values, lacking certain attributes of interest, or containing only aggregate data.\n",
        "    * Noisy: containing errors or outliers.\n",
        "    * Inconsistent: containing discrepancies in codes or names."
      ]
    },
    {
      "metadata": {
        "_uuid": "a30f7f7e2a855e2f0ef0bfc096bd4cc61a3399d9",
        "id": "UwPYZ8ZoEMSu"
      },
      "cell_type": "markdown",
      "source": [
        "Let's take a sample dataset for this exercise.\n",
        "This dataset named \"data.csv\" contains whether a user purchased the product or not.\n",
        "The users data has age,salary and the country they belonged to."
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "3ed37978d39bc4b4497ed16fd66a99a40df07561",
        "id": "oZQ4xVnCEMSu"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 1 : Importing the libraries                      #\n",
        "###############################################################\n",
        "\n",
        "\n",
        "# NumPy is module for Python. The name is an acronym for \"Numeric Python\" or \"Numerical Python\".\n",
        "# This makes sure that the precompiled mathematical and numerical functions\n",
        "# and functionalities of Numpy guarantee great execution speed.\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "# Pandas is an open-source Python Library providing high-performance data manipulation\n",
        "# and analysis tool using its powerful data structures.\n",
        "# The name Pandas is derived from the word Panel Data – an Econometrics from Multidimensional data.\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# The OS module in Python provides a way of using operating system dependent functionality.\n",
        "# The functions that the OS module provides allows you to interface with the underlying operating system\n",
        "# that Python is running on – be that Windows, Mac or Linux.\n",
        "\n",
        "import os"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "d09edc61b5ef258b23b6de01c4745613a4d00eca",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NQKA1fhQEMSv",
        "outputId": "224158ef-3105-47b4-d70e-90b2610bcbb1"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 2 : Importing the Dataset                        #\n",
        "###############################################################\n",
        "\n",
        "#Read the 'Data.csv' and store the data in the vairable dataset.\n",
        "dataset = pd.read_csv(\"/preprocessing_data.csv\")\n",
        "\n",
        "print('Load the datasets...')\n",
        "\n",
        "\n",
        "# Print the shape of the dataset\n",
        "print ('dataset: %s'%(str(dataset.shape)))\n"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Load the datasets...\n",
            "dataset: (15, 4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4IfQ5azLeaEy",
        "outputId": "769b3904-3494-4c62-8196-a7035bcf32d2"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "f2255fd0287097870845b0b4dbfd4e4ac04ea9f9",
        "id": "xD9z5ITdEMSv"
      },
      "cell_type": "markdown",
      "source": [
        "The dataset contains 15 rows and 4 columns"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2764bded9c4328f4ca9902a333d882b12d09223e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 519
        },
        "id": "znDiM5zkEMSv",
        "outputId": "837ccfc6-9b81-49dd-d464-8ddb5374d600"
      },
      "cell_type": "code",
      "source": [
        "# print the dataset\n",
        "dataset"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Country   Age   Salary Purchased\n",
              "0       India  34.0  92000.0       Yes\n",
              "1   Sri lanka  22.0  25000.0       Yes\n",
              "2       China  31.0  74000.0       Yes\n",
              "3   Sri lanka  29.0      NaN        No\n",
              "4       China  55.0  98000.0       Yes\n",
              "5       India  24.0  30000.0        No\n",
              "6   Sri lanka  28.0  40000.0        No\n",
              "7       India   NaN  60000.0        No\n",
              "8       China  51.0  89000.0       Yes\n",
              "9       India  44.0  78000.0       Yes\n",
              "10  Sri lanka  21.0  20000.0        No\n",
              "11      China  25.0  30000.0       Yes\n",
              "12      India  33.0  45000.0       Yes\n",
              "13      India  42.0  65000.0       Yes\n",
              "14  Sri lanka  33.0  22000.0        No"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b6121abf-9227-4735-8093-e963c328702f\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>Age</th>\n",
              "      <th>Salary</th>\n",
              "      <th>Purchased</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>India</td>\n",
              "      <td>34.0</td>\n",
              "      <td>92000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>22.0</td>\n",
              "      <td>25000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>China</td>\n",
              "      <td>31.0</td>\n",
              "      <td>74000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>29.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>China</td>\n",
              "      <td>55.0</td>\n",
              "      <td>98000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>India</td>\n",
              "      <td>24.0</td>\n",
              "      <td>30000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>28.0</td>\n",
              "      <td>40000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>India</td>\n",
              "      <td>NaN</td>\n",
              "      <td>60000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>China</td>\n",
              "      <td>51.0</td>\n",
              "      <td>89000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>India</td>\n",
              "      <td>44.0</td>\n",
              "      <td>78000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>21.0</td>\n",
              "      <td>20000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>China</td>\n",
              "      <td>25.0</td>\n",
              "      <td>30000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>India</td>\n",
              "      <td>33.0</td>\n",
              "      <td>45000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>India</td>\n",
              "      <td>42.0</td>\n",
              "      <td>65000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>33.0</td>\n",
              "      <td>22000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b6121abf-9227-4735-8093-e963c328702f')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-b6121abf-9227-4735-8093-e963c328702f button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-b6121abf-9227-4735-8093-e963c328702f');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-81dab2ca-5212-470c-9e0f-304fb1b5a878\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-81dab2ca-5212-470c-9e0f-304fb1b5a878')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-81dab2ca-5212-470c-9e0f-304fb1b5a878 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_1a8d16f1-e6c2-485d-beec-7a77b949327f\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('dataset')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_1a8d16f1-e6c2-485d-beec-7a77b949327f button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('dataset');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "dataset",
              "summary": "{\n  \"name\": \"dataset\",\n  \"rows\": 15,\n  \"fields\": [\n    {\n      \"column\": \"Country\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"India\",\n          \"Sri lanka\",\n          \"China\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 10.593383794604076,\n        \"min\": 21.0,\n        \"max\": 55.0,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          33.0,\n          21.0,\n          34.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Salary\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 27980.36988499435,\n        \"min\": 20000.0,\n        \"max\": 98000.0,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          65000.0,\n          20000.0,\n          92000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Purchased\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "0b51a61e0f0b243b1b3c5650a30dcf02d6f943a5",
        "id": "RkLDGgAwEMSv"
      },
      "cell_type": "code",
      "source": [
        "# Separate the dependent and independent variables\n",
        "\n",
        "# Independent variable\n",
        "# iloc[rows,columns]\n",
        "# Take all rows\n",
        "# Take last but one column from the dataset (:-1)\n",
        "X = dataset.iloc[:,:-1].values\n",
        "\n",
        "# Dependent variable\n",
        "# iloc[rows,columns]\n",
        "# Take all rows\n",
        "# Take last column from the dataset (:-1)\n",
        "Y = dataset.iloc[:,3].values"
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5351fbd6905b93aad9c455ee99cb0814e55cfc58",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OvPKIYQDEMSv",
        "outputId": "7168c65a-4cac-400f-b35e-4bf1468518bb"
      },
      "cell_type": "code",
      "source": [
        "# Print the X and Y\n",
        "print ('X: %s'%(str(X)))\n",
        "print ('-----------------------------------')\n",
        "print ('Y: %s'%(str(Y)))"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "X: [['India' 34.0 92000.0]\n",
            " ['Sri lanka' 22.0 25000.0]\n",
            " ['China' 31.0 74000.0]\n",
            " ['Sri lanka' 29.0 nan]\n",
            " ['China' 55.0 98000.0]\n",
            " ['India' 24.0 30000.0]\n",
            " ['Sri lanka' 28.0 40000.0]\n",
            " ['India' nan 60000.0]\n",
            " ['China' 51.0 89000.0]\n",
            " ['India' 44.0 78000.0]\n",
            " ['Sri lanka' 21.0 20000.0]\n",
            " ['China' 25.0 30000.0]\n",
            " ['India' 33.0 45000.0]\n",
            " ['India' 42.0 65000.0]\n",
            " ['Sri lanka' 33.0 22000.0]]\n",
            "-----------------------------------\n",
            "Y: ['Yes' 'Yes' 'Yes' 'No' 'Yes' 'No' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'Yes'\n",
            " 'Yes' 'No']\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "dffee0eb70165f04561442a9f05bf2fd0c0d205f",
        "id": "3nTd6mphEMSw"
      },
      "cell_type": "markdown",
      "source": [
        "#### 1. Handle Missing Data\n",
        "\n",
        "There are few missing data in the Age and salary columns (NaN values).\n",
        "\n",
        "#### i. Deleting Rows:\n",
        "*      We cannot remove the rows with the missing data as it will affect the output of the  machine learning algorithm.\n",
        "*      However we can delete a particular row if it has a null value for a particular feature and a particular column if it has more than 70-75% of missing values.\n",
        "      \n",
        "\n",
        "#### ii. Replacing With Mean/Median/Mode:\n",
        "*      This strategy can be applied on a feature which has numeric data like the age of a person.\n",
        "*      We can calculate the mean, median or mode of the feature and replace it with the missing values.    \n",
        "*     The loss of the data can be negated by this method which yields better results compared to removal of rows and  \n",
        "*       columns.\n",
        "*      Replacing with the above three approximations are a statistical approach of handling the missing values.\n",
        "*     This method is also called as leaking the data while training.\n",
        "*     Another way is to approximate it with the deviation of neighbouring values.\n",
        "*     This works better if the data is linear.\n"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "bc0f9fc1fde9aff85963ee3db02f1fd943d01d93",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HvBAeIXaEMSw",
        "outputId": "03719185-08ca-4876-cca8-16c86f3e03d5"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 3 : Missing Data                                 #\n",
        "###############################################################\n",
        "\n",
        "# Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface in Python.\n",
        "# The sklearn.preprocessing package provides several common utility functions and transformer classes\n",
        "# to change raw feature vectors into a representation that is more suitable for the downstream estimators\n",
        "\n",
        "\n",
        "from sklearn.impute import  SimpleImputer\n",
        "\n",
        "# Imputer Class takes the follwing parameters:\n",
        "#     missing_values : The missing values in our dataset are called as NaN (Not a number).Default is NaN\n",
        "#     strategy       : replace the missing values by mean/median/mode. Default is mean.\n",
        "#     axis           : if axis = 0, we take we of the column and if axis = 1, we take mean value of row.\n",
        "\n",
        "imputer =SimpleImputer(missing_values =np.NaN,strategy = 'mean', fill_value=None,verbose=0,copy=True)\n",
        "\n",
        "# Fit the imputer on X.\n",
        "# Take all rows and columns only with the missing values.\n",
        "# Note: Index starts with 0. Upper bound (3) is not included.\n",
        "\n",
        "# Fit imputer for columns 1 and 2 of X matrix.\n",
        "imputer = imputer.fit(X[:,1:3])\n",
        "\n",
        "#Replace missing data with mean of column\n",
        "X[:,1:3] = imputer.transform(X[:,1:3])\n"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/impute/_base.py:382: FutureWarning: The 'verbose' parameter was deprecated in version 1.1 and will be removed in 1.3. A warning will always be raised upon the removal of empty columns in the future version.\n",
            "  # By default, fill_value=None, and the replacement is always\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "cbb90e1ca86164287023c7fc38197bf087e0ef0e",
        "id": "pgWxPnG1EMSw"
      },
      "cell_type": "code",
      "source": [
        "print ('X: %s'%(str(X)))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "e06044bf541de146377c72fe4f34eb83100c2f49",
        "id": "PbleK7MvEMSw"
      },
      "cell_type": "markdown",
      "source": [
        "* Mean Value of Age    = Sum of all age values /14   = 33.714285714285715\n",
        "* Mean Value of Salary = Sum of all Salary value /14 = 54857.142857142855"
      ]
    },
    {
      "metadata": {
        "_uuid": "0504a7e75bde4ac7779062a37f144d9b9a096a17",
        "id": "jIpscFh3EMSw"
      },
      "cell_type": "markdown",
      "source": [
        "#### 2. Encode the Categorical data\n",
        "\n",
        "Categorical data are variables that contain label values rather than numeric values.\n",
        "Some algorithms can work with categorical data directly.\n",
        "\n",
        "For example, a decision tree can be learned directly from categorical data with no data transform required (this depends on the specific implementation).\n",
        "\n",
        "Many machine learning algorithms cannot operate on label data directly. They require all input variables and output variables to be numeric.\n",
        "\n",
        "This means that categorical data must be converted to a numerical form."
      ]
    },
    {
      "metadata": {
        "_uuid": "a8261920df0d266e0551cdae8264a07c96cdd7f8",
        "id": "QViKTpJ9EMSw"
      },
      "cell_type": "markdown",
      "source": [
        "In our dataset there are 2 columns with categorical data.\n",
        "\n",
        "The First column which contains the country and the last column purchased."
      ]
    },
    {
      "metadata": {
        "_uuid": "28a61d344d1556bdac352ac69e2ed0eb0e9a0cbc",
        "id": "7wKidr9AEMSw"
      },
      "cell_type": "markdown",
      "source": [
        "#### i.  Label Encoder:\n",
        "\n",
        "    * It is used to transform non-numerical labels to numerical labels (or nominal categorical variables).\n",
        "    * Numerical labels are always between 0 and n_classes-1.     \n",
        "\n",
        "#### ii. OneHotEncoder:\n",
        "    * Encode categorical integer features using a one-hot aka one-of-K scheme.\n",
        "    * The input to this transformer should be a matrix of integers, denoting the values taken on by categorical (discrete)\n",
        "      features.\n",
        "    * The output will be a sparse matrix where each column corresponds to one possible value of one feature.\n",
        "    * It is assumed that input features take on values in the range [0, n_values]\n",
        "    * This encoding is needed for feeding categorical data to many scikit-learn estimators, notably linear models and SVMs\n",
        "      with the standard kernels.        "
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "ad860887b31ba69dfe706ccd320b9cebe4fe931b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Oqu3kxxdEMSw",
        "outputId": "f9d375b8-2a60-4439-f28b-fb4cc49c736a"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 4 : Categorical variables                        #\n",
        "###############################################################\n",
        "\n",
        "from sklearn.preprocessing import LabelEncoder,OneHotEncoder\n",
        "\n",
        "labelencoder_X = LabelEncoder()\n",
        "X[:,0] = labelencoder_X.fit_transform(X[:,0])\n",
        "X[:,0]"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 1, 1, 2], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "5f745a4a68c5e1d90dc1537940af301e69d9c164",
        "id": "vms_8CWlEMSw"
      },
      "cell_type": "markdown",
      "source": [
        "Now the categorical data of the country value is changed to numerical value.\n",
        "\n",
        "| Country | Value |\n",
        "|:--------|:------|\n",
        "| China   |   0   |  \n",
        "| India   |   1   |   \n",
        "| Srilanka|   2   |   \n"
      ]
    },
    {
      "metadata": {
        "_uuid": "9c4a6e53a3a028c11f1d9a91b9f45fbf8c64c996",
        "id": "LuL-vdxsEMSw"
      },
      "cell_type": "markdown",
      "source": [
        "#### Dummy Encoding\n",
        "\n",
        "    * The above encoding will result in a problem.\n",
        "    * The label encoding transforms the data as shown in the table above.\n",
        "    * The Machine learning algorithm will assume that China>India>Sri Lanka.\n",
        "    * But this is not the case. We just converted the categorical value and assigned it to a numeric value.\n",
        "    * Hence there is a need to apply Dummy encoding to the above dataset.\n",
        "\n",
        "| Country | China | India | Sri Lanka |\n",
        "|:--------|:------|:------|:----------|\n",
        "| China   |   1   |  0    |    0      |   \n",
        "| India   |   0   |  1    |    0      |   \n",
        "| Srilanka|   0   |  0    |    1      |   \n",
        "| India   |   0   |  1    |    0      |  \n",
        "| Srilanka|   0   |  0    |    1      |  \n",
        "| China   |   1   |  0    |    0      |  \n",
        "  \n",
        "\n"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2594e6f27a4b8a3fda17c7def917c1884546bae1",
        "id": "YscnzErJEMSx"
      },
      "cell_type": "code",
      "source": [
        "# Applying the OneHotEncoder to the first column[0]\n",
        "onhotencoder = OneHotEncoder()\n",
        "X=X.reshape(-1,1)\n",
        "X=onhotencoder.fit_transform(X).toarray()\n"
      ],
      "execution_count": 33,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "614c26108b7dcd141f65bf14b67e178aee962f19",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JeZDybScEMSx",
        "outputId": "ff88fcc5-6b93-4b3b-cfb3-e3f864c1cf77"
      },
      "cell_type": "code",
      "source": [
        "# Encoding the categorical data for Y matrix\n",
        "labelencoder_Y = LabelEncoder()\n",
        "Y = labelencoder_X.fit_transform(Y)\n",
        "Y"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0])"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "19b3d19ab1e4b1c1ff425d55b0eb79317bf7ab86",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 373
        },
        "id": "oe2jg_nGEMSx",
        "outputId": "0f357e83-9a76-4976-d2ad-e264e8b63e05"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 5 : Splitting the dataset                        #\n",
        "############################################################\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# The test size is taken as 20% of the total dataset i.e., out of 15 only 3 rows are taken as test set\n",
        "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "Found input variables with inconsistent numbers of samples: [45, 15]",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-42-8c5fba6d49ab>\u001b[0m in \u001b[0;36m<cell line: 7>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;31m# The test size is taken as 20% of the total dataset i.e., out of 15 only 3 rows are taken as test set\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mX_train\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mX_test\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mY_train\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mY_test\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtrain_test_split\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mY\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtest_size\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0.2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mrandom_state\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/model_selection/_split.py\u001b[0m in \u001b[0;36mtrain_test_split\u001b[0;34m(test_size, train_size, random_state, shuffle, stratify, *arrays)\u001b[0m\n\u001b[1;32m   2557\u001b[0m         \u001b[0;34m\"stratify\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m\"array-like\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2558\u001b[0m     },\n\u001b[0;32m-> 2559\u001b[0;31m     \u001b[0mprefer_skip_nested_validation\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2560\u001b[0m )\n\u001b[1;32m   2561\u001b[0m def train_test_split(\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mindexable\u001b[0;34m(*iterables)\u001b[0m\n\u001b[1;32m    441\u001b[0m     \u001b[0mParameters\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    442\u001b[0m     \u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 443\u001b[0;31m     \u001b[0;34m*\u001b[0m\u001b[0marrays\u001b[0m \u001b[0;34m:\u001b[0m \u001b[0mlist\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mtuple\u001b[0m \u001b[0mof\u001b[0m \u001b[0minput\u001b[0m \u001b[0mobjects\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    444\u001b[0m         \u001b[0mObjects\u001b[0m \u001b[0mthat\u001b[0m \u001b[0mwill\u001b[0m \u001b[0mbe\u001b[0m \u001b[0mchecked\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mconsistent\u001b[0m \u001b[0mlength\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    445\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mcheck_consistent_length\u001b[0;34m(*arrays)\u001b[0m\n\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mcheck_memory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmemory\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 397\u001b[0;31m     \"\"\"Check that ``memory`` is joblib.Memory-like.\n\u001b[0m\u001b[1;32m    398\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    399\u001b[0m     \u001b[0mjoblib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mMemory\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mlike\u001b[0m \u001b[0mmeans\u001b[0m \u001b[0mthat\u001b[0m\u001b[0;31m \u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0mmemory\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m \u001b[0mcan\u001b[0m \u001b[0mbe\u001b[0m \u001b[0mconverted\u001b[0m \u001b[0minto\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: Found input variables with inconsistent numbers of samples: [45, 15]"
          ]
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "780861983da7a12d75a1a3c7e6e03a1602d41c07",
        "scrolled": true,
        "id": "8sRO-kpeEMSx"
      },
      "cell_type": "code",
      "source": [
        "# Print the shape of the dataset\n",
        "print ('X_train: %s'%(str(X_train.shape)))\n",
        "print ('----------------')\n",
        "print ('X_test: %s'%(str(X_test.shape)))\n",
        "print ('----------------')\n",
        "print ('Y_train: %s'%(str(Y_train.shape)))\n",
        "print ('----------------')\n",
        "print ('Y_test: %s'%(str(Y_test.shape)))\n",
        "print ('----------------')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "0ef42f4efa7b7ed1f21966153a9a0de7a14d1d2e",
        "id": "otylLu6KEMSx"
      },
      "cell_type": "markdown",
      "source": [
        "#### 3. Scale your Features\n",
        "    *  Most of the times, the dataset will contain features highly varying in magnitudes, units and range.\n",
        "    *  Since the machine learning algorithms use Eucledian distance between two data points in their computations, this is\n",
        "       result in wrong prediction.\n",
        "      \n",
        "We need to put the variables in same range, in the same scale so that no variable dominates the other variable.     \n",
        "      \n",
        "      "
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "d7b0722d744c2da299c42cc2b6e50f6a21a87d20",
        "id": "wt2ZyXxJEMSx"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 6 : Feature Scaling                              #\n",
        "###############################################################\n",
        "\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "sc_X = StandardScaler()\n",
        "\n",
        "# We need to fit and transform the training set\n",
        "X_train = sc_X.fit_transform(X_train)\n",
        "\n",
        "# We need to fit the test set\n",
        "X_test = sc_X.transform(X_test)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "19edd09629c93a036a69dbb5adc2fa526c1403db",
        "id": "twd4xeW4EMSx"
      },
      "cell_type": "code",
      "source": [
        "X_train"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "047b9e920be562717de782098c416e0bcc6e9bd5",
        "id": "FV9n5poqEMSy"
      },
      "cell_type": "code",
      "source": [
        "X_test"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "d884daf43f80af5c65844fbc763ea18c738890ec",
        "id": "GSzHr4wpEMSy"
      },
      "cell_type": "markdown",
      "source": [
        "Now the all the data are in same scale. We can now apply different Machine learning model to the dataset."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.6.6",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}