# getdefs_LSJ
A Python script that retrieves dictionary definitions from the Liddell–Scott–Jones *Greek–English Lexicon* (LSJ) for words saved as a list in a text file

## Instructions

Download the LSJ xml files here: https://github.com/helmadik/LSJLogeion

Update the location of the files in the script (replace "/path/to/LSJ" with your directory in double quotation marks).

Save a UTF-8 text file of Greek words, each on a new line, in the same directory as this script. Give it the name "wordlist.txt".

Run the script from Terminal:
```
$ python3 getdefs_LSJ.py
```
Depending on the number of words in your list, the script may need some time to finish, so be patient.

The script will create "output.txt", a tab-delineated text file containing your words and their definitions, provided it finds the relevant lemmata in the LSJ.

Check definitions thoroughly. The script imports definitions only, no grammatical details like gender, case usage or voice information.

### Credits
The incomparable Helma Dik of [Logeion] (https://logeion.uchicago.edu/λόγος), Perseus Tufts

### Errors
Please report LSJ errors here: https://logeion.uchicago.edu/ (click
"Report a Problem" at top right-hand corner).
