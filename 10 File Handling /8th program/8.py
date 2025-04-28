# Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.

def remove_words(input_file, output_file):
    words_to_remove = ['a', 'the', 'an']

    try:
        with open("10 File hendling/8th/input.txt", 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                words = line.split()
                
                modified_line = ' '.join([word if word.lower() not in words_to_remove else '' for word in words])
                outfile.write(modified_line + '\n')

        print(f"Processed file saved as '{output_file}'.")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'input.txt'  
output_file = 'output.txt' 
remove_words(input_file, output_file)
