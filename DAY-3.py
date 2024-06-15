#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day3


# In[2]:


import random

def power(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p

    return res

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Find r such that n = 2^r * d + 1
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True
num = int(input("Enter a number to test for primality: "))
iterations = 5  

if miller_rabin(num, iterations):
    print(f"{num} is likely prime.")
else:
    print(f"{num} is composite.")


# In[4]:


def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence
def display_fibonacci(sequence):
    print("Fibonacci Sequence:")
    for term in sequence:
        print(term, end=" ")

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

fib_sequence = generate_fibonacci(num_terms)
display_fibonacci(fib_sequence)


# In[2]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_next_prime(N):
    next_prime = N + 1
    while True:
        if is_prime(next_prime):
            return next_prime
        next_prime += 1

def smallest_prime_larger_than_N(N):
    return find_next_prime(N)

def sum_of_primes_between_N_and_next_prime(N):
    next_prime = find_next_prime(N)
    prime_sum = 0
    for num in range(N + 1, next_prime):
        if is_prime(num):
            prime_sum += num
    return prime_sum

def product_of_next_two_primes_is_prime(N):
    next_prime = find_next_prime(N)
    next_next_prime = find_next_prime(next_prime)
    product = next_prime * next_next_prime
    return is_prime(product)

def solve_puzzle(N):
    level_1_result = smallest_prime_larger_than_N(N)
    level_2_result = sum_of_primes_between_N_and_next_prime(N)
    level_3_result = product_of_next_two_primes_is_prime(N)
    return (level_1_result, level_2_result, level_3_result)

# Test the function
N = int(input("Enter the value of N:"))
puzzle_results = solve_puzzle(N)
print("Results of the puzzle for N =", N)
print("Level 1: Smallest prime larger than N -", puzzle_results[0])
print("Level 2: Sum of primes between N and the smallest prime larger than N -", puzzle_results[1])
print("Level 3: Is the product of the next two primes prime? -", puzzle_results[2])


# In[3]:


N= int(input("Enter the value of N:"))
flag=(0)
k=N+1
while flag>1:
    check_prime(k)


# In[7]:


n=int(input("Enter the number:"))
flag=True
while flag:
    n+=1
    count=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            count+=1
    if count==0:
         print(n)
         flag=False


# In[8]:


def party(time,nos):
    count=0
    req=0
    for i in range(1,nos+1):
        req+=i*5
        if req<=time:
            count+=1
        else:
            break
    return count
print("Time deadline: 8pm")
start=8*60
t=int(input("Enter the present time:"))
t=t*60
nos=int(input("Enter the number of problems:"))
print("The number of possible questions can be solved are:",party(start-t,nos))


# In[1]:


def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(1, num_players + 1):
        player_name = input(f"Enter name of player {i}: ")
        players.append(player_name)
    
    max_vowels = 0
    winner = ""
    
    for player in players:
        word = input(f"{player}, please say a word: ")
        vowel_count = count_vowels(word)
        print(f"Number of vowels in {word}: {vowel_count}")
        
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            winner = player
    
    print(f"\nThe winner is {winner} with {max_vowels} vowels!")

if __name__ == "__main__":
    main()


# In[2]:


def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in word if char in vowels)
    return vowel_count

def main():
    num_players = int(input("Enter the number of players: "))
    players = []

    # Gather player names
    for i in range(1, num_players + 1):
        player_name = input(f"Enter name of player {i}: ")
        players.append(player_name)
    
    max_vowels = 0
    winner = ""

    # Game loop
    for player in players:
        word = input(f"{player}, please say a word: ")
        vowel_count = count_vowels(word)
        print(f"Number of vowels in {word}: {vowel_count}")

        # Determine winner based on vowel count
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            winner = player
    
    # Announce the winner
    print(f"\nThe winner is {winner} with {max_vowels} vowels!")

if __name__ == "__main__":
    main()


# In[ ]:


def vowels(sent):
    dic = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
    }
    sent = str(sent)
    sent = sent.lower()
    dic['a'] = sent.count('a')
    dic['e'] = sent.count('e')
    dic['i'] = sent.count('i')
    dic['o'] = sent.count('o')
    dic['u'] = sent.count('u')
    
    for key, value in dic.items():
        print(key, value)
    
    maxi = 0
    keyy = None
    for key, value in dic.items():
        if value > maxi:
            maxi = value
            keyy = key
    
    print("The max count of the vowel is", keyy, ":", dic[keyy])

while Trque:
    sent = input("Enter the sentence:")
    vowels(sent)


# In[1]:


'''game={}
def do(name,string):
    a,e,i,o,u,A,E,I,O,U=0,0,0,0,0,0,0,0,0,0
    for i in range(o,len(string)):
        if i=='a':
            a+=1
        elif string[i]=='e':
            e+=1
        elif string[i]=='i':
            i+=1
        elif string[i]=='o':
            o+=1
        elif string[i]=='u':
            u+=1
        elif string[i]=='A':
            A+=1
        elif string[i]=='E':
            E+=1
        elif string[i]=='I':
            I+=1
        elif string[i]=='O':
            O+=1
        elif string[i]=='U':
            U+=1
        else:
            print('invalid')
        game[i]
    
    players=input('enter the number of players')
    print('number of players are:',players)
    for i in range(0,len(players)):
        name=input('Name:')
        sentence=input('sentence:')
        game[name]=sentence
        do(game[name]) 
        '''
        
        
        
        
        
        
        
def count_vowel(S):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in S:
        if i == 'a' or i == 'A':
            dic['A']+=1
        elif i == 'e' or i=='E':
            dic['E']+=1
        elif i == 'i' or i=='I':
            dic['I']+=1
        elif i == 'o' or i=='O':
            dic['O']+=1
        elif i == 'u' or i=='U':
            dic['U']+=1
    x=max(dic.values())
    result=[]
    for i,j in dic.items():
        if j==x:
         result.append(i)
    return result

i_p = [
       ['sameer','my name is bhagya'],
       ['tania','my name is indra'],
       ['goutham','my name is isaaq'],
       ['abhilash','my name is ganesh'],
       ['asstin','my name is rithvik']
       ]
o_p = {}
for i in i_p:
    o_p[i[0]] = count_vowel(i_p[i[1]])
print(o_p)


# In[2]:


def count_vowel(S):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in S:
        if i == 'a' or i == 'A':
            dic['A'] += 1
        elif i == 'e' or i == 'E':
            dic['E'] += 1
        elif i == 'i' or i == 'I':
            dic['I'] += 1
        elif i == 'o' or i == 'O':
            dic['O'] += 1
        elif i == 'u' or i == 'U':
            dic['U'] += 1
    max_count = max(dic.values())
    result = [key for key, value in dic.items() if value == max_count]
    return result

input_players = [
    ['sameer', 'my name is bhagya'],
    ['tania', 'my name is indra'],
    ['goutham', 'my name is isaaq'],
    ['abhilash', 'my name is ganesh'],
    ['asstin', 'my name is rithvik']
]

output_players = {}

for player_info in input_players:
    name = player_info[0]
    sentence = player_info[1]
    vowels_max = count_vowel(sentence)
    output_players[name] = vowels_max

print(output_players)


# In[ ]:




