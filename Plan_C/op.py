

def file_open():
    with open('high_score.txt', 'r') as f:
        last_ten_lines = f.readlines()[-11:-1]
        return last_ten_lines

# def show(lines):
#     lines = lines.strip('\n')
#     # lines = lines.split(' - ')
#     print(lines)

    




def file_save(added):
    with open('high_score.txt', 'a+') as f:
        f.write('\n' + added)
        content = f.readline()
        print(content)


file_save('Gdynia')
ten_line = file_open()
print(*ten_line, sep='\n')
# show(ten_line)






