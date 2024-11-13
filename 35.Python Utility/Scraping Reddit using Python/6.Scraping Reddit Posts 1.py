from praw.models import MoreComments

post_comments = []

for comment in submission.comments:
	if type(comment) == MoreComments:
		continue

	post_comments.append(comment.body)

# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
comments_df
