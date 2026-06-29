states = ["DELHI", "UTTAR PRADESH", "UTTARAKHAND", "SIKKIM"]

# print(states[2])
# print(states[-1])
states[1] = "JAMMU & KASHMIR"
print(states)

states.append("Lalaland")
print(states)

states.pop()
print(states)

states.extend(["PUNJAB" ,"HIMACHAL"])
print(states)