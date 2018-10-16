# Learn Python for Data Science -- #3 Recommendation Systems
import numpy as np
import scipy
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

def sample_recomendation(model, data, user_ids):
	# number of users and moives ini training data
	n_users, n_items = data['trian'].shape;
	
	# generate recommendations for each user we input
	for user_id in user_ids:
	
		# moives they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices];
		
		# moives our model predicts they will like
		scores = model.predict(user_id, np.arange(n_items));
		# rank them in order of most liked to least
		top_items = data['item_labels'][np.argsot(-scores)];
		
		# print out the results
		print("User %s", %user_id);
		
		print("\t\tKnown positives:");
		for x in known_positives[:3]:
			print("\t\t\t%s", %x);
		
		print("\t\tRecommendation:");
		for x in top_items[:3]:
			print("\t\t\t%s",%x);

# fetch data abd format it 
data = fetch_movielens(min_rating = 4.0);

# print training and testing data
print(repr(data['train']));
print(repr(data['test']));

# create model
model = LightFM(loss='warp'); # warp = Weighted Approximate-Rank Pairwise
# train model
model.fit(data['train'], epochs=30, num_threads=2);

sample_recomendation(model,data)