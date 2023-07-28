#pip install openai
import openai, constants

def ask_chatgpt(question:str, system_command:str = "", model:str = 'gpt-3.5-turbo', temperature:float=.2, max_tokens:int=256):
	openai.api_key = constants.openai_api_key
	messages = []
	if system_command !="": messages.append({"role": "system", "content": system_command})
	messages.append({"role": "user", "content": question})
	try: 
		result = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens )
		success = True
	except Exception as e:
		print("ChatGPT query failed:", e)
		success = False
		result = "API Call Failed"
	if success: result = result.choices[0].message.content
	return result

if __name__ == "__main__":
	datafile_in = "resume_input.txt"
	datafile_out = "resume_output.txt"
	with open(datafile_in, "r") as text_file:
		resume = text_file.read()	
	question = "write a resume from the following input: " + resume
	chatgpt_result = ask_chatgpt(question=question, model ='gpt-3.5-turbo', max_tokens=2600)
	with open(datafile_out, "w") as text_file:
		text_file.write(chatgpt_result)
	
