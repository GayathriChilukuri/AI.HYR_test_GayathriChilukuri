# AI.HYR take-home test

## Instructions to run the code: <br>
1. install the libraries PyPDF2 and openai using the following commands: <br>
pip install openai==0.28<br>
pip install PyPDF2<br>
2. paste the pdf format of the resume(from which the details need to be extracted) in the same folder as the main.py<br>
3. run main.py to extract and print the specified details of the candidate<br>

## Approach<br>
1. Firstly, I extracted the text from the pdf file using the PyPDF2 library <br>
2. Then, sent the extracted text along with the prompt message to the Openai API <br>
3. Printed the response from the API in the terminal <br>
4. This response will have the required details: Candidate’s name, Candidate’s email, Candidate’s phone number, Candidate’s work experience
<br><br><br>

##Gayathri Chilukuri
