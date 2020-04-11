#StudentManagementSystem.py
import time 
#初始化：
#设置起始时间戳
start = time.perf_counter()
#全局定义：
#学生信息总类"次数"：listtime = lt
lt = 3
#学生人数为：sum
sum = 0
#循环介质置零： i
i = 0
#内嵌默认管理员账户
defaultuser = {'name':'admin', 'passwd':'passwd'} 
#检索现有的学生内容：
try: 
    file=open('default.txt',"r", encoding = 'utf-8')    
except FileNotFoundError:          
    print("The Student Managerment Is Empty Now")
else:
    contents=file.readlines() 
#将默认学生信息导入至学生列表：       
    student = []
    for content in contents:       
        student.append(content[3:-1])
    tempsum = int(len(student)/lt)
#用户登录代码
def login(shutdown): 
    with open("users.txt", 'r+', encoding='utf-8') as f:
        getinformation = f.readlines() 
        tempuserslist = [] 
        for count in range(3): 
            name = input('请输入用户名： ')
            password = input('请输入密码： ')
            for getit in getinformation: 
                tempuserslist.append(getit) 
            for gettemplistline in tempuserslist: 
                users = eval(gettemplistline) 
                if (name == users['name'] and password == users['passwd']) or (name == defaultuser['name'] and password == defaultuser['passwd']):
                    print(  '登录成功！')
                    shutdown = 1 
                    return shutdown 
            if (not(name == users['name'] and password == users['passwd']) or (name == defaultuser['name'] and password == defaultuser['passwd'])):
                lost = 2 - count 
                if count < 2:
                    print('用户名或密码错误,还有{:}次机会'.format(lost))
                else:
                    alertexit = '输入错误次数过多，程序终止' 
                    print(alertexit)
                    shutdown = 0 
                    return shutdown                                 
        f.close()
#选择输出文本代码
def chooseoutput (name, tempcondition):
    for i in range(lt * sum): 
        if tempcondition in student[i]: 
            with open (name, "a+", encoding = 'utf-8') as f:
                p = ('姓名：' + student[i - 1] + "\n" + '性别：' + student[i] + "\n" + '学号：' + student[i + 1]) #设置输出附加语句
                f.writelines(p + "\n")
                pass
            f.close()
#全输出文本代码
def alloutput(name):
    with open (name, "a+", encoding = 'utf-8') as f:
        for i in range(len(student)): 
            if i % lt == 0: 
                p = ('姓名：' + student[i] + "\n" + '性别：' + student[i + 1] + "\n" + '学号：' + student[i + 2])
                f.writelines(p + "\n")
                pass
            else:
                continue
        f.close()
#清空文本代码
def coveroutput():
    with open ('default.txt', "a+", encoding = 'utf-8') as f:
        f.seek(0) 
        f.truncate() 
        pass
        f.close()
#进度条代码：
scale = 50
print('加载中'.center(scale//2, '-'))
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n'+'加载完成'.center(scale//2,'-'))
#首页：
print('1.注册', '2.登录')
choosefirst = input('请选择：')
#用户管理：
#普通用户注册
if choosefirst == '1': 
    with open("users.txt", 'r+', encoding='utf-8') as f:
        information = f.readlines()
        for it in information:
            it = it.strip() 
            users = eval(it) 
        for i in range(4):
            name = input('请输入用户名：')
            passwd = input('请输入密码：')
            again_passwd = input('请再次输入密码：')
            if len(name.strip()) != 0 and name != users['name'] and len(passwd.strip()) != 0 and passwd == again_passwd:
                users = {'name': name, 'passwd': passwd} 
                f.writelines(str(users) + '\n') 
                print('恭喜，注册成功')
                f.close()
                break
            elif len(name.strip()) == 0:
                print('用户名不能为空，请重新输入。还可输入%d次' %(3-i))
            elif name == users['name']:
                print('用户名重复，请重新输入。还可输入%d次' %(3-i))
            elif len(passwd.strip()) == 0:
                print('密码不能为空，请重新输入。还可输入%d次' %(3-i))
            elif again_passwd != passwd:
                print('两次输入的密码不一致，请重新输入。还可输入%d次' %(3-i))
    shutdown = login(1) #注册之后强制登录
#用户登录
elif choosefirst == '2':
    shutdown = login(1)
#主界面：
while(1):
    if shutdown == 0:
        break
    line1 = ['学生管理系统']
    print(line1)
    line2 = ['0.初始录入' , '1.增添学生' , '2.删除学生 ', '3.更改信息 ', '4.筛选学生 ', '5.输出所有学生信息', '6.退出系统', '7.查询版本']
    print(line2)
    #用户选择代码
    choose = input( '请选择你需要的功能:')
    #0.初始学生录入代码
    if choose == '0':
        alert0 = input( '选择初始录入会清空现有学生数据，你是否要继续：')
        if alert0 == '是':
            tempsum = 0
            student = []
            sum = int( input( '请输入学生人数:'))
            for i in range(sum):
                name=input('请输入姓名:')
                student.append(name)
                sex=input('请输入性别:')
                student.append(sex)
                stuid=input('请输入学号:')
                student.append(stuid)
            if len(student) == lt * sum:
                print('初始录入学生信息成功')
                m =input( '是否显示当前学生信息:')
                if m == '是':
                    print(student)
            else:
                print('信息录入失败')
    #1.增添学生代码
    elif choose == '1':
        newsum = int( input( '请输入新增的学生人数:'))
        for i in range(newsum):
            name=input('请输入姓名:')
            student.append(name)
            sex=input('请输入性别:')
            student.append(sex)
            stuid=input('请输入学号:')
            student.append(stuid)
        sum = sum + newsum + tempsum
        if len(student) == lt * sum:
            print('增添学生信息成功')
            m =input( '是否显示当前学生信息:')
            if m == '是':
                print(student)
        else:
            print('信息录入失败')
    #2.删除学生代码
    elif choose == '2':
        condition = input('请输入要删除学生的姓名:')
        if sum == 0:
            sum = tempsum
        for i in range(lt * sum):
            if condition == student[i]:
                del student[i:i + lt]
                sum = sum - 1
                break
        if len(student) == lt * sum:
            print('删除学生信息成功')
            m =input( '是否显示当前学生信息:')
            if m == '是':
                print(student)
        else:
            print('信息删除失败')
    #3.更改学生信息代码
    elif choose == '3':
        if sum == 0:
            sum = tempsum
        condition = input('请输入要修改的学生姓名:')
        choosechange = input('请输入要修改的内容：【1.性别 2.学号】：')
        if choosechange == '1':
            tempsex = input('请输入修改后的性别：')
            for i in range(lt * sum):
                if student[i] == condition:
                    student[i + 1] = tempsex
        elif choosechange == '2':
            tempstuid = input('请输入修改后的学号：')
            for i in range(lt * sum):
                if student[i] == condition:
                    student[i + 2] = tempstuid
        if condition in student:
            print('更改学生信息成功')
        else:                
            print('更改学生信息失败')
        m = input( '是否显示当前学生信息:')
        if m == '是':
            print(student)
    #4.筛选学生信息代码
    elif choose == '4':
        if sum == 0:
            sum = tempsum    
        choosename = input('请输入文件名：')
        choosesex = input( '请输入筛选性别:')
        chooseoutput(choosename,choosesex)
        print('已输出筛选的学生信息')
    #5.全输出
    elif choose == '5':
        choosename = input('请输入文件名：')
        alloutput(choosename)
        print('已全部输出')
    #6.系统退出
    elif choose == '6':
        alert = input('是否保存修改：')
        if alert == '是':
            coveroutput()
            alloutput('default.txt')
        print('系统退出')
        break
    #7.查询版本
    elif choose == '7':
        print('version-5.2')
    