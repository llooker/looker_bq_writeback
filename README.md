# looker_bq_writeback

cloud function to write back to Looker


This cloud function leverage [Looker's Actions](https://looker.com/platform/actions/) as the starting point to write back to our table in BigQuery to update records. 

At a high level, the script is:

1. Takes in row level data in JSON format passed from Looker's actions. 
2. Reads and parses the relevant values to populate our SQL query which will INSERT into our specified table


Additional resources:
[Cloud Function](https://cloud.google.com/functions)
