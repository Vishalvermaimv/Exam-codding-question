class TestSample :
    @staticmethod
    def main( args) :
        scanner =  "Python-inputs"
        students = input()
        subjects = input()
        marks = [[0] * (subjects) for _ in range(students)]
        row = 0
        while (row < students) :
            col = 0
            while (col < subjects) :
                marks[row][col] = input()
                col += 1
            row += 1
        scanner.close()
        avg = [0] * (subjects)
        min = -1
        skipIndex = -1
        sub = 0
        while (sub < subjects) :
            stu = 0
            while (stu < students) :
                avg[sub] += marks[stu][sub]
                stu += 1
            avg[sub] /= students
            if (sub == 0) :
                min = avg[0]
                skipIndex = 0
            elif(avg[sub] < min) :
                min = avg[sub]
                skipIndex = sub
            sub += 1
        result = [0] * (students)
        row = 0
        while (row < students) :
            col = 0
            while (col < subjects) :
                if (skipIndex != col) :
                    result[row] += marks[row][col]
                col += 1
            row += 1
        for mark in result :
            print(str(mark) + " ", end ="")
    

if __name__=="__main__":
    TestSample.main([])