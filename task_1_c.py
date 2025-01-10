# Function to read a file, count words, and write the result to a new file
def count_words(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Count the number of words
        word_count = len(text.split())

        # Write the word count to the output file
        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}\n")

        print(f"Word count has been written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

# Define input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Call the function
count_words(input_file, output_file)
