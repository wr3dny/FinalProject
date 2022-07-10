filename = 'high_score.txt'

def score_save(score):
    with open(filename, 'a') as f:
        f.write('\\n' + score)
        f.close()


def score_read():
    with open('high_score.txt', 'r+') as f:
        content = f.readline()
        f.close()
        return content


def main():
    bla = 'bla'
    score_save(bla)
    hs = score_read()
    print(hs)


if __name__ == '__main()__':
    main()