# Assignment 4

It's yet another Tuesday and you're in lecture learning about all the wonderful things Python can do. Your teacher starts talking about another super useful topic that you're really interested in. All of the sudden, his computer starts going crazy! He's getting hacked!

He powers off his computer to sever the connection. Knowing that the hacker will pounce when he restarts, he asks for your help. If he can find the deactivation key for all the malicious packets he received, he could mount an effective defense against the attacker.

## Packet Data

Please head to this github page. Included is the code used to generate all your input files, but more importantly, your puzzle input.

Browse to 'students', and click on the last four digits of your student ID. (If yours does not appear, please let me know).

One file (`packet_base.txt`) includes 32,768 lines of data for your deactivation key. Finding the deactivation key can be complex, but might be easy if you use third-party packages like numpy (nudge nudge).

The other file (`packet_weight.txt`) includes the same length of data, but is a weight of how important that data is.

Inside your folder, you'll also see an answer folder, and inside, a collection of 4096 files that simply contain either 'incorrect' or 'correct'. This is how you will check your result.

## Deactivation Key

Finding the deactivation key of your packet can be broken down into a few steps that you'll need to follow.

1. Load both the base data and the mult data as an array.
2. Separate your data into chunks of 8.
   1. You should have a 2D array, 4096 arrays of 8 values.
3. Multiply your base array by your weight values for every element.
4. For each of the chunks, you'll need to find the minimum, maximum, and mean. The 'result' of each chunk will be `(max - mean) * min`.
5. Find the sum of all your chunk results and round down to the next integer.
6. Find the remainder if you divided by 4096.

Once you think you have an answer, you can go to your `answers` folder, ctrl+f, and type in your value. click the file with the name of your final value to check your answer!

## Testing

In the data directory, you'll find another folder `test`. This dataset has smaller input files and a file containing the final answer for your testing. Instead of chunks of 8, you'll need to use chunks of 4.
