from sys import argv
import numpy as np

if __name__ == '__main__':
    inputfile = argv[1]
    output = open(argv[2], 'w')
    columns = 'eval\tacc\tmcc\ttp\tfp\tfn\ttn\n'
    output.write(columns)
    # eval_t = float(argv[2])

    # print(eval_t)

    for i in range(-20,1):
        eval_t = 1.0*(10**i)
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        with open(inputfile) as file:
            for line in file:
                line = line.rstrip().split()
                # print(line)
                if (float(line[1]) <= eval_t) and (line[2] == '1'): tp += 1
                if (float(line[1]) <= eval_t) and (line[2] == '0'): fp += 1
                if (float(line[1]) > eval_t) and (line[2] == '1'): fn += 1
                if (float(line[1]) > eval_t) and (line[2] == '0'): tn += 1
            matrix = [[tp, fp], [fn, tn]]
            acc = (tp+tn)/(tp+tn+fn+fp)
            mcc = ((tp*tn)-(fp*fn))/np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
            out = str(eval_t) + '\t' + str(acc) + '\t' + str(mcc) + '\t' + str(matrix[0][0]) + '\t' + str(matrix[0][1]) + '\t' + str(matrix[1][0]) + '\t' + str(matrix[1][1]) + '\n'
        print(out)
        output.write(out)

    output.close()