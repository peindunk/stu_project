import menu as m
import student_info as si
import sys



def main():
    infos=[]
    while True:
        m.output_menu()
        try:
            choice = input('请选择功能\n')
        except:
            print('输入有误')
            continue
        if choice== 'q':
            sys.exit()
        elif choice == '1':
            infos = si.input_student(infos)
        elif choice == '2':
            si.output_student(infos)
        elif choice == '3':
            infos = si.del_student_infos(infos)
        elif choice == '4':
            infos = si.modify_student_infos(infos)
        elif choice == '5':
            infos = si.sort_by_score_h2l(infos)
        elif choice == '6':
            infos = si.sort_by_score_l2h(infos)
        elif choice == '7':
            infos = si.sort_by_age_h2l(infos)
        elif choice == '8':
            infos = si.sort_by_age_l2h(infos)
        elif choice == '9':
            infos = si.get_info_from_file()
        elif choice == '10':
            si.save_info_to_file(infos)


if __name__ == '__main__':
    main()