# def greet_with(name,location):
#     print(f"hello {name}")
#     print(f"did you enjoy {location}")
# greet_with("sam","trivandrum")
def calculate_love_score(name1,name2):
    combined = (name1 + name2).lower()
    true_count = 0
    love_count = 0
    for letter in "true":
        true_count += combined.count(letter)
    for letter in "love":
        love_count += combined.count(letter)
    score = str(true_count) + str(love_count)
    print(f"Love score = {score}")
calculate_love_score("Kanye West", "Kim Kardashian")
            