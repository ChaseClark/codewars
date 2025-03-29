from collections import defaultdict
import random
import string


class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.encode_map:
            short_url = str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = short_url
            self.decode_map[short_url] = longUrl
        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.decode_map[shortUrl]


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
assert url == codec.decode(codec.encode(url))


# alt version


class Codec2:
    codeDB, urlDB = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        code = "".join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlDB:
            return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB:
            code = self.getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        return self.codeDB[shortUrl]


codec2 = Codec2()
print(codec2.encode("youtube.com"))
