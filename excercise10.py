# Start out by creating the following dictionary representing the number of students in past Bitmaker cohorts:
#
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}
# Create a method that displays the name and number of students for each cohort, like so:
def list_cohorts(cohort_dict):
    for cohort, size in cohort_dict.items():
        print('{}: {} students'.format(cohort,size))

list_cohorts(students)
# Add cohort 4, which had 43 students, to the dictionary.
students['cohort4'] = 43
# Use the keys method to output all of the cohort names.
print(students.keys())
# The classrooms have been expanded! Increase each cohort size by 5% and display the new results.
def increase_cohort(cohort_dict,percent):
    for cohort, size in cohort_dict.items():
        cohort_dict[cohort] = int(size * (1 + percent / 100))
increase_cohort(students,5)
print(students)

# Delete the 2nd cohort and redisplay the dictionary.
students.pop('cohort2')
print(students)
# BONUS: Calculate the total number of students across all cohorts using a for loop. Output the result.
total_students = 0
for cohort, size in students.items():
    total_students += size

print('The total number of students across all cohorts is {}.'.format(total_students))
