from blocks import *
import har


def best_scheme():
    dmax = ds[0]
    imax = 0
    for i in range(len(ds)):
        if ds[i] > dmax:
            dmax = ds[i]
            imax = i
    return schemes[imax]


C_START = 35
funcs = [mech, adsorb,revers, transit]
# random.uniform(1,10)
cs, vs, ds, schemes = [], [], [], []
for scheme in itertools.product(funcs, repeat=3):
    if not is_valid(scheme):
        continue
    c, v = C_START, 1
    for node in scheme:
        c0 = c
        c, v = node(c, v)
        if (c < 0) or (c > c0):
            break

    if 0 < c < C_START:
        print('---------------')
        # print(c>0 and c< C_START)
        print(c)
        print('calculated for ' + str(del_transit(scheme)))
        schemes.append(scheme)
        cs.append(c)
        vs.append(v)
        ds.append(har.d(c, v))
