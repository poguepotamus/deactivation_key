import numpy as np
from pathlib import Path
import packetParser

import logging as logger
logger.basicConfig(level=logger.INFO)

DATA_SIZE = [64 * 64, 8]
MAX_VALUE = 64 * 64
DATA_PATH = Path(r'.\data').resolve()
ANSWERS_PATH = DATA_PATH / 'answers'
STUDENT_IDS = [
    '4800',
    '3770',
    '3495',
    '8471',
    '7266',
    '2262',
    '7302',
    '3341'
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
    ANSWERS_PATH.mkdir(exist_ok=True)

    for studentId in STUDENT_IDS:
        logger.info(f'Starting on student ending in `{studentId}`')
        # Creating the path for the student
        studentDataPath = DATA_PATH / str(studentId)
        studentDataPath.mkdir(exist_ok=True)

        logger.info('Generating the packet base and weight for the student')
        # Inside that directory, we'll put a random base file and a random mult file
        studentPacketBase = studentDataPath / 'packet_base.txt'
        studentPacketMult = studentDataPath / 'packet_weight.txt'

        genBaseFile(studentPacketBase)
        genMultFile(studentPacketMult)

        # Now that we have the inputs, we'll parse them and find our answer
        logger.info('Finding the answer for our student')
        answer = packetParser.findDeactivationKey(
            studentPacketBase,
            studentPacketMult,
            DATA_SIZE
        )
        logger.info(f'Answer for student `{studentId}` is `{answer}`')

        # Writing the answer to the answer directory
        answerFile = ANSWERS_PATH / studentId
        logger.info(f'Writing answer to `{answerFile}`')
        with open(answerFile, 'w', encoding='utf-8') as answerOutputFile:
            answerOutputFile.write(str(answer))

        

        # Creating our answers directory, writing all our possible files, writing 'correct' to the one that matches our answer.
        logger.info(f'Writing the answer files for student `{studentId}`')
        studentAnswerPath = studentDataPath / 'answers'
        studentAnswerPath.mkdir(exist_ok=True)
        # If we're writing a example, we write the answer to the answers directory
        if 'test' in studentId.lower():
            with open(studentAnswerPath / 'answer', 'w', encoding='utf-8') as answerFile:
                answerFile.write(answer)

        # Now, iterating through all the possible answer files and writing them
        for it in range(1, 4096):
            if it % 500 == 0:
                logger.info(f'Writing file `{it}`')
            answerPath = studentAnswerPath / str(it)
            with open(answerPath, 'w', encoding='utf-8') as answerFile:
                if it == answer:
                    answerFile.write('correct')
                else:
                    answerFile.write('incorrect')
