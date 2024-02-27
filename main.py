
V, C = map(int, input().split())


lst =  ['НӨЛ', "БИР", "ЭКИ", "ҮЧ", "ТӨРТ",
        "БЕШ", "АЛТЫ", "ЖЕТИ", "СЕГИЗ", "ТОГУЗ" ]



mas_v = ['Ө', "И", 'У', 'Ү', 'А', 'Е', 'Ы', 'О', "Э" ]



def func(V, C):
    comb = []
    for i in range(101):

        
        
        s = str(i)

        l = []

        for i in range(len(s)):
            l.append(s[i])


        s = ''
        
        for i in range(len(l)):
            s += lst[int(l[i])]

        vc = 0
        cc = 0
        
        for i in range(len(s)):
            if s[i] in mas_v:
                vc+=1

            else:
                cc+=1
        
        if vc == V and cc == C:
            s1 = ""
            for i in range(len(l)):
                s1 += l[i]

            comb.append(int(s1))


    return max(comb)


print(func(V, C))
        















        






