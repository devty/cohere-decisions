import os
import re
import warnings

import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_APP_API_KEY")
warnings.filterwarnings('ignore')


# Now we'll set up the cohere client.
co = cohere.Client(api_key=api_key)

# Prepare our decisions
decisions = [ 
    {"start_date":"01/01/2018","department":"Finance", "decision":"Finance will only accept NET30 payment terms."},
    {"start_date":"01/01/2019","department":"Finance","decision":"Finance will accept NET60 payment terms with a two year commitment."},
    {"start_date":"01/01/2020","department":"Engineering","decision":"Engineering will only use pull requests to merge code."},
    {"start_date":"01/01/2023","department":"Product","decision":"Product releases will be on the first Monday of every month."},
    {"start_date":"01/01/2022","department":"Operations","decision":"We store all company policies in Notion."},
    {"start_date":"01/01/2021","department":"Product","decision":"We use Jira for all project management."},
    {"start_date":"01/01/2020","department":"Engineering","decision":"All engineering work must have an associated ticket in Jira."}
]

# We'll save this later
#import json
#decisions_json = json.dumps(decisions, indent=4)

model_name = "embed-english-v3.0"

# Sample queries from Slack, both questions and statements
query = ["Can we accept NET120 payment terms?",
         "Do we accept NET60 payment terms?",
         "Can I just merge this into master?",
         "Let's store that as a policy.",
         "I can't find my project.",
         "Going to get started on this work without a ticket."]

input_type_embed = "search_document"




## Query Cohere chat for each of our sample queries, along with the collection of existing decisions
for i in query:
    response = co.chat(message=i,
                       documents=decisions)
    with open('response.txt', 'a') as f:
        f.write(f"Query: {response.message}\n")
        f.write(f"Response: {response.text}\n")
        f.write(f"Documents: {response.documents}\n\n####################\n\n")
    


