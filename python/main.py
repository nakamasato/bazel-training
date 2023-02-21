import pandas as pd
from proto.user_pb2 import User

if __name__ == '__main__':
    user = User()
    user.id = "id1"
    user.name = "John"
    df = pd.DataFrame()
    print(f"hello, {user.id=} {user.name=}, {df.shape=}")
