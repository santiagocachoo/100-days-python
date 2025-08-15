# create a letter using starting_letter.txt
# for each name in invited_names.txt
# replace the [name] placeholder with the actual name
# save the letters in the folder "ready_to_send"


clean_names = []
with open("/Users/santiagocachoh/Code/100python/dia_24/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()
    for name in names:
        name = name.strip()
        clean_names.append(name)

with open("/Users/santiagocachoh/Code/100python/dia_24/starting_letter.txt", "r") as starting_letter:
    starting_letter = starting_letter.read()

for name in clean_names:
    custom_file = open(f"/Users/santiagocachoh/Code/100python/dia_24/ready_to_send/letter_for_{name}.txt", "w")
    custom_letter = starting_letter.replace("[name]", name)
    custom_file.write(custom_letter)
    






        
        

        
              


 