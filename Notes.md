-- DUPLICATE INTEGERS --

use a dictionary as they are very fast in terms of finding whether a key exist or not, find whether or not the number already existed inside of the dictionary, if no then add it in, if yes it means it does exist and we've seen the number before which we are able to conclude that they are a duplicate.

-- IS ANAGRAM --

use a dictionary again, for this one we make sure they are the same length first because its looking for anagram if they don't have the same length they are not an anagram. The next step is to loop through the whole string using the range because we want to check for those letters inside of two dictionary one for each word, we can use to map these letters based on the dictionary whether they exist or not. we use the get method and a default dict so we do not get a keyerror problem when we are trying to find something in that dictionary as we want to check first if they exist then we add if not we set the default values to be a 0. At the end of it we set to check as the result if the two dictionary are a match with each other which means they are an anagram which just means a word that has the same amount of letters and the same letters but in different orders.

-- TWO SUM -- 

use a dictionary again, we loop through the whole list, we want to check if the target value minus the value of the number on that index already existed in the dictionary or not ? If it does not exist then we add the number on that index into the dictionary. we don't need to think of an edge case as the question specified that there is always going to be a result from the list.