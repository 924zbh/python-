for value in range (0,100,10):
    print(value)

numbers = list(range(0,100,10))
print(numbers)

squares = []
for value in range(0,11):
    square = value **2
    squares.append(square)

print(squares)

digits = [4,32,4,4,5,7,8,0,3,2,5,7,]
min(digits)
sum(digits)
squares = [value**2 for value in range(0,11)]
print(squares)

players = ["1","2","3"]
for player in players:
    print(player)

players = ["1","2","3"]
for player in players:
    print(f"{player.title()},that was a great trick!")
print("thanak you,everyone.that was a great competition!")

a = 1
b = 2
if a <= b:
    print("6")
else:
    print(9)

age = 14
if age < 4:
    print("your admission cost $0.")
elif age < 18:
    print("your admission cost $25.")
else:
    print("csot $40")

age = 14
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"your admission csot is ${price}")

age = 14
if age < 4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20

print(f"your admission cost is ${price}.")

bycles = ["1","2","3"]
request_bycles = ["1"]
print(f"give you {request_bycles}")

alien_0 = {"color":"green", "points":5}
print(alien_0["color"])
print(alien_0["points"])

alien_0 = {"color":"green","points":5}

new_points = alien_0["points"]
print(f"you just earned {new_points} points")

alien_0 = {"color":"green", "points":5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

alien_0 = {"color":"green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")
# 向右移动外星人
# 根据当前速度确定外星人向右移动多远
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    #这个外星人速度肯定很快
    x_increment = 3
    #新位置等于旧位置加上移动距离
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'rerd', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#创建一个用于储存外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")

aliens = []
for alien_number in range (30):
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('zhang')


def headsomeboy(username):
    print(f"Hello,the most headsome boy, {username.title()}")

headsomeboy('zhangbh')

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)    
    
