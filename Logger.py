import logging
import Method_Over_Loading
def main():
    logging.basicConfig(filename="looging.log", level=logging.INFO)
    logging.info("Program started")
    result = Method_Over_Loading.add(7,6,8)
    logging.info("Done!")
 
if __name__ == "__main__":
    main()
