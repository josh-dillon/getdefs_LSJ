# Download the LSJ xml files here: https://github.com/helmadik/LSJLogeion
#
# Update the location of the files below (replace "/path/to/LSJ" with your directory
# in double quotation marks).
#
# Save a UTF-8 text file of Greek words, each on a new line, in the same directory
# as this script. Give it the name wordlist.txt.
#
# Run the script from Terminal ($ python3 getdefs_LSJ.py). Depending on the number of
# words in your list, the script may need some time to finish, so be patient.
#
# The script will create output.txt, a tab-delineated text file containing your words
# and their definitions provided it finds the relevant lemmata in the LSJ.
#
# Check definitions thoroughly. The script imports definitions only, no grammatical
# details like case, gender, tense or voice information.
#
# CREDITS: Perseus Tufts and the incomparable Helma Dik of Logeion.
#
# ERRORS: Please report LSJ errors here: https://logeion.uchicago.edu/ (click
# "Report a Problem" at top right-hand corner).

import xml.etree.ElementTree as ET
import unicodedata
import os
import re

# Function to extract text from <sense><i>...</i></sense> tags
def extract_senses(entry):
    senses = entry.findall(".//sense")
    sense_texts = []
    for sense in senses:
        i_tags = sense.findall(".//i")
        sense_text = ""
        if i_tags is not None:
            for i, i_tag in enumerate(i_tags):
                sense_text += i_tag.text
                if i_tag.tail is not None:  # Add this check
                    if i < len(i_tags) - 1:
                        if (" or " in i_tag.tail and i_tag.tail.strip().startswith("or")) \
                                or (", esp. " in i_tag.tail and i_tag.tail.strip().startswith(", esp.")):
                            sense_text += i_tag.tail
                        else:
                            sense_text += "; "
        sense_texts.append(sense_text.strip())
    return sense_texts


# Function to remove diacritics from vowels
def remove_diacritics(word):
    normalized_word = unicodedata.normalize('NFD', word)
    return ''.join(char for char in normalized_word if unicodedata.category(char) != 'Mn')

# Function to clean the output file
def clean_output_file(filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        
        # Replace ",;" with ";"
        content = re.sub(r',;', ';', content)
        
        # Replace ",\n" with "\n"
        content = re.sub(r',\n', '\n', content)
        
        # Loop until no more occurrences of "; \n" are found
        while re.search(r';\s*\n', content):
            # Replace "; \n" with "\n"
            content = re.sub(r';\s*\n', '\n', content)
        
        # Replace multiple semicolons with one semicolon and space until no more occurrences are found
        while re.search(r';\s*;+', content):
            content = re.sub(r';\s*;+', '; ', content)
        
        # Replace two or more spaces with a single space
        content = re.sub(r' {2,}', ' ', content)
        
        file.seek(0)
        file.write(content)
        file.truncate()

# Mapping between initial letters and corresponding XML files
file_mapping = {
    'α': ["/path/to/LSJ/greatscott02.xml",
          "/path/to/LSJ/greatscott03.xml",
          "/path/to/LSJ/greatscott04.xml",
          "/path/to/LSJ/greatscott05.xml",
          "/path/to/LSJ/greatscott06.xml",
          "/path/to/LSJ/greatscott07.xml",
          "/path/to/LSJ/greatscott08.xml",
          "/path/to/LSJ/greatscott09.xml",
          "/path/to/LSJ/greatscott10.xml",
          "/path/to/LSJ/greatscott11.xml"],
    'β': ["/path/to/LSJ/greatscott12.xml",
          "/path/to/LSJ/greatscott13.xml"],
    'γ': ["/path/to/LSJ/greatscott14.xml",
          "/path/to/LSJ/greatscott15.xml"],
    'δ': ["/path/to/LSJ/greatscott16.xml",
          "/path/to/LSJ/greatscott17.xml",
          "/path/to/LSJ/greatscott18.xml",
          "/path/to/LSJ/greatscott19.xml"],
    'ε': ["/path/to/LSJ/greatscott20.xml",
          "/path/to/LSJ/greatscott21.xml",
          "/path/to/LSJ/greatscott22.xml",
          "/path/to/LSJ/greatscott23.xml",
          "/path/to/LSJ/greatscott24.xml",
          "/path/to/LSJ/greatscott25.xml",
          "/path/to/LSJ/greatscott26.xml",
          "/path/to/LSJ/greatscott27.xml",
          "/path/to/LSJ/greatscott28.xml",
          "/path/to/LSJ/greatscott29.xml"],
    'ζ': ["/path/to/LSJ/greatscott31.xml"],
    'η': ["/path/to/LSJ/greatscott32.xml"],
    'θ': ["/path/to/LSJ/greatscott33.xml",
          "/path/to/LSJ/greatscott34.xml"],
    'ι': ["/path/to/LSJ/greatscott35.xml",
          "/path/to/LSJ/greatscott36.xml"],
    'κ': ["/path/to/LSJ/greatscott37.xml",
          "/path/to/LSJ/greatscott38.xml",
          "/path/to/LSJ/greatscott39.xml",
          "/path/to/LSJ/greatscott40.xml",
          "/path/to/LSJ/greatscott41.xml",
          "/path/to/LSJ/greatscott42.xml"],
    'λ': ["/path/to/LSJ/greatscott43.xml",
          "/path/to/LSJ/greatscott44.xml",
          "/path/to/LSJ/greatscott45.xml"],
    'μ': ["/path/to/LSJ/greatscott46.xml",
          "/path/to/LSJ/greatscott47.xml",
          "/path/to/LSJ/greatscott48.xml"],
    'ν': ["/path/to/LSJ/greatscott49.xml",
          "/path/to/LSJ/greatscott50.xml"],
    'ξ': ["/path/to/LSJ/greatscott51.xml"],
    'ο': ["/path/to/LSJ/greatscott52.xml",
          "/path/to/LSJ/greatscott53.xml",
          "/path/to/LSJ/greatscott54.xml",
          "/path/to/LSJ/greatscott55.xml"],
    'π': ["/path/to/LSJ/greatscott56.xml",
          "/path/to/LSJ/greatscott57.xml",
          "/path/to/LSJ/greatscott58.xml",
          "/path/to/LSJ/greatscott59.xml",
          "/path/to/LSJ/greatscott60.xml",
          "/path/to/LSJ/greatscott61.xml",
          "/path/to/LSJ/greatscott62.xml",
          "/path/to/LSJ/greatscott63.xml"],
    'ρ': ["/path/to/LSJ/greatscott66.xml",
          "/path/to/LSJ/greatscott67.xml"],
    'σ': ["/path/to/LSJ/greatscott68.xml",
          "/path/to/LSJ/greatscott69.xml",
          "/path/to/LSJ/greatscott70.xml",
          "/path/to/LSJ/greatscott71.xml",
          "/path/to/LSJ/greatscott72.xml",
          "/path/to/LSJ/greatscott73.xml"],
    'τ': ["/path/to/LSJ/greatscott74.xml",
          "/path/to/LSJ/greatscott75.xml",
          "/path/to/LSJ/greatscott76.xml"],
    'υ': ["/path/to/LSJ/greatscott77.xml",
          "/path/to/LSJ/greatscott78.xml"],
    'φ': ["/path/to/LSJ/greatscott79.xml",
          "/path/to/LSJ/greatscott80.xml",
          "/path/to/LSJ/greatscott81.xml"],
    'χ': ["/path/to/LSJ/greatscott82.xml",
          "/path/to/LSJ/greatscott83.xml"],
    'ψ': ["/path/to/LSJ/greatscott84.xml",
          "/path/to/LSJ/greatscott85.xml"],
    'ω': ["/path/to/LSJ/greatscott86.xml"],
}

# Main function
def main():
    with open('wordlist.txt', 'r', encoding='utf-8') as wordlist_file:
        words_to_lookup = [line.strip() for line in wordlist_file]

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for word_to_lookup in words_to_lookup:
            initial_letter = remove_diacritics(word_to_lookup[0]).lower()
            xml_files = file_mapping.get(initial_letter, [])
            found = False
            for xml_file_path in xml_files:
                try:
                    tree = ET.parse(xml_file_path)
                    root = tree.getroot()
                    for entry in root.findall(".//div2"):
                        if entry.find("head").text == word_to_lookup:
                            found = True
                            word = entry.find("head").text
                            senses = extract_senses(entry)
                            output_file.write(f"{word}\t{'; '.join(senses)}\n")
                            break
                    if found:
                        break
                except FileNotFoundError:
                    print(f"XML file {xml_file_path} not found.")
            if not found:
                print(f"{word_to_lookup} not found in {', '.join(xml_files)}")

    # Clean the output file
    clean_output_file('output.txt')

if __name__ == "__main__":
    main()
