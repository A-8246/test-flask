#updates
from flask import Flask,request

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os

os.environ['WOLFRAM_ALPHA_APPID'] = 'EWGUTT-U3K3R95PHU'
os.environ['OPENAI_API_KEY'] = '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'

def out(query):
	llm = OpenAI(temperature=0)
	tool_names = ["wolfram-alpha"]
	tools = load_tools(tool_names)
	agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
	res = agent.run(query)
	return res


app = Flask(__name__)


@app.route('/qa')
def hello_world():
	args = request.args
	arg = args.get("query")
	res = out(arg)
	return {'bot': res}


if __name__ == '__main__':
    app.run()
