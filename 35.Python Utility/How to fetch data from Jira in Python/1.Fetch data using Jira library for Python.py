# import the installed Jira library
from jira import JIRA

# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://txxxxxxpython.atlassian.net"}

# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options=jiraOptions, basic_auth=(
	"prxxxxxxh@gmail.com", "bj9xxxxxxxxxxxxxxxxxxx5A"))

# Search all issues mentioned against a project name.
for singleIssue in jira.search_issues(jql_str='project = MedicineAppBugs'):
	print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,
							singleIssue.fields.reporter.displayName))
