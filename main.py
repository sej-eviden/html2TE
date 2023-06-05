import argparse
import json
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument("-file", "--examfile", help="HTML Exam file")
args = parser.parse_args()
file = args.examfile

with open(file, "r", encoding="utf-8") as HTMLFile:
    index = HTMLFile.readlines()
    title = ""

    file_title = ""

    currentTitleI = 0
    questionI = -1
    currentBodyI = 0
    currentOptionI = 0

    questions = {}

    for i, line in enumerate(index):
        if index[i - 1].find("<h1") >= 0:
            file_title = line.split("Exam Actual Questions")[0].strip()

        if line.find("<div class=\"card-header text-white bg-primary\">") >= 0:
            currentTitleI = i
            questionI += 1
        if i == currentTitleI + 1 and questionI >= 0:
            title = line.strip().replace("#", "")
            print(title)
        if i == currentTitleI + 3 and questionI >= 0:
            title = line.strip() + " | " + title
            title = " ".join([word.rjust(2, "0") for word in title.split(" ") if word != "|"])
            print(title)
            questions[title] = {
                "options": [],
                "body": [],
                "answer": ""
            }

        if line.find("<p class=\"card-text\">") >= 0:
            currentBodyI = i
        if i == currentBodyI + 3 and title in questions:

            paragraphs = line.strip().split("<br>")
            for p in paragraphs:
                if p.find("img") > 0:
                    src = p.split('"')[1].split("/")[-1]
                    p = f"<img>/{file_title}/img/{src}<img>"
                questions[title]["body"].append(p.strip())
            # questions[title]["body"] =

        if line.find("<li class=\"multi-choice-item") >= 0:
            currentOptionI = i
        if i == currentOptionI + 6 and title in questions:
            questions[title]["options"].append(line.strip())

        # Change to find in "<div class="voting-summary" and also save percentage
        # <div class="vote-bar progress-bar bg-primary"
        if line.find("<div class=\"vote-bar progress-bar bg-primary\"") >= 0 and title in questions:
            ans_start = line.find(">", line.find("<div class=\"vote-bar progress-bar bg-primary\""))
            ans = line[ans_start + 1: line.find(" ", ans_start)]
            questions[title]["answer"] = ans

        if line.find("<span class=\"correct-answer\"><img") >= 0:
            src = line.split('/')[2].split('"')[0]
            questions[title]["options"].append(f"<img>/{file_title}/img/{src}<img>")
            
    # for key in questions.keys():
    #     print(key)

    for question_title in questions:
        question_formatted = {
            "title": question_title,
            "body": questions[question_title]["body"],
            "options": questions[question_title]["options"],
            "answer": questions[question_title]["answer"]
        }
        json_file = f"./results/{file_title.replace(' ', '_')}/{question_title.replace(' | ', '_').replace(' ', '_')}.json"
        print(json_file)
        with open(json_file, "w") as end_file:
            json.dump(question_formatted, end_file)
