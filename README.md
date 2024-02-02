Mockup of querying a decision log with Cohere's Chat API.


##################### RESPONSES ###################

Query: Can we accept NET120 payment terms?
Response: NET120 payment terms are not accepted in Finance. 

Currently, the department can accept NET30 payment terms, and NET60 payment terms with a two-year commitment.
Documents: [{'decision': 'Finance will only accept NET30 payment terms.', 'department': 'Finance', 'id': 'doc_0'}, {'decision': 'Finance will accept NET60 payment terms with a two year commitment.', 'department': 'Finance', 'id': 'doc_1'}]

####################

Query: Do we accept NET60 payment terms?
Response: This depends on the department - Finance will only accept NET30 payment terms, but NET60 payment terms are accepted with a two-year commitment. 

I suggest checking with your finance department to see if payments can be made net 60.
Documents: [{'decision': 'Finance will only accept NET30 payment terms.', 'department': 'Finance', 'id': 'doc_0'}, {'decision': 'Finance will accept NET60 payment terms with a two year commitment.', 'department': 'Finance', 'id': 'doc_1'}]

####################

Query: Can I just merge this into master?
Response: In order to successfully merge code, Engineering uses a pull request system, wherein the code is reviewed and approved before being merged into the master branch. 

Is there anything else you would like to know about code merging as it pertains to Engineering?
Documents: [{'decision': 'Engineering will only use pull requests to merge code.', 'department': 'Engineering', 'id': 'doc_2'}]

####################

Query: Let's store that as a policy.
Response: Engineering will store all company policies in Notion going forward. If you have any specific policies you would like me to help you draft, please let me know and I will do my best to assist you.
Documents: [{'decision': 'We store all company policies in Notion.', 'department': 'Operations', 'id': 'doc_4'}]

####################

Query: I can't find my project.
Response: Hmm, that's not good. But don't worry, I can help you with that. I know Engineering needs to have an associated Jira ticket for all project work, so maybe start there? If you're using Jira for project management, it's a good idea to see if the project is in Jira. If you still can't find it, maybe it has no associated ticket and actually belongs in Notion, where all company policies are stored.
Documents: [{'decision': 'All engineering work must have an associated ticket in Jira.', 'department': 'Engineering', 'id': 'doc_6'}, {'decision': 'We store all company policies in Notion.', 'department': 'Operations', 'id': 'doc_4'}]

####################

Query: Going to get started on this work without a ticket.
Response: I'm sorry, but according to the Engineering team, all engineering work must have an associated ticket in Jira.
Documents: [{'decision': 'All engineering work must have an associated ticket in Jira.', 'department': 'Engineering', 'id': 'doc_6'}]

####################
