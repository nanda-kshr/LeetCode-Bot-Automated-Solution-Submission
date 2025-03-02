import html
import json
import re
import time
import requests
def print_ascii_with_color(starting):
    colored_text = ""
    for char in starting:
        if char == '█' or char == '▄':
            colored_text += char
        elif char.strip():  
            colored_text += "\033[91m" + char + "\033[0m" 
        else:
            colored_text += char 
    print(colored_text)

starting = """
 ██▓    ▓█████ ▓█████▄▄▄█████▓ ▄████▄  ▒█████  ▓█████▄  ▓█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██▒    ▓█   ▀ ▓█   ▀▓  ██▒ ▓▒▒██▀ ▀█ ▒██▒  ██▒▒██▀ ██▌ ▓█   ▀     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒██░    ▒███   ▒███  ▒ ▓██░ ▒░▒▓█    ▄▒██░  ██▒░██   █▌ ▒███       ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██░    ▒▓█  ▄ ▒▓█  ▄░ ▓██▓ ░ ▒▓▓▄ ▄██▒██   ██░░▓█▄   ▌ ▒▓█  ▄     ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░██████▒░▒████▒░▒████  ▒██▒ ░ ▒ ▓███▀ ░ ████▓▒░░▒████▓ ▒░▒████    ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒░▓  ░░░ ▒░ ░░░ ▒░   ▒ ░░   ░ ░▒ ▒  ░ ▒░▒░▒░  ▒▒▓  ▒ ░░░ ▒░     ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░ ▒  ░ ░ ░  ░ ░ ░      ░      ░  ▒    ░ ▒ ▒░  ░ ▒  ▒ ░ ░ ░      ░▒░▒   ░   ░ ▒ ▒░     ░    
  ░ ░      ░      ░    ░      ░       ░ ░ ░ ▒   ░ ░  ░     ░        ░    ░ ░ ░ ░ ▒    ░      
    ░  ░   ░  ░   ░           ░ ░         ░ ░     ░    ░   ░      ░ ░          ░ ░       


    
Developed By - Evil Beast 
LeetCodeBot version 2.0
"""
print_ascii_with_color(starting)
countofsubmitions = 0
time.sleep(3)
print("\033[94mLogged In Successfully")
time.sleep(1)
print("\033[94m Task Initiated\033[92m")
for i in range(1, 10):
    print(".", end="", flush=True) 
    time.sleep(.2) 
print("")
skip = 400

crfToken = input("crfToken : ")
cookie =  input("cookies : ")
headers = {
    'Host': 'leetcode.com',
    'Content-Type': 'application/json',
    f'Cookie':cookie,
    'X-Csrftoken': crfToken,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Origin': 'https://leetcode.com',
    'Referer': 'https://leetcode.com/problems/two-sum/',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

zzzheaders = {
    "Host": "zzzcode.ai",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://zzzcode.ai",
    "Referer": "https://zzzcode.ai/code-generator?id=70ca1d02-1631-45ac-97e2-5e1d9bd26637",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}


def fetch_problems():
    problems_data = {
        "query": """
            query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
                questions: data {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                paidOnly: isPaidOnly
                status
                title
                titleSlug
                topicTags {
                    name
                    id
                    slug
                }
                hasSolution
                hasVideoSolution
                }
            }
            }
        """,
        "variables": {
            "categorySlug": "all-code-essentials",
            "skip": skip,
            "limit": 100,
            "filters": {}
        },
        "operationName": "problemsetQuestionList"
    }
    response = requests.post(url="https://leetcode.com/graphql/", headers=headers, json=problems_data)
    return response.json()['data']['problemsetQuestionList']['questions']

def clean_code(html_string):
    text = re.sub(r'<[^>]+>', '', html_string)
    text = html.unescape(text)
    return text
 
def remove_comments(code):
    return re.sub(r'#.*', '', code)

def convert_textarea_to_code(textarea_content):
    code_snippet = textarea_content.strip()
    code_snippet = code_snippet.replace('<textarea b-lh4nsey01i id="uiOutputContent" style="display: none;">', '')
    code_snippet = code_snippet.replace('</textarea>', '')
    code_snippet = code_snippet.replace("&#xA;","\n")
    return remove_comments(code_snippet)

def extract_python_code(data):
    data_part = data.split("data: ")[1].strip().replace("zzz", "")
    decoded_code = data_part.encode('latin1').decode('unicode_escape')
    decoded_code = decoded_code.replace("```python","")
    decoded_code = decoded_code.replace("```","")
    decoded_code = decoded_code.replace('"',"")
    decoded_code = decoded_code.replace('newline',"\n")
    decoded_code = decoded_code.replace('\n\n',"\n")
    return decoded_code

def connect_to_browser(problem):
    title_slug = problem['titleSlug']
    print(f"Processing: {title_slug}")
    problem_desc_query = {
        "query": """
        query questionContent($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                content
                mysqlSchemas
                dataSchemas
            }
        }
        """,
        "variables": {"titleSlug": title_slug},
        "operationName": "questionContent"
    }
    problem_desc = requests.post('https://leetcode.com/graphql/', headers=headers, json=problem_desc_query).json()['data']['question']
    problem_desc = clean_code(problem_desc['content'])
    
    input_data_query = {
        "query": """
        query consolePanelConfig($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                questionTitle
                enableDebugger
                enableRunCode
                enableSubmit
                enableTestMode
                exampleTestcaseList
                metaData
            }
        }
        """,
        "variables": {"titleSlug": title_slug},
        "operationName": "consolePanelConfig"
    }
    input_data = requests.post('https://leetcode.com/graphql/', headers=headers, json=input_data_query).json()['data']['question']['exampleTestcaseList']
    input_data = "\n".join(input_data)

    starting_code_query = {
        "query": """
        query questionEditorData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                envInfo
                enableRunCode
                hasFrontendPreview
                frontendPreviews
            }
        }
        """,
        "variables": {"titleSlug": title_slug},
        "operationName": "questionEditorData"
    }
    starting_code = requests.post('https://leetcode.com/graphql/', headers=headers, json=starting_code_query).json()['data']['question']['codeSnippets'][3]['code']
    proper_question =  problem_desc+"\n . Format of code " + starting_code 
    code_id = ""
    coder = "https://zzzcode.ai/api/tools/code-generator"
    bot_input = {"id":code_id,
                 "p1":"Python3",
                 "p2": proper_question ,
                 "p3":"",
                 "p4":"",
                 "p5":"",
                 "option1":"2 - Generate code",
                 "option2":"Professional",
                 "option3":"English",
                 "hasBlocker":True}
    json_data = json.dumps(bot_input)
    code_id = requests.post(coder, headers=zzzheaders, data=json_data).text
    code_id = code_id.split('"')
    code_id = code_id[1].replace("zzzredirectmessageidzzz:","")
    code_id = code_id.replace("zzzmessageidzzz:","")
    code_id = code_id.replace(" ","")
    bot_input = {"id":code_id,
                 "p1":"Python3",
                 "p2": "" ,
                 "p3":"",
                 "p4":"",
                 "p5":"",
                 "option1":"2 - Generate code",
                 "option2":"Professional",
                 "option3":"English",
                 "hasBlocker":True}
    json_data = json.dumps(bot_input)
    generated_code = requests.post(coder, headers=zzzheaders, data=json_data).text
    generated_code = requests.post(coder, headers=zzzheaders, data=json_data).text
    generated_code = extract_python_code(generated_code)
    generated_code = remove_comments(generated_code)
    print("Generated Code")
    problem_id_query = {
        "query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    categoryTitle\n  }\n}\n    ",
        "variables": {"titleSlug": title_slug},
        "operationName": "questionTitle"
    }
    problem_id = requests.post('https://leetcode.com/graphql/', headers=headers, json=problem_id_query).json()['data']['question']["questionId"]
    run_code_data = {
        "lang": "python3",
        "question_id": problem_id,
        "typed_code": generated_code,
        "data_input": input_data
    }
    run_codeurl = f'https://leetcode.com/problems/{title_slug}/interpret_solution/'
    run_code_response = requests.post(run_codeurl, headers=headers, json=run_code_data).json()
    if not check_code_execution(run_code_response['interpret_id']):
        return False
    submit_code_data = {
        "lang": "python3",
        "question_id": problem_id,
        "typed_code": generated_code
    }
    submit_code_response = requests.post(f'https://leetcode.com/problems/{title_slug}/submit/', headers=headers, json=submit_code_data).json()
    check_code_submission(submit_code_response['submission_id'])

def check_code_execution(interpret_id):
    while True:
        response = requests.post(f'https://leetcode.com/submissions/detail/{interpret_id}/check/', headers=headers).json()
        if response['state'] == "SUCCESS":
            if response['status_msg'] != 'Accepted':
                print("\033[91mExecution Failed\033[92m")
                return False
            else:
                return True
        else:
            time.sleep(3)

def check_code_submission(submission_id):
    while True:
        response = requests.post(f'https://leetcode.com/submissions/detail/{submission_id}/check/', headers=headers).json()
        if response['state'] == "SUCCESS":
            if response['status_msg'] != 'Accepted':
                print("\033[91mSubmission Failed:\033[92m")
                return False
            else:
                print("Submission Successful")
                return True
        else:
            time.sleep(3)

def main():
    global countofsubmitions
    problems = fetch_problems()
    for problem in problems:
        try:
            connect_to_browser(problem)
            countofsubmitions += 1
            print(f"No of successful submissions : {countofsubmitions}")
            time.sleep(3)
        except Exception as e:
            print(e)

while(True):
    main()
    skip += 100

