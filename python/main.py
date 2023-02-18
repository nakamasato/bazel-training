import pandas as pd
from python.user_pb2 import User

if __name__ == '__main__':
    user = User()
    df = pd.DataFrame()
    print(f"hello, {user}, {df.shape}")
