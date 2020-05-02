import requests

def test_wordcount():
    data = {
        "top": 10,
        # "texts": [
        #     "string 1",
        #     "string 2"
        # ]
        "texts": "this is a string"
    }

    response = requests.post("http://localhost:5000/api/wordcount/", data)
    print(response.text)

test_wordcount()