import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Plot all reaction times for a participant in a session
    df1=pd.read_csv('Mohsen Kabirian_abm_2023-02-17_14h47.24.019.csv')
    df1['RTms'].plot(xlabel='Stimulus Index',ylabel='Reaction Time(ms)')
    plt.show()
    
    