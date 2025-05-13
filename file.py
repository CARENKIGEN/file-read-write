def process_file():
    """
    Reads a file, modifies its content, and writes it to a new file.
    Includes comprehensive error handling.
    """
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read {len(content)} characters from {input_filename}")
            
            # Ask user how they want to modify the content
            print("\nHow would you like to modify the content?")
            print("1. Convert to uppercase")
            print("2. Convert to lowercase")
            print("3. Add line numbers")
            print("4. Replace a word")
            
            choice = input("Enter your choice (1-4): ")
            
            # Modify content based on user choice
            if choice == '1':
                modified_content = content.upper()
                modification_type = "uppercase"
            elif choice == '2':
                modified_content = content.lower()
                modification_type = "lowercase"
            elif choice == '3':
                lines = content.split('\n')
                modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
                modification_type = "line numbers added"
            elif choice == '4':
                word_to_replace = input("Enter word to replace: ")
                replacement_word = input("Enter replacement word: ")
                modified_content = content.replace(word_to_replace, replacement_word)
                modification_type = f"replaced '{word_to_replace}' with '{replacement_word}'"
            else:
                print("Invalid choice. No modification will be made.")
                modified_content = content
                modification_type = "no modification"
            
            # Ask user for output filename
            output_filename = input("Enter the name for the output file: ")
            
            # Write the modified content to the output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                    print(f"\nSuccess! Content ({modification_type}) written to {output_filename}")
            except IOError as e:
                print(f"Error writing to file {output_filename}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred while writing: {e}")
                
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{input_filename}'. It might be a binary file.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("File Read & Write Challenge")
    print("==========================")
    
    continue_program = True
    while continue_program:
        process_file()
        
        # Ask if the user wants to process another file
        response = input("\nDo you want to process another file? (y/n): ").lower()
        continue_program = response == 'y' or response == 'yes'
    
    print("Thank you for using the File Read & Write program!")