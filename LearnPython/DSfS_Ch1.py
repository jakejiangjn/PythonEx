# from __future__ import division # integer division is lame
from collections import defaultdict
from collections import Counter	# not loaded by default


# functions
def number_of_friends(user):
        """how many friends does _user_ have?"""
        return len(user["friends"]) # length of friend_ids list

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
	return [foaf["id"]
		for friend in user["friends"] # for each of user's friends
		for foaf in friend["friends"]] # get each of _their_ friends

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
	that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
		for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
					for friend in user["friends"] # for each of my friends
					for foaf in friend["friends"] # count *their* friends
					if not_the_same(user, foaf) # who aren't me
					and not_friends(user, foaf)) # and aren't my friends

def data_scientists_who_like( target_insterets ):
    return[user_id
			for user_id, user_interest in interests
			if (user_interest == target_insterets)]



# main body

	# data part
users = [
	{ "id": 0, "name": "Hero" },
	{ "id": 1, "name": "Dunn" },
	{ "id": 2, "name": "Sue" },
	{ "id": 3, "name": "Chi" },
	{ "id": 4, "name": "Thor" },
	{ "id": 5, "name": "Clive" },
	{ "id": 6, "name": "Hicks" },
	{ "id": 7, "name": "Devin" },
	{ "id": 8, "name": "Kate" },
	{ "id": 9, "name": "Klein" }
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
	(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
interests = [
	(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
	(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
	(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
	(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
	(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
	(3, "statistics"), (3, "regression"), (3, "probability"),
	(4, "machine learning"), (4, "regression"), (4, "decision trees"),
	(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
	(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
	(6, "probability"), (6, "mathematics"), (6, "theory"),
	(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
	(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
	(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
	(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


    # execution part
for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

total_connections = sum(number_of_friends(user)for user in users) # 24


num_users = len(users) # length of the users list
avg_connections = total_connections / num_users # 2.4
# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))for user in users]


# num_friends_by_id = sorted(num_friends_by_id, # get it sorted
# 		key=lambda (user_id, num_friends): (num_friends), # by num_friends
# 		reverse=True) # largest to smallest
num_friends_by_id = sorted(num_friends_by_id, # get it sorted
		key=lambda USERS: USERS[1], # by num_friends
		reverse=True) # largest to smallest

print( [friend["id"] for friend in users[0]["friends"]] ) # [1, 2]
print( [friend["id"] for friend in users[1]["friends"]] ) # [0, 2, 3]
print( [friend["id"] for friend in users[2]["friends"]] ) # [0, 1, 3]
print( friends_of_friend_ids(users[3]) ) # Counter({0: 2, 5: 1})


# keys are interests, value are lists of user_id s with that interest
user_ids_by_interest = defaultdict(list)
# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    interests_by_user_id[user_id].append(interest)




