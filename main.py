baz_txt = ['1.txt', '2.txt', '3.txt']
txt_sort = {}

for file_txt in baz_txt:
    with open(file_txt, 'rt', encoding='utf-8') as file:
        for count, line in enumerate(file):
            pass
        txt_sort[file_txt] = count+1
list_txt = sorted(txt_sort, key=txt_sort.get)

for txt in list_txt:
    print(txt)
    print(txt_sort[txt])
    with open(txt, 'rt', encoding='utf-8') as file:
        oll_txt = file.read()
        print(oll_txt)