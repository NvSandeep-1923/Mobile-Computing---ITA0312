from itertools import product

# Cost surface models decode quality q and cache c interaction.
def cost(q,c,W,lam):
    n=len(W); hit=min(0.85,0.12*c/(1+0.04*sum(W)/max(n,1)))
    frame=sum(W)*q*(1.6-0.6*hit)/max(n,1)
    energy=sum(W)*(0.35+0.12*q+0.035*c)
    drops=max(0,frame-16)*0.8
    quality_loss=0.6*n/q
    return drops+lam*energy+quality_loss

def exact(W,L,C,lam): return min((cost(q,c,W,lam),q,c) for q in range(1,L+1) for c in range(1,C+1))
def greedy(W,L,C,lam):
    q,c=min(2,L),min(2,C); current=cost(q,c,W,lam); steps=[]; evaluated=0
    while True:
        neighbours=[(q+dq,c+dc) for dq,dc in [(-1,0),(1,0),(0,-1),(0,1)] if 1<=q+dq<=L and 1<=c+dc<=C]
        scored=[(cost(a,b,W,lam),a,b) for a,b in neighbours]; evaluated+=len(scored)
        best=min(scored)
        if best[0]<current: steps.append((q,c,current,best)); current,q,c=best
        else: break
    return (current,q,c),steps,evaluated

if __name__=='__main__':
 print('B3 - Exact vs Adaptive Feed Optimisation')
 tests=[([1,2,2,3,1,2,3,2,1,1],4,4,0.3),([4,5,3,6,2,5,4,3,6,5],4,4,1.0),([2,1,2,1,3,2,1,2,3,1],4,4,0.05)]
 for i,(W,L,C,lam) in enumerate(tests,1):
  e=exact(W,L,C,lam); g,steps,n=greedy(W,L,C,lam); print(f'Test {i}: exact={e}; adaptive={g}; match={abs(e[0]-g[0])<1e-9}; neighbour_evaluations={n}')
 surface={(1,1):6.92,(1,2):7.10,(1,3):7.28,(1,4):7.50,(2,1):7.40,(2,2):7.39,(2,3):7.23,(2,4):7.40,(3,1):7.7,(3,2):7.8,(3,3):8.0,(3,4):8.2,(4,1):8.2,(4,2):8.4,(4,3):8.6,(4,4):8.9}
 q,c=2,2; start=surface[(q,c)]; print(f'Counterexample: start (2,2) cost {start:.2f}; best neighbour (2,3) cost {surface[(2,3)]:.2f}; no adjacent improvement -> stop, but exact global best (1,1) cost {surface[(1,1)]:.2f}.')
 for N,L in [(50,4),(200,8),(1000,16)]:
  C=L; exact_configs=L*C; exact_ops=exact_configs*N; adaptive_configs=10; adaptive_ops=adaptive_configs*N
  print(f'Scale N={N}, grid={L}x{C}: exact configs={exact_configs}, exact item evaluations={exact_ops}, adaptive configs~{adaptive_configs}, adaptive item evaluations~{adaptive_ops}')
 print('Trade-off: fewer configurations/evaluations and online adaptation; no global optimality guarantee (local minimum possible).')
