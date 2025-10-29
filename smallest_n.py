# Importing two modules
import sp.m_lists
from sp.two_smallest import find_two_smallest

# Defining and Opening the file
file_1 = "result.txt"
file = open(file_1, "w")

# Writing the smallest two numbers in lists
file.write(str(find_two_smallest(m_lists.l_1)))
file.write(str(find_two_smallest(m_lists.l_2)))
file.write(str(find_two_smallest(m_lists.l_3)))
file.write(str(find_two_smallest(m_lists.l_4)))
file.close()