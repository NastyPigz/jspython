import json

def require(*files):
    for file in files:
        try:
            res = __import__(file)
            return res
        except:
            pass
        try:
            with open(file, "r") as f:
                content = f.read()
                if file.endswith(".json"):
                    return json.dumps(content)
            return content
        except Exception as e:
            print(e)
            raise Exception("File Not Found")