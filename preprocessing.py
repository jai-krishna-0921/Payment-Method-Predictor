import pandas as pd
import numpy as np

original_file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\data.xlsx'

def preprocess_data(df):
    def update_average(value):
        try:
            # Check if it's a range (e.g., '100-150')
            parts = value.split('-')
            if len(parts) == 2:
                return int(parts[1])
            # If not a range, it's already numeric, convert it
            return int(value)
        except:
            return None

    # Update the 'average amount spent' column
    df['average amount spent'] = df['average amount spent'].apply(update_average)

    # Change 'UPI (digital payment)' to 'UPI' in 
    df['how they make payments'] = df['how they make payments'].replace('UPI (digital payment)', 'UPI')

    if 'Timestamp' in df:
        df.drop(columns=['Timestamp'], inplace=True)

    # Remove rows without values in the "enter your name" column
    df = df.dropna(subset=["name"])

    df = df.drop_duplicates(subset=["name"], keep=False)

    # Map values in specific columns
    column_mappings = {
        'gender': {'Male': 1, 'Female': 0, 'Prefer not to say': 0},
        'year of study': {
            'Btech 1st year': 1,
            'Btech 2nd year': 2,
            'Btech 3rd year': 3,
            'Btech 4th year': 4,
            'Mtech': 5,
            'PhD': 6,
        },
        'what time they purchase': {
            'Morning': 1,
            'Afternoon': 2,
            'Evening': 3,
            'Night': 4,
        },
        'how they make payments': {
            'Cash': 1,
            'UPI': 2,
        },
        'how they visit the stores' : {
            'Yes, we visit as a group of 2': 2,
            'Yes, we visit as a group of 3': 3,
            'Yes, we visit as a group of 4': 4,
            'Yes, we visit as a group of 5': 5,
            'Yes, we visit as a group of more than 5': 6,
            'No': 1,
        },
        'why they purchase at the department stores' : {
            'Just for eating snacks': 1,
            'Emergency purposes': 2,
            'Finds the pricing very affordable': 3,
            'Taste of eatables are good': 4,
            'Other': 5,
        }
    }

    # Perform one-hot encoding for the "what they purchase" column
    purchase_dummies = df['what they purchase'].str.get_dummies(sep=',')

    # Concatenate the one-hot encoded columns with the original DataFrame
    df = pd.concat([df, purchase_dummies], axis=1)

    # Drop the original "what they purchase" column
    df.drop(columns=['what they purchase'], inplace=True)

    df.replace(column_mappings, inplace=True)
    
    # range around which average will be generated
    std_deviation = 10  

    #generate proper average
    df['average amount spent'] = df['average amount spent'].apply(lambda avg_amount: round(np.random.normal(avg_amount, std_deviation)))
    
    df.drop(columns=[' chargers etc)'], inplace=True)

    return df

try:
    original_df = pd.read_excel(original_file_path)
    preprocessed_df = preprocess_data(original_df)

    # Remove rows with missing 'average amount spent' values   
    preprocessed_df = preprocessed_df.dropna(subset=['average amount spent'])

    # Save and create new excel
    updated_file_path = 'preprocessed_data.xlsx'
    preprocessed_df.to_excel(updated_file_path, index=False)
    print("Data preprocessing completed successfully.")

except FileNotFoundError:
    print(f"Original file not found at the specified path: {original_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
