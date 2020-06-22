from typing import List, Dict, Any

UserInfo = Dict[str, Any]

def select(*field_names: str):
    """ This function select necessary fields.​
    :param *field_names: List of necessary fields that can be in a result data.​
    :type *field_names: str.​
    :returns: List[UserInfo].
    """
    def inner(data: List[UserInfo]):
        for userinfo in data:
            for key in list(userinfo.keys()):
                if key not in field_names:
                    del userinfo[key]
        return data
    return inner

def field_filter(field_name: str, *values):
    """ This function is used to filter data.
    :param field_name: The field_name is used to extract only those records that
    fulfill a specified condition. This function filter data and select nec field that can be in a result data.​
    :type field_name: str.​
    :param *values: This param contains the possible values for field_name.​
    :type *values: str.​
    :returns: List[UserInfo].
    """
    def inner(data: List[UserInfo]):
        return [u for u in data if u[field_name] in values]
    return inner

def query(data: List[UserInfo], selection, *filters: callable) -> List[Dict[str, Any]]:
    """This function filter data and select necessary fields that can be in a result data.​
    :param data: Data that should be filtered.​
    :type data: List[UserInfo].
    ​:param selection: Function for select  necessary fields.
    ​:type selection: callable.​
    ​:param *filters: Function for filtering  data.
    ​:type *filters: callable.
    :returns: List[UserInfo].
    """
    s = selection
    for filt in filters:
        f = filt
        data = f(data)
    data = s(data)
    return data




friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол'}
]

# Пример работы программы:​
#
result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', 'Баскетбол', 'Волейбол'),
    field_filter('gender', 'Мужской')
)

print(f'result = {result}')

