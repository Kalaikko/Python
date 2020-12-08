import pickle
fav = ['parotta','salna','kalakki']
filePath = 'e:\\Kalai Python\\favor.dat'
save_file = open(filePath,'wb')
pickle.dump(fav,save_file)
save_file.close()
load_file = open(filePath,'rb')
loadedData = pickle.load(load_file)
print(loadedData)
load_file.close()
