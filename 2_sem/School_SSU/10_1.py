## по должности, при равенстве по возрастанию опыта работы

def vacancies(file):
    hh = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            titles = line.strip().split(';')
            if len(titles) == 4:
                company, position, salary, experience = titles
                hh.append({
                    'company': company, 'position': position,
                    'salary': salary, 'experience': experience
                })
    return hh


def buble_sort(hh):
    n = len(hh) - 1
    for i in range(n):
        for j in range(n - i):
            if (hh[j]['position'] > hh[j + 1]['position'] or
                    (hh[j]['position'] == hh[j + 1]['position'] and hh[j]['experience'] > hh[j + 1]['experience'])):
                hh[j]['position'], hh[j + 1]['position'] = hh[j + 1]['position'], hh[j]['position']


def sel_sort(hh):
    n = len(hh)
    for i in range(n - 1):
        m = i
        for j in range(i + 1):
            if (hh[j]['position'] < hh[m]['position'] or
                    (hh[j]['position'] == hh[m]['position'] and hh[j]['experience'] < hh[m]['experience'])):
                m = j
        hh[i]['position'], hh[m]['position'] = hh[m]['position'], hh[i]['position']


def sel_sort_stable(hh):
    n = len(hh)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if (hh[j]['position'] < hh[m]['position'] or
                    (hh[j]['position'] == hh[m]['position'] and hh[j]['experience'] < hh[m]['experience'])):
                m = j
        min_val = hh[m]
        for k in range(m, i, -1):
            hh[k] = hh[k - 1]
        hh[i] = min_val


def insertion_sort(hh):
    n = len(hh)
    for i in range(1, n):
        j = i

        while (j > 0 and hh[j - 1]['position'] > hh[i]['position'] or
               (hh[j - 1]['position'] == hh[i]['position'] and hh[j - 1]['experience'] > hh[i]['experience'])):
            hh[j]['position'] = hh[j - 1]['position']

        hh[j]['position'] = hh[i]['position']

file = '../../../school_SSU/hh.txt'
work = vacancies(file)

bubble, sel, stable_sel, insertion = work.copy(), work.copy(), work.copy(), work.copy()
buble_sort(bubble)
sel_sort(sel)
sel_sort_stable(stable_sel)
insertion_sort(insertion)

print(bubble)
print(sel)
print(stable_sel)
print(insertion)
