# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:03:48 2018

@author: hila
"""
def compare_subjects_within_students(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    student_name_subj1=set(subj1_all_students)
    student_name_subj2=set(subj2_all_students)
    subj=[]
    subj.append(subj1_all_students['subj'])
    subj.append(subj2_all_students['subj'])
    student_both_grades=student_name_subj1.intersection(student_name_subj2)
    student_both_grades=student_both_grades.difference({'subj'})
    student_best_subj=dict()
    for i in student_both_grades:
        subj1_all_students[i]=max(subj1_all_students[i])
        subj2_all_students[i]=max(subj2_all_students[i])
        if subj1_all_students[i]==subj2_all_students[i]:
            student_best_subj[i]=(subj)
        else:
            if subj1_all_students[i]<subj2_all_students[i]:
                student_best_subj[i]=subj[1]
            else:
                student_best_subj[i]=subj[0]
    return(student_best_subj)

if __name__ == '__main__':
    art={'subj':'art','Dana':[95,90],'Ori':[75,65],'Dan':[85,100],'Michal':[70,90]}
    math={'subj':'math','Dana':[95,100],'Oren':[70,85],'Dan':[85,95],'Michal':[95,90]}
    result3=compare_subjects_within_students(art,math)
    print('Question 3 solution: \n' + str(result3))
    