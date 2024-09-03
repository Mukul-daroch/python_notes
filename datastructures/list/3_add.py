list = [" ", " ", " ", " "]
print("_____________________________________________")
print(f"{'list'}                 {list}")
print("---------------------------------------------")
# extend ------------------------------------------
list = [" ", " ", " ", " "]
listx = ["0", "1", "2"]
print("list=              >", list)
print("listx=              >", listx)
list.extend(listx)
print("list.extend(listx) >", list, "\n")
# ------------------------------------------
print("                    >", list)
list.insert(2, "X")
print("list.insert(2,'X') >", list, "\n")
# ------------------------------------------
list = [" ", " ", " ", " "]
print("                    >", list)
list.append("X")
print("list.append('X')   >", list, "\n")
