import cohere
import numpy as np
import re
import pandas as pd
from tqdm import tqdm
from datasets import load_dataset
import umap
import altair as alt
from sklearn.metrics.pairwise import cosine_similarity
from annoy import AnnoyIndex
import warnings
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_APP_API_KEY")
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)

# Now we'll set up the cohere client.
co = cohere.Client(api_key=api_key)

# Prepare our decisions
decisions = [ 
    {"department": "Finance", "decision":"Finance will only accept NET30 payment terms."},
    {"department": "Finance","decision":"Finance will accept NET60 payment terms with a two year commitment."},
    {"department": "Engineering","decision":"Engineering will only use pull requests to merge code."},
    {"department": "Product","decision":"Product releases will be on the first Monday of every month."},
    {"department": "Operations","decision":"We store all company policies in Notion."},
    {"department": "Product","decision":"We use Jira for all project management."},
    {"department": "Engineering","decision":"All engineering work must have an associated ticket in Jira."}
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
    print(response)

    

