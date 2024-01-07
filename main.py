# importing the required libraries
from PyPDF2 import PdfReader
import openai

# reading the resume (pdf) file
reader = PdfReader('resume2.pdf')

# extracting text from the pdf
page = reader.pages[0]
text = page.extract_text()

# sending the extracted text to openai api to get the specified details about the candidate
openai.api_key = "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"
messages = [{"role": "system", "content": "You are a kind helpful assistant."}, ]

# giving the necessary prompt to openai api for getting the required details
message = text + "extract Candidate’s name,Candidate’s email,Candidate’s phone number and Candidate’s work experience from the above text extracted from a resume"
if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

# extracting the reply from the openai api
reply = chat.choices[0].message.content

# printing the candidate details
result = str(reply)
print(result)
