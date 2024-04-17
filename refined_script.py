# This script is not part of this project. 
# It was used for collecting data from web and storing in specific files for Geeks job project

import re
import random

index = 1
count = 1
geeksJobRegex = re.compile(r'(.*), (.*), (.*), (.*), (.*), (.*)')

with open('all.txt', 'r+', encoding="UTF8") as opener, open('question.json', 'a+', encoding='UTF8') as writer:
    for line in opener:

        regex = geeksJobRegex.search(line)

        if regex is None:

            print("Something is missing at Line ", index)

        else:

            option1 = regex.group(2)
            option2 = regex.group(3)
            option3 = regex.group(4)
            option4 = regex.group(5)
            answer = regex.group(6)

            optionsList = [option1, option2, option3, option4]
            random.shuffle(optionsList)

            if option1 == option2 \
                    or option3 == option4 \
                    or option1 == option3 \
                    or option1 == option4 \
                    or option2 == option3 \
                    or option2 == option4:
                pass
            else:
                if option1 == answer or option2 == answer or option3 == answer or option4 == answer:

                    writer.write("\"{}\":{{"
                                    "\"question\":\"{}\","
                                    "\"option1\":\"{}\","
                                    "\"option2\":\"{}\","
                                    "\"option3\":\"{}\","
                                    "\"option4\":\"{}\","
                                    "\"answer\":\"{}\"}},".format(index,
                                                                regex.group(1),
                                                                optionsList[0],
                                                                optionsList[1],
                                                                optionsList[2],
                                                                optionsList[3],
                                                                regex.group(6)))
                else:
                    print("Problem found in ", index)

                index = index + 1
