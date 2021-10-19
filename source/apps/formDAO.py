import pandas as pd

data_url = 'apps/data/form_data.csv'

states = {
    'SP': 'São Paulo',
    'RJ': 'Rio de Janeiro',
    'MG': 'Minas Gerais'
}

genders = {
    'F': 'Female',
    'M': 'Male',
    'NA': 'N/A'
}

languages = {
    'P': 'Python',
    'J': 'Java',
    'C': 'C#',
    'JS': 'Java Script',
    'PR': 'Pearl'
}

def get_all():

    data = pd.read_csv(data_url)
    return data

def add_data(name, city, gender, languages):
    current_data = get_all()

    return_message = 'OK'

    if name in current_data['name'].values:
        print("{} already exists".format(name))
        return_message = 'Name already exists'
    else:
        print('adding new entry')
        form_dataset = {
            'name': name, 
            'city': city,
            'gender': gender,
            'languages': languages
        }
        current_data = current_data.append(form_dataset, ignore_index=True)
        current_data.to_csv(data_url, index=False)
    
    return return_message



