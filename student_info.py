import stu_class as sc

#　输出学生信息　并　打印
def output_student(infos):
    print('+-------------+----------+--------+')
    print('|    姓名     |   年龄   |   成绩 |')
    print('+-------------+----------+--------+')

    for item in infos:
        print('|'+item.name.center(13)+'|'+str(item.age).center(10)+'|'+str(item.score).center(8)+'|')

    print('+-------------+----------+--------+')

# 输入添加学生信息
def input_student(infos):
    while True:
        try:
            n = input('请输入学生姓名')
            if not n:
                break
            a = int(input('请输入学生年龄'))
            s = int(input('请输入学生成绩'))
        except:
            print('输入有误')
            return infos
        # d=dict(name = n, age = a, score = s)
        stu = sc.Student(n,a,s)
        infos.append(stu)
    return infos

# 删除学生信息
def del_student_infos(infos):
    if infos:
        s = input('请输入您要删除的学生姓名')
        for item in infos:
            if s == item.name:
                infos.remove(item)
                print('删除成功')
                return infos
        else:
            print('您要删除的信息不存在')
            return infos
    else:
        print('学生信息为空')
        return infos

# 修改学生信息
def modify_student_infos(infos):
    if infos:
        s = input('请输入您要修改的学生姓名')
        for item in infos:
            if s == item.name:
                # item['name'] = input('请输入要修改的修改的名字')
                item.age = int(input('请输入你要修改的年龄'))
                item.score = int(input('请输入你要修改的成绩'))
                print('修改成功')
                return infos
        else:
            print('学生信息不存在')
            return infos
    else:
        print('学生信息为空')
        return infos

def sort_by_score_h2l(infos):
    return sorted(infos,key=lambda x:x.score,reverse=True)

def sort_by_score_l2h(infos):
    return sorted(infos,key=lambda x:x.score)

def sort_by_age_h2l(infos):
    return sorted(infos,key=lambda x:x.age,reverse=True)

def sort_by_age_l2h(infos):
    return sorted(infos,key=lambda x:x.age)

def get_info_from_file():
    infos = []
    filename = 'si.txt'
    with open(filename) as f:
        while True:
            s = f.readline().strip()
            if not s:
                break
            l = s.split(',')
            # d = dict(name=l[0],age=int(l[1]),score=int(l[2]))
            stu = sc.Student(l[0],l[1],l[2])
            infos.append(stu)
    return infos

def save_info_to_file(infos):
    if not infos:
        print('无需要保存的信息')
        return infos
    filename = 'si.txt'
    with open(filename,'a') as f:
        for d in infos:
            f.write('%s,%s,%s\n'%(d.name,str(d.age),str(d.score)))
