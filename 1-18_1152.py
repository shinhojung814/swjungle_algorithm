# 1152. 단어의 개수
# https://www.acmicpc.net/problem/1152

input_str = str(input())
word_list = list(input_str.strip().split(' '))
word_count = 0

for word in word_list:
    word_count += 1

print(word_count)

words_list = input().split()
print(len(words_list))