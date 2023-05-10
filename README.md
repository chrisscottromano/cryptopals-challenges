# cryptopals-challenges
Solutions to some of the [cryptopals crypto challenges](https://cryptopals.com/)
All done in python

1. Converts hex to base64 without using libraries
2. Simple fixed XOR
3. Brute force XOR decipher + output strings ranked by word frequency similarity to english (correct string ranked third)
4. For each string, top-10 candidate strings returned via word frequency similarity. Once all strings are processed, the top 50 of all produced strings are returned, ranked again. The word frequency similarity approach was performing poorly on this task, so I used the Natural Language ToolKit (NLTK) to perform more robust screening. The correct string is ranked first.
5. Still working on this guy.  
