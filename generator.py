import numpy as np
from pathlib import Path
import packetParser

DATA_SIZE = [64 * 64, 8]
MAX_VALUE = 64 * 64
# DATA_SIZE = [8, 4]
# MAX_VALUE = 64 * 8

DATA_PATH = Path(r'\\neptune\dropbox\projects\teaching\2301_INF-138\assignments\a4\data')
ANSWERS_TEMPLATE = Path(r'\\NEPTUNE\dropbox\projects\teaching\2301_INF-138\assignments\a4\answers')

STUDENT_IDS = [
    # 'test'
    46743, 52646, 36933, 44128,
    52858, 52655, 53811, 33793,
    36899, 33507, 52759, 52951,
]

def genBaseFile(fileLocation:Path):
    # Generating our base case first
    np.savetxt(
        fileLocation,
        np.multiply(
            np.random.rand(*DATA_SIZE).flatten(),
            MAX_VALUE,
        ).astype(int),
        fmt='%d',
        delimiter='\n'
    )

def genMultFile(fileLocation:Path):
    # Generating the mult case
    np.savetxt(
        fileLocation,
        np.random.rand(*DATA_SIZE).flatten(),
        fmt='%.4f',
        delimiter='\n'
    )

if __name__ == '__main__':
    DATA_PATH.mkdir(exist_ok=True)

    for studentId in STUDENT_IDS:
        # Creating the path for the student
        studentDataPath = DATA_PATH / str(studentId)
        studentDataPath.mkdir(exist_ok=True)

        # Inside that directory, we'll put a random base file and a random mult file
        studentPacketBase = studentDataPath / 'packet_base.txt'
        studentPacketMult = studentDataPath / 'packet_weight.txt'

        genBaseFile(studentPacketBase)
        genMultFile(studentPacketMult)

        # Now that we have the inputs, we'll parse them and find our answer
        answer = packetParser.findDeactivationKey(
            studentPacketBase,
            studentPacketMult,
            DATA_SIZE
        )

        # Writing the answer to the directory
        if studentId == 'test':
            with open(studentDataPath / 'answer', 'w', encoding='utf-8') as answerFile:
                answerFile.write(str(answer))

        # Creating our answers directory, writing all our possible files, writing 'correct' to the one that matches our answer.
        studentAnswerPath = studentDataPath / 'answers'
        studentAnswerPath.mkdir(exist_ok=True)
        for it in range(1, 4096):
            answerPath = studentAnswerPath / str(it)
            with open(answerPath, 'w', encoding='utf-8') as answerFile:
                if it == answer:
                    answerFile.write('correct')
                else:
                    answerFile.write('incorrect')
