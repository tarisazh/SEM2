from dotenv import load_dotenv
import os

load_dotenv()

nama_depan = os.getenv("VARIABLE_DEPAN")
nama_belakang = os.getenv("VARIABLE_BELAKANG")

print("VARIBLE_DEPAN : ", nama_depan)
print("VARIBLE_BELAKANG :", nama_belakang)