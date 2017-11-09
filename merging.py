import pandas as pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director'},
                         {'Name': 'Kelly', 'Role': 'Course Liaison'},
                         {'Name': 'james', 'Role': 'grader'}])

staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'james', 'school': 'grader'},
                           {'Name': 'mike', 'school': 'grader'},
                           {'Name': 'sally', 'school': 'grader'}])
student_df = student_df.set_index('Name')
#
# print(staff_df)
# print()
# print(student_df)
#

whack1 = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
whack2 = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
whack2 = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
whack2 = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# print(whack1)
print(whack2)

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
print(pd.merge(staff_df,student_df,how='inner', left_on=['First Name', 'Last Name'],right_on=['First Name', 'Last Name']))
