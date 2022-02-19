import sys
num = sys.argv[1]
in_file = open("edge.facts", 'w')
for i in range(int(num)):
    in_file.write("{}\t{}\n".format(i, i+1))
