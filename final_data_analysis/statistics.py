import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro 
import scipy.stats as stats


if __name__ == "__main__":
    
    
    df1=pd.read_csv('average_RTVar_all.csv')
    # df1['RT_average_music'].plot(xlabel='id',ylabel='Reaction Time(ms)')
    
    #Check normality
    # print(shapiro(df1['RT_average_music']))
    # plt.hist(df1['RT_average_music'], edgecolor='black', bins=20)
    # plt.hist(df1['RTVar_music'], edgecolor='black', bins=20)
    # plt.show()
    
    #Paired t-test
    #For average
    print(stats.ttest_rel(df1['RT_average_music'], df1['RT_average_no_music']))
    #for RTVar
    print(stats.ttest_rel(df1['RTVar_music'], df1['RTVar_no_music']))
    
    #plot data
    plt.title("Reaction time average")
    df1['RT_average_music'].plot(xlabel='id',ylabel='Reaction Time(ms)',label = 'Music')
    df1['RT_average_no_music'].plot(xlabel='id',ylabel='Reaction Time(ms)', label = 'No Music')
    plt.legend()
    plt.show()
    
    plt.title("RTVar (Reaction time variation)")
    df1['RTVar_music'].plot(xlabel='id',ylabel='Reaction Time(ms)',label = 'Music')
    df1['RTVar_no_music'].plot(xlabel='id',ylabel='RTVar(ms)', label = 'No Music')
    plt.legend()
    plt.show()
    
    
    
    

    
    
    

    