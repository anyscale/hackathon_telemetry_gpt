**Ray Telemetry GPT**

A natural language interface over our Ray telemetry data. Easily answer questions such as "How many new users for HuggingfaceTrainer are there from 2.5 to 2.6?" or "What instance type is most used with RLlib?"  without needing to stare at graphs or write SQL queries yourself. Through prompt engineering, we can have LLMs return a structured response containing a SQL query to answer the provided question, which we can then execute on the telemetry database before returning back to the user. An example from LangChain.

***How to start the server?***

- Follow  https://github.com/anyscale/hermetic/blob/main/README.md to set up environment.
   1. python -m pip install --upgrade pip
   2. pip install git+https://github.com/anyscale/hermetic.git
   3. export OPENAI_API_BASE=https://console.endpoints.anyscale.com/m/v1
   4. export OPENAI_API_KEY=secret_<your secret> 
- Run **python pirate_langchain.py** in local.
- Go to http://127.0.0.1:7860/.
