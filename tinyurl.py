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
