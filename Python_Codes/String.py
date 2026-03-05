message=" Hello Python, This is showman"
# print(message)

# indexing or slicing 

# print(message[0:5]) #Hell
# print(message[-7:]) #showman
# print(message[-7:-2]) #showm

txt="visit###earth!!"
clean_txt=txt.replace("#"," ").replace("!",'')
# print(clean_txt)
#capitalize
# print(clean_txt.upper())

# string concatenation

sen_1="Showman"
sen_2="das"
# print("Full sentence : ",sen_1 + "#" + sen_2)

sentence="Greetings from {} ! {}.".format(sen_1,sen_2)
# print(sentence)
sentence_2=f"Greetings from {sen_1} ! {sen_2}."
# print(sentence_2)

# count any letter / word

# print(sentence_2.count('o')) # 2

print(sentence.split())  #list
