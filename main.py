from testing import *

# experiment 1
for i in range(7, 16):
    algs1 = case_1(i)
    print(algs1)

# experiment 2
for j in range(7, 16):
    results = []
    lst = generate_sorted(j)
    results.append(test_selection(deepcopy(lst)))
    results.append(test_insertion(deepcopy(lst)))
    results.append(test_merge(deepcopy(lst)))
    results.append(test_shell(deepcopy(lst), j))
    print(f"Time for 2**{j} Insertion")
    print(results)

# experiment 3D
for k in range(7, 16):
    s_lst = generate_sorted(k)[::-1]
    resultss = []
    resultss.append(test_selection(deepcopy(s_lst)))
    resultss.append(test_insertion(deepcopy(s_lst)))
    resultss.append(test_merge(deepcopy(s_lst)))
    resultss.append(test_shell(deepcopy(s_lst), k))
    print(f"Time for 2**{k} S/I/M/Sh:")
    print(resultss)

# experiment 4
for l in range(7, 16):
    algs4 = case_4(l)
    print(algs4)
