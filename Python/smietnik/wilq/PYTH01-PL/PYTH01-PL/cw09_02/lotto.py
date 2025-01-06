from scipy.special import comb

k = int(input('Ile liczb będziesz losował? '))
n = int(input('Spośród ilu liczb? '))

szansa = comb(n, k, exact=True)
print(f'Szansa na trafienie {k} liczb spośród {n} wynosi 1 : {szansa:,}')
