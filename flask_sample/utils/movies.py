import os
# fix for testing just this file
if __name__ == "__main__":
    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)
from utils.api import API
class movies(API):
    @staticmethod
    def get_movie(movie,params = {"exact":"false"}):
        return API.get(f"/titles/search/title/{movie}", params )

if __name__ == "__main__":
    querystring = {"exact":"false","titleType":"movie"}
    resp = movies.get_movie("spiderman",querystring)
    print(resp)
