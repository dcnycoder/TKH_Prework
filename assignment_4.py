names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

def findLongest(list):
    longest_name = ''
    for name in list:
        if len(name)>len(longest_name):
            longest_name = name
    return longest_name

big_name = findLongest(names_list)
print (big_name)