'''
Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).
'''


def flatten_dictionary(dictionary):
    # for every key:
    # cond1: if value is not a dictionary, return val
    # else:
    # if key2 is not empty, set key = key.key2
    # check cond1
    flat = {}
    flatten("", dictionary, flat)
    print(flat)
    return flat


def flatten(initKey, d, flatD):
    for k, v in d.items():
        print(initKey, d, flatD, k, v)
        if not isinstance(v, dict):
            if initKey == None or initKey == "":
                flatD[k] = v
            else:
                if k == "":
                    flatD[initKey] = v
                else:
                    flatD[initKey+"."+k] = v

        else:
            if initKey == None or initKey == "":
                return flatten(k, v, flatD)
            else:
                if k == "":
                    return flatten(initKey, v, flatD)
                return flatten(initKey+"."+k, v, flatD)


dic2 = {"Key": {"a": "2", "b": "3"}}

dic1 = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

dic3 = {"Key1": "1", "Key2": {
    "a": "2", "b": "3", "c": {"d": "3", "e": {"f": "4"}}}}

dic4 = {"a": {"b": {"c": {"d": {"e": {"f": {"": "awesome"}}}}}}}
dic5 = {"a": "1"}

print(flatten_dictionary(dic5))

'''Input:
{"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}
Expected:
{"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}'''

'''Input:
{"Key":{"a":"2","b":"3"}}
Expected:
{"Key.a":"2","Key.b":"3"}'''

'''Input:
{"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}
Expected:
{"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}'''

'''Input:
{"":{"a":"1"},"b":"3"}
Expected:
{"a":"1","b":"3"}'''

'''Input:
{"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}
Expected:
{"a.b.c.d.e.f":"awesome"}'''

'''Input:
{"a":"1"}
Expected:
{"a":"1"}'''
