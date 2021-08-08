import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def trichrome_plot(data):
    df = pd.DataFrame(data)
    df['percent'] = df['blue']/df['area']*100
    sns.set(style="ticks")
    sns.boxplot(x='group', y='percent', hue='side', data= df, palette='Set1', width=1).set_title('Fibrosis Index')
    plt.show()

def oilredo_plot(data):
    df = pd.DataFrame(data)
    df['percent'] = df['red']/df['area']*100
    sns.set(style="ticks")
    sns.boxplot(x='group', y='percent', hue='side', data= df, palette='Set1', width=1).set_title('Fat Index')
    plt.show()

def laminin_plot(data):
    df = pd.DataFrame(data)
    sns.set(style="ticks")
    sns.boxplot(x='group', y='area', hue='side', data= df, palette='Set1', width=1).set_title('Fiber Size')
    plt.show()

def ucp1_plot(data):
    df = pd.DataFrame(data)
    df['percent'] = df['ucp1']/df['area']*100
    sns.set(style="ticks")
    sns.boxplot(x='group', y='percent', hue='side', data= df, palette='Set1', width=1).set_title('UCP1')
    plt.show()

def cd31_plot(data):
    df = pd.DataFrame(data)
    df['percent'] = df['cd31']/df['area']*100
    sns.set(style="ticks")
    sns.boxplot(x='group', y='percent', hue='side', data= df, palette='Set1', width=1).set_title('CD31')
    plt.show()

data = pd.read_csv('')
