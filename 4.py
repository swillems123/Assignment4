def read_column_15(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Initialize variables
            in_quotes = False
            current_column = ""
            columns = []
            
            # Manually parse the line, character by character
            for char in line:
                if char == '"':  # Toggle the in_quotes flag when encountering quotes
                    in_quotes = not in_quotes
                elif char == ',' and not in_quotes:  # Only split if not inside quotes
                    columns.append(current_column.strip())
                    current_column = ""
                else:
                    current_column += char
            
            # Add the last column (since there's no comma at the end of the line)
            columns.append(current_column.strip())

            # Ensure the line has at least 15 columns
            if len(columns) >= 15:
                # Convert the 15th column to a float and print it if it's >= 9
                try:
                    value = float(columns[14])
                    if value >= 9:
                        print(value)
                except ValueError:
                    print("Non-float value in column 15")
            else:
                print("Row does not have 15 columns")

# Example usage with your provided path
read_column_15(r'C:\Projects\4\toprankedanime.csv')

