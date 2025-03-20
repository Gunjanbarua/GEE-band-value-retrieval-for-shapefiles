import pandas as pd
import numpy as np

def reorganize_timeseries_data(input_file, output_file):
    """
    Reorganizes a multi-temporal dataset to have one row per feature. I am using plot_ID as the index and pivoting the data based on the date. 

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        df = pd.read_csv(input_file)

        # Convert 'date' to datetime objects
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m')

        # Sort by plot_ID and date
        df = df.sort_values(['plot_ID', 'date'])

        # Identify columns to pivot (all except plot_ID and date)
        cols_to_pivot = [col for col in df.columns if col not in ['plot_ID', 'date']]

        # Create a dictionary to store the reshaped data
        reshaped_data = {}

        # Iterate over unique plot_IDs
        for plot_id in df['plot_ID'].unique():
            plot_df = df[df['plot_ID'] == plot_id]

            # Initialize the row for this plot_ID
            reshaped_data.setdefault(plot_id, {'plot_ID': plot_id})

            # Pivot the data
            for col in cols_to_pivot:
                for _, row in plot_df.iterrows():  # Iterate through rows
                    date_str = row['date'].strftime('%Y_%m')  # Format: yyyy_mm
                    new_col_name = f"{col}_{date_str}"
                    reshaped_data[plot_id][new_col_name] = row[col]

        # Convert the dictionary to a DataFrame
        output_df = pd.DataFrame.from_dict(reshaped_data, orient='index')
        output_df = output_df.reset_index(drop=True)

        # Save to CSV
        output_df.to_csv(output_file, index=False)
        print(f"Reorganized data saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
    except pd.errors.EmptyDataError:
        print(f"Error: Input file is empty: {input_file}")
    except KeyError as e:
        print(f"Error: Required column missing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_csv = 'inpute_file.csv'  #  Example input (modify as needed)
    output_csv = 'output_file.csv'     #  Example output

    reorganize_timeseries_data(input_csv, output_csv)

if __name__ == '__main__':
    main()