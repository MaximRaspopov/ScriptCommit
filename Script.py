import os

os.chdir(input("Введите директорию проекта\n"))
print(os.listdir())

print("Введите название файлов которые хотите закомитить. Для выхода введите end")
end = ""
list = []

while True:
    end = input()
    if end == "end":
        break
    list.append(end)

for i in list:
    os.system("git add {}".format(i))

os.system("git commit -m 'sucess'")
os.system("git push")