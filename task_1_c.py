
def count_words(input_file, output_file):
    try:
    
        with open(input_file, 'r') as file:
            text = file.read()
        
    
        word_count = len(text.split())

    
        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}\n")

        print(f"Word count has been written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

input_file = "input.txt"
output_file = "output.txt"

count_words(input_file, output_file)
