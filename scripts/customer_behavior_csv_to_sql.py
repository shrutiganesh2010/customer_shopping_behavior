from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv(r"C:\Users\Shru\Downloads\customer_shopping_behavior\data\customer_shopping_behavior_cleaned.csv")

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"      
password = "password" 
host = "localhost"         
port = "5432"              
database = "customer_behavior"   

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")


# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"   
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


