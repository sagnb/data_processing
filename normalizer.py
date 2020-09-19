def min_max(data):
  for column in data.columns:
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
  return data
