The new quantum weapons developed by the weapon laboratory are stored in the manufactory.csv file. This file stores the following information:

Weapon_id: The ID of the weapon being produced;
Weapon_model: The model of the weapon being produced;
Factory: The ID of the factory producing the weapon;
Staff_id: The ID of the staff in charge of producing the weapon;
The quality testing data for the weapons conducted by the laboratory is stored in the experiment.csv file. The data stored in this file is as follows:

ID: The ID of the testing experiment;
Weapen: The ID of the weapon being tested;
Tester: The ID of the tester;
Damage: The test result data.
The Weapon_id in the manufactory.csv file corresponds to the Weapen in the experiment.csv file.

The task of this challenge is to implement the combine_files() method in the combine_files.py file to merge the two CSV files into a new report.csv file.


import csv
import json
import pandas as pd
from collections import Counter

def combine_files():
     try:
        # Load the CSV files
        manufactory_df = pd.read_csv("manufactory.csv")
        experiment_df = pd.read_csv("experiment.csv")
        
        # Merge the data on Weapon_id (manufactory) and Weapen (experiment)
        merged_df = manufactory_df.merge(experiment_df, left_on="Weapon_id", right_on="Weapen", how="inner")
        
        # Drop duplicate weapon ID column from experiment.csv
        merged_df.drop(columns=["Weapen"], inplace=True)
        
        # Save to report.csv
        merged_df.to_csv("report.csv", index=False)
        print("report.csv has been successfully created.")
     except FileNotFoundError:
        print("One or more files not found. Please ensure both CSV files exist.")
     except pd.errors.EmptyDataError:
        print("One or more files are empty.")
     except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    combine_files()
########################################
manufactury.csv
###########################################
Weapon_id,Weapon_model,Factory,Staff_id
7196b564,Quantum_A_648a,Factory_I,10010046
480637b4,Quantum_A_f7ff,Factory_II,100103f3
4d03ccf1,Quantum_B_e90f,Factory_II,1001064a
bee4b9fa,Quantum_A_fc6c,Factory_III,10010595
16c7fba5,Quantum_A_df73,Factory_III,10010741


#############################################
experiment.csv
###############################################

ID,Weapen,Tester,Damage
222200001,7196b564,100102c2,29089
222200002,480637b4,10010715,29508
222200003,7196b564,10010040,44534
222200004,4d03ccf1,100100da,51700
222200005,bee4b9fa,10010307,88798
222200006,16c7fba5,100106cb,12530
222200007,4d03ccf1,1001025d,11472
222200008,16c7fba5,10010399,16441
222200009,bee4b9fa,10010742,81737
222200010,4d03ccf1,100100c7,13090
