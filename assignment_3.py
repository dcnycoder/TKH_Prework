names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
longest_name = ''

for name in names_list:
    if len(name)>len(longest_name):
        longest_name = name
print(longest_name)
