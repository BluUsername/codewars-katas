def generate_hashtag(s):
    result = '#' + ''.join(w.capitalize() for w in s.split())
    return result if 1 < len(result) <= 140 else False
