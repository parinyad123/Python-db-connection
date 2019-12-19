from pymongo import  MongoClient

if __name__ == "__main__":
    # Build connection
    con=MongoClient("localhost",27017)
    # connect database "company"
    db=con.get_database("Stock")
    # build collection employees
    emp=db.Stockprice
    # insert document
    emp.insert({"name":"DDD","price":"154"})
    emp.insert({"name": "OUI", "price": "784"})
    emp.insert({"name": "YTG", "price": "741"})