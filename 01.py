import itertools,numpy, har
def transit(c,v):
    return c,v
def adsorb(c,v):
    # print("concentration ",c)
    return 1-0.4*numpy.exp(c),v
def mech(c,v):
    return 40-0.7*c,v
def revers(c,v):
    r=0.83
    return (1-r)*c,v/(1+1/r)
def best_scheme():
    dmax=ds[0]
    imax=0
    for i in range(len(ds)):
        if ds[i]>dmax:
            dmax=ds[i]
            imax=i
    return schemes[imax]

funcs = [mech,revers,transit]
# random.uniform(1,10)
cs,vs,ds,schemes = [],[],[],[]
for scheme in itertools.product(funcs, repeat=3):
    c,v=38,1
    assert len(scheme)>0
    for node in scheme:
        c,v = node(c,v)
    schemes.append(scheme)
    cs.append(c)
    vs.append(v)
    ds.append(har.d(c,v))

#ttprint(cs)
print(best_scheme())
