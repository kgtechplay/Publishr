class ObjectStore:
    def put(self, key: str, content: bytes) -> str:
        return f"s3://bucket/{key}"
