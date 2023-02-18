import pandas as pd
import user_pb2

if __name__ == '__main__':
    user = user_pb2.User()
    df = pd.DataFrame()
    print(f"hello, {user}, {df.shape}")
