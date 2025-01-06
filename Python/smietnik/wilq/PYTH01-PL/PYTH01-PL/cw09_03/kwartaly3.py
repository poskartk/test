import numpy as np

rok = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
       'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

kwartaly = np.array(rok).reshape(4, 3).tolist()

print(*kwartaly, sep='\n')
