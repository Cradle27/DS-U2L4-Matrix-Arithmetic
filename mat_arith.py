# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE


def mat_sum(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        height = len(m1)
        width = len(m1[0])
        new = [m1[h] + m2[h] * width for h in range(height)]
        m3 = [[] * height]
        for i in range(len(m3)):
            m3[i].append(new[0:4])
            m3[i].remove(new[0:4])
            return m3
    else:
        return "No solution"

def mat_mul(m1, m2):
    row1 = len(m1)
    row2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])
    if row2 == col1:
      m3 = [[0] * col2 for i in range(row1)]
      for ind, row in enumerate(m3):
        for ind2, col in enumerate(row):
          num = 0
          for e in range(len(m1[ind])):
            num += (m1[ind][e] * m2[e][ind2])
          m3[ind][ind2] = num
      return m3
    
    else:
        return "No solution"
