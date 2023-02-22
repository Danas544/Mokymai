import logging
logging.basicConfig(level=logging.DEBUG,filename='Mokymai/02.22/data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
name = input("Enter Your Name:\n")
logging.info(f"{name} has logged in successfully !!")