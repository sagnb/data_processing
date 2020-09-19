def cross_validation(data, k=10):
  outcomes = data.Outcome.value_counts().index # classes do problema
  class_data = [data[data.Outcome == outcome] for outcome in outcomes] # separação das instancias em classes
  class_quant = [] # quantidade de cada classe para manter a proporção
  class_remainder = [] # resto da div
  for data in class_data:
    class_quant.append(int(data.shape[0] / k))
    class_remainder.append(int(data.shape[0] % k))
  folds = [pd.DataFrame(columns=data.columns) for i in range(k)] # inicia a lista de folds
  for data in class_data:
    data.index = range(data.shape[0]) # reindex das tabelas
  for i in range(k): # para cada fold
    for j in range(len(class_data)): # para cada classe
      for _ in range(class_quant[j]): # até a quantidade certa
        index = randint(0, class_data[j].shape[0]-1) # determina o index
        folds[i] = folds[i].append(class_data[j].iloc[index], ignore_index=True) # adiciona a instancia em um fold
        class_data[j].drop([index], inplace=True) # retira da tabela
        class_data[j].index = range(class_data[j].shape[0]) # reindex
      if class_remainder[j] > 0:
        index = randint(0, class_data[j].shape[0]-1)
        folds[i] = folds[i].append(class_data[j].iloc[index], ignore_index=True)
        class_data[j].drop([index], inplace=True)
        class_data[j].index = range(class_data[j].shape[0])
        class_remainder[j] -= 1
  new_train_datas = [pd.DataFrame(columns=data.columns) for i in range(k)] # inicia a lista de dados de treinamento
  new_test_datas = [pd.DataFrame(columns=data.columns) for i in range(k)] # inicia a lista de dados de teste
  for i in range(k): # cria as novas tabelas de dados utilizando os folds
    new_test_datas[i] = new_test_datas[i].append(folds[i], ignore_index=True)
    for j in range(k):
      if i != j:
        new_train_datas[i] = new_train_datas[i].append(folds[j], ignore_index=True)
  return (new_train_datas, new_test_datas)
