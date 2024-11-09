class DBClient:
    def __init__(self, db_url: str):
        self._engine = None
        self._session = None
        self._cache = self._get_profile_cache()

    def _get_profile_cache(self):
        print(self._session)
        print("Return  created session")
        return {"": ""}

    def ping(self):
        return f"{__name__} is Working!!!"
