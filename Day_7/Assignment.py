"""1) Custom String Class with OOP Features
Problem Statement:
Implement a class FileOps initialized with two files. One for reading and one for writing. The first file
contain one entry in each line, can be either string or number. Read the strings only and write a
report in the second file with the entry as result of following operations. Implement exception
handling while reading the file
Palindrome, Number of vowels, Number of consonants, resulting string with duplicates removed
Input Format:
 Input line abcefgaccdbgh
 Output Line: N, 3, 10, abcefgdh"""

input_file = "r_file.txt"  
output_file = "w_file.txt"  

class FileOps:
    def _init_(self, input_file, output_file):
        self.input_file = input_file  # File to read from
        self.output_file = output_file  # File to write to

    def is_palindrome(self, s):
        """Check if the string is a palindrome."""
        return s == s[::-1]

    def count_vowels_consonants(self, s):
        """Count the number of vowels and consonants in the string."""
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        count_v = sum(1 for char in s if char in vowels)
        count_c = sum(1 for char in s if char in consonants)
        return count_v, count_c

    def remove_duplicates(self, s):
        """Remove duplicate characters from the string while preserving order."""
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return "".join(result)

    def process_file(self):
        """Read the input file, process each line, and write the results to the output file."""
        try:
            with open(self.input_file, "r") as infile, open(self.output_file, "w") as outfile:
                for line in infile:
                    line = line.strip()  # Remove leading/trailing whitespace
                    if line and line.isalpha():  # Process only if the line is a string
                        # Perform operations
                        palindrome = "Y" if self.is_palindrome(line) else "N"
                        vowels, consonants = self.count_vowels_consonants(line)
                        unique_string = self.remove_duplicates(line)

                        # Write the result to the output file
                        outfile.write(f"{palindrome}, {vowels}, {consonants}, {unique_string}\n")
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "_main_":
    input_file = "r_file.txt"  # Replace with your input file name
    output_file = "w_file.txt"  # Replace with your output file name

    file_ops = FileOps(input_file, output_file)
    file_ops.process_file()

# 2. Word Frequency Counter in Large Text and show it in dictionary format

class WordFrequencyCounter:
    def _init_(self, text):
        self.text = text
        self.freq = dict()

    def __transform(self, text):
        new_st = ""
        text = text.replace('.', '')
        l = text.split(" ")
        for word in l:
            new_st = new_st + word.lower() + " "
        return new_st.strip()

    def word_count(self):
        new_text = self.__transform(self.text)
        l = new_text.split(" ")
        s = set()

        for i in l:
            s.add(i.lower())
        for words in s:
            self.freq[words] = l.count(words)

        return self.freq

text = input("Text: ")    
w = WordFrequencyCounter(text)
d = w.word_count()
print(d)
        
# 3. enter the numbers and right shift the binary representation of the number by number of spikes given

N=int(input())
a=list(map(int,input().split()))
n=int(input())
s=""
for i in a:
    s+=str(i>>n)+" "
print(s)
