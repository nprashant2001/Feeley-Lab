import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#THE PURPOSE OF THIS PROGRAM IS TO TAKE A CSV OF UNANALYZED DATA AND CREATE A BOXPLOT FROM IT
#PROS: ITS FREE AND FAST, PRISM ISNT
#CONS: NO SIGNIFICANCE BARS(WORKING ON IT), CSV FILE HAS TO BE FORMATTED AND NAMED A CERTAIN WAY
#ANYONE WITH CODING EXP, FEEL FREE TO EDIT AND MAKE BETTER

class Plot:
    def __init__(self, csv, stain, title, x, y, hue, laminin):
        self.csv = csv
        self.stain = stain
        self.title = title
        self.x = x
        self.y = y
        self.hue = hue
        self.laminin = laminin

        data = pd.read_csv(self.csv)
        df = pd.DataFrame(data)
        if self.laminin == "N":
            df['percent'] = df[self.stain] / df['area'] * 100
        sns.set(style="ticks")
        sns.boxplot(x=self.x, y=self.y, hue=self.hue, data=df, palette='Set1', width=1).set_title(self.title)
        plt.show()




Plot()

    #components: Plot('csv file path', 'measured pixels', 'chart title', 'x-axis', 'y-axis', 'sub-component', 'is this a laminin stain? Y/N')

    # Trichrome example: Plot('/Users/prashantn/Downloads/Trichrome.csv', 'blue', 'Fibrosis Index', 'group', 'percent', 'side', 'N')

    #ensure you have ALL components or IT WILL NOT WORK
    
