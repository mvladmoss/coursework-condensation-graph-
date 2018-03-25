data = []
array = []
new_component = []
components = []
with open("TEST1.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
        # Считываю кол-во вершин и ребер, а затем пары чисел и записываю в их
        # в виде списка из 2 элементов в список data
number_of_point = (int(data[0][0]))
number_of_edge = (int(data[1][0]))
graph = list([] for i in range(number_of_point + 1))
Tgraph = list([] for i in range(number_of_point + 1))
used = [False for i in range(number_of_point + 1)]
for i in range(2, number_of_edge + 2):
    if data[i][1] not in graph[data[i][0]]:
        graph[data[i][0]].append(data[i][1])
    if data[i][0] not in Tgraph[data[i][1]]:
        Tgraph[data[i][1]].append(data[i][0])


def dfs1(v):
    used[v] = True
    for i in range(len(graph[v])):  
        if not used[graph[v][i]]:
            dfs1(graph[v][i])
    array.append(v)


def dfs2(v, temp):
    used[v] = True
    temp.append(v)
    for i in range(len(Tgraph[v])):
        if not used[Tgraph[v][i]]:
            dfs2(Tgraph[v][i], temp)
    return temp


def restart_used():
    for i in range(number_of_point + 1):
        used[i] = False    


def main():
    for i in range(1, number_of_point + 1):
        if not used[i]:
            dfs1(i)
    print(array)
    restart_used()
    for i in range(1, number_of_edge + 1):
        v = array[number_of_point - i]
        if not used[v]:
            temp = []
            new_component = dfs2(v, temp)
            components.append(new_component)
    print("Компоненты сильной связности:")
    count = 0
    for i in components:
        print(str(count + 1) + ")", end="")
        print("{ ", end="")
        for t in i:
            print(str(t) + " ", end="")
        print("}")
        count = count + 1
    count = 0
    print("Граф конденсации в виде списка смежности")
    condencat_graph = list([] for i in range(len(components)))
    for k in range(len(components)):
        for t in components[k]:
            for temp in graph[t]:
                if temp not in components[k]:
                    for qwerty in range(len(components)):
                        if temp in components[qwerty]:
                            if (qwerty + 1) not in condencat_graph[k]:
                                condencat_graph[k].append(qwerty + 1)
    count = 1
    for k in condencat_graph:
        print(str(count) + "){ ", end="")
        for t in k:
            print(t, end=" ")                
        count = count + 1
        print("}")    
                    

main()
