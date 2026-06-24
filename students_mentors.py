# Variables for the students and mentors
students = ['Emma','Liam','Olivia','Noah','Ava','William','Isabella','James','Sophia','Logan','Mia','Elijah','Charlotte','Carter','Amelia','Oliver','Evelyn','Mason','Harper','Ethan','Emily','Alexander','Avery','Sebastian','Scarlett','Michael','Grace','Daniel','Chloe','Jacob','Zoey','Benjamin','Lily','Luke','Madison','Matthew','Aubrey','Henry','Layla','Joseph','Lillian','Caleb','Nora','Wyatt','Elizabeth','Owen','Abigail','Jack','Ella','Samuel','Addison']
mentors = {
    'Alice': 0,
    'Charlie': 0,
    'David': 0,
    'Olaf': 0
} 

# Function to divide students into groups
def divide_students(students, num_groups):
    group_size = len(students) // num_groups
    return [students[i:i+group_size] for i in range(0, len(students), group_size)]

def assign_mentors(groups, mentors):
    sorted_mentors = sorted(mentors.items(), key=lambda x: x[1])
    mentors_list = [mentor[0] for mentor in sorted_mentors]

    result = {}
    for idx, group in enumerate(groups):
        mentor = mentors_list[idx % len(mentors_list)]
        result[f'Group {idx+1}'] = {'Students': group, 'Mentor': mentor}
        mentors[mentor] += 1

    return result 

count_students = len(students)
num_groups = len(mentors)
groups = divide_students(students, num_groups)
student_by_group = assign_mentors(groups, mentors)
print(student_by_group)
