'''
import pandas as pd
SocialMediaMarket = pd.read_csv("social_media_4.csv")
AnxietyDisorderRates = pd.read_csv("prevalence-of-anxiety-disorders-males-vs-females.csv")

columns_to_keep = ['Date', 'Instagram']
SocialMediaMarket.drop(columns=[col for col in SocialMediaMarket.columns if col not in columns_to_keep]).to_csv('Insta_Market.csv', index=False)
columns_to_keep_anxiety = ['Entity', 'Year', 'Male_Prevalence', 'Female_Prevalence']
AnxietyDisorderRates.drop(columns=[col for col in AnxietyDisorderRates.columns if col not in columns_to_keep_anxiety]).to_csv('Anxiety_Rates.csv', index=False)
''' # ^ was done in a separate file

import pandas as pd

Anxiety_Rates = pd.read_csv("Anxiety_Rates.csv")
Insta_Market = pd.read_csv("Insta_Market.csv")

cleaned_Anxiety_Rates = Anxiety_Rates.dropna()
cleaned_Anxiety_Rates = cleaned_Anxiety_Rates[cleaned_Anxiety_Rates['Year'].isin([2016, 2017, 2018, 2019])].to_csv('cleaned_Anxiety_Rates.csv', index=False)
cleaned_Insta_Market = Insta_Market[Insta_Market['Instagram'] != 0].to_csv('cleaned_Insta_Market.csv', index=False)


def choosingCountry():
    print('Which country would you like to view statistics for (We don\'t have them all)')
    countryChosen = input('Type the country with a capital letter and spelt correctly.')

print('Welcome! This is a program that aims to illustrate the correlation between the rise of Instagram in the social media market, and the increase in rates of Anxiety.')
print('Would you like to continue with single plot mode, or dual plot mode? \nSingle plot mode generates a single graph for you to look at, while dual plot mode creates two so it is easy for you to compare the two.')
plotMode = input('Type \'1\' for Single, and \'2\' for Dual.')
if plotMode == '1':
    print('Single Plot mode selected.')
    choosingCountry()


