# Deactivation Key

It's yet another Tuesday and you're in lecture learning about all the wonderful things Python can do. Your teacher starts talking about another super useful topic that you're really interested in. All of the sudden, his computer starts going crazy! He's getting hacked!

He powers off his computer to sever the connection. Knowing that the hacker will pounce when he restarts, he asks for your help. If he can find the deactivation key for all the malicious packets he received, he could mount an effective defense against the attacker.

## Packet Data

Please head to [this github page](https://github.com/poguepotamus/deactivation_key). Included is the code used to generate all your input files, but more importantly, your puzzle input.

Browse to `data`, and click on the last four digits of your student ID. (If yours does not appear, please let me know).

One file (`packet_base.txt`) includes 32,768 lines of data for your deactivation key. Finding the deactivation key can be complex, but might be easy if you use third-party packages like numpy (nudge nudge).

The other file (`packet_weight.txt`) includes the same length of data, but is a weight of how important that data is.

Inside your folder, you'll also see an answer folder, and inside, a collection of 4,096 files that simply contain either 'incorrect' or 'correct'. This is how you will check your result.

## Finding the Deactivation Key

Finding the deactivation key of your packet can be broken down into a few steps that you'll need to follow.

1. Load both the packge_base data and the packet_weight data as an array.
2. Separate your data into chunks of 8.
   1. You should have a 2D array, 4096 arrays of 8 values.
3. Multiply your base array by your weight values for every element.
4. For each of the chunks, you'll need to find the minimum, maximum, and mean. The 'result' of each chunk will be `(max - mean) * min`.
5. Find the sum of all your chunk results and round down to the next integer.
6. Find the remainder if you divided by 4096.

Once you find your answer, you can take the following url and replace the information surrounded by carrots with their appropriate values to paste into your browser's url box.

```
https://github.com/poguepotamus/deactivation_key/tree/main/data/<last_4_studentID>/answers/<answer>
```

i.e. if I think the proper result is `183`, and the last 4 digits of my student ID are `3829`, I would go to:

```
https://github.com/poguepotamus/deactivation_key/tree/main/data/3829/answers/183
```

## Testing

In the data directory, you'll find another folder `test`. This dataset has smaller input files and a file containing the final answer for your testing.

## Submission

Your assignment should be submitted as a link to a remote git repository.