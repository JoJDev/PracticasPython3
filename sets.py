s = set([1,2,3]);
t = set([3,4,5]);

print(s.union(t));
print(s.intersection(t));
print(s.difference(t));
1 in s;
1 in t;
2 not in s;
2 not in t;

print((s.difference(t)).union(t.difference(s)));
    # union de la diferencia de t en s y de s en t